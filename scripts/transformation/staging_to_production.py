"""Transform staging data to production warehouse schema"""
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataTransformation:
    def __init__(self, host, database, user, password):
        self.conn_params = {'host': host, 'database': database, 'user': user, 'password': password}
        self.conn = psycopg2.connect(**self.conn_params)
        self.cursor = self.conn.cursor()
    
    def transform_transactions(self):
        """Transform raw transactions to dimension and fact tables"""
        query = '''
            INSERT INTO warehouse.fact_transactions 
            (transaction_id, customer_id, product_id, amount, transaction_date)
            SELECT 
                transaction_id,
                customer_id,
                product_id,
                amount,
                DATE(timestamp)
            FROM staging.raw_transactions
            WHERE timestamp > CURRENT_DATE - INTERVAL '30 days'
        '''
        try:
            self.cursor.execute(query)
            self.conn.commit()
            logger.info(f'Transformed transactions successfully')
        except Exception as e:
            logger.error(f'Error transforming transactions: {e}')
            self.conn.rollback()
    
    def aggregate_sales(self):
        """Create sales aggregations"""
        query = '''
            INSERT INTO warehouse.sales_aggregates 
            (product_id, total_sales, transaction_count, aggregation_date)
            SELECT 
                product_id,
                SUM(amount) as total_sales,
                COUNT(*) as transaction_count,
                CURRENT_DATE
            FROM warehouse.fact_transactions
            GROUP BY product_id
        '''
        try:
            self.cursor.execute(query)
            self.conn.commit()
            logger.info('Sales aggregations created')
        except Exception as e:
            logger.error(f'Error in aggregation: {e}')
            self.conn.rollback()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    transformer = DataTransformation('postgres', 'ecommerce_db', 'admin', 'password')
    transformer.transform_transactions()
    transformer.aggregate_sales()
    transformer.close()
