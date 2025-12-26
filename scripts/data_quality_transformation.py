#!/usr/bin/env python3
"""
Data Quality & Transformation Script for E-Commerce Analytics Pipeline
Performs data validation, cleaning, and transformation
"""

import pandas as pd
import numpy as np
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATARAW_PATH = "../../dataraw"
DATASTAGING_PATH = "../../datastaging"
DATAPROCESSED_PATH = "../../dataprocessed"

class DataQualityTransformation:
    """Handle data quality checks and transformations"""
    
    def __init__(self):
        self.quality_report = {}
        self.row_counts = {}
        
    def load_data(self):
        """Load raw data files"""
        logger.info("Loading raw data...")
        
        customers_df = pd.read_csv(f'{DATARAW_PATH}/customers/customers_raw.csv')
        products_df = pd.read_csv(f'{DATARAW_PATH}/products/products_raw.csv')
        transactions_df = pd.read_csv(f'{DATARAW_PATH}/transactions/transactions_raw.csv')
        
        self.row_counts['customers'] = len(customers_df)
        self.row_counts['products'] = len(products_df)
        self.row_counts['transactions'] = len(transactions_df)
        
        logger.info(f"Loaded {len(customers_df)} customers, {len(products_df)} products, {len(transactions_df)} transactions")
        return customers_df, products_df, transactions_df
    
    def check_data_quality(self, customers_df, products_df, transactions_df):
        """Perform data quality checks"""
        logger.info("Performing data quality checks...")
        
        quality_checks = {}
        
        # Customer quality checks
        quality_checks['customers'] = {
            'missing_values': int(customers_df.isnull().sum().sum()),
            'duplicates': int(customers_df.duplicated().sum()),
            'total_records': len(customers_df)
        }
        
        # Product quality checks
        quality_checks['products'] = {
            'missing_values': int(products_df.isnull().sum().sum()),
            'duplicates': int(products_df.duplicated().sum()),
            'negative_prices': int((products_df['price'] < 0).sum()) if 'price' in products_df.columns else 0,
            'total_records': len(products_df)
        }
        
        # Transaction quality checks
        quality_checks['transactions'] = {
            'missing_values': int(transactions_df.isnull().sum().sum()),
            'duplicates': int(transactions_df.duplicated().sum()),
            'negative_amounts': int((transactions_df['total_amount'] < 0).sum()) if 'total_amount' in transactions_df.columns else 0,
            'total_records': len(transactions_df)
        }
        
        self.quality_report = quality_checks
        logger.info(f"Quality checks complete: {quality_checks}")
        return quality_checks
    
    def transform_data(self, customers_df, products_df, transactions_df):
        """Apply transformations to data"""
        logger.info("Applying data transformations...")
        
        # Transform customers
        customers_df['signup_date'] = pd.to_datetime(customers_df['signup_date'])
        customers_df['full_name'] = customers_df['first_name'] + ' ' + customers_df['last_name']
        
        # Transform products
        if 'price' in products_df.columns:
            products_df['price_range'] = pd.cut(products_df['price'], 
                                                 bins=[0, 100, 500, 1000, float('inf')],
                                                 labels=['Budget', 'Mid-Range', 'Premium', 'Luxury'])
        
        # Transform transactions
        if 'transaction_date' in transactions_df.columns:
            transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'])
            transactions_df['month'] = transactions_df['transaction_date'].dt.to_period('M')
        
        logger.info("Data transformations applied successfully")
        return customers_df, products_df, transactions_df
    
    def save_processed_data(self, customers_df, products_df, transactions_df):
        """Save processed data"""
        logger.info("Saving processed data...")
        
        Path(DATAPROCESSED_PATH).mkdir(parents=True, exist_ok=True)
        
        # Save processed data
        customers_df.to_csv(f'{DATAPROCESSED_PATH}/customers_processed.csv', index=False)
        products_df.to_csv(f'{DATAPROCESSED_PATH}/products_processed.csv', index=False)
        transactions_df.to_csv(f'{DATAPROCESSED_PATH}/transactions_processed.csv', index=False)
        
        logger.info("Processed data saved successfully")

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("Data Quality & Transformation Pipeline")
    print("="*60)
    
    try:
        transformer = DataQualityTransformation()
        customers_df, products_df, transactions_df = transformer.load_data()
        quality_report = transformer.check_data_quality(customers_df, products_df, transactions_df)
        customers_df, products_df, transactions_df = transformer.transform_data(customers_df, products_df, transactions_df)
        transformer.save_processed_data(customers_df, products_df, transactions_df)
        
        print("\n" + "="*60)
        print("Transformation completed successfully!")
        print("Quality Report:", quality_report)
        print("="*60 + "\n")
        return 0
        
    except Exception as e:
        logger.error(f"Error during transformation: {str(e)}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
