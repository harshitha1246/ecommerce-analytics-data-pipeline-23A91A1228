"""Data ingestion script to load data into staging schema"""
import psycopg2
import csv
from psycopg2.extras import execute_batch
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, host, database, user, password, port=5432):
        self.conn_params = {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'port': port
        }
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Establish connection to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.cursor = self.conn.cursor()
            logger.info('Connected to database successfully')
        except Exception as e:
            logger.error(f'Failed to connect: {str(e)}')
            raise
    
    def ingest_transactions(self, csv_file):
        """Load transaction data into staging table"""
        try:
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                rows = []
                for row in reader:
                    rows.append((
                        row['transaction_id'],
                        row['customer_id'],
                        row['product_id'],
                        row['category'],
                        float(row['amount']),
                        row['timestamp']
                    ))
                
                query = '''
                    INSERT INTO staging.raw_transactions 
                    (transaction_id, customer_id, product_id, category, amount, timestamp)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (transaction_id) DO NOTHING
                '''
                
                execute_batch(self.cursor, query, rows, page_size=1000)
                self.conn.commit()
                logger.info(f'Ingested {len(rows)} transactions')
        except Exception as e:
            logger.error(f'Error during ingestion: {str(e)}')
            self.conn.rollback()
            raise
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            logger.info('Connection closed')

if __name__ == '__main__':
    ingestion = DataIngestion(
        host='postgres',
        database='ecommerce_db',
        user='admin',
        password='password'
    )
    ingestion.connect()
    ingestion.ingest_transactions('data/staging/raw_transactions.csv')
    ingestion.close()
