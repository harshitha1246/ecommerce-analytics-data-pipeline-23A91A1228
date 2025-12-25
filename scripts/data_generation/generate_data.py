"""Data generation script for e-commerce pipeline"""
import random
import csv
from datetime import datetime, timedelta
import os

def generate_sample_data(output_file, num_records=10000):
    """
    Generate sample e-commerce data.
    
    Args:
        output_file: Path to output CSV file
        num_records: Number of records to generate
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['transaction_id', 'customer_id', 'product_id', 'category', 'amount', 'timestamp'])
        
        for i in range(num_records):
            transaction_id = f'TXN_{i+1:010d}'
            customer_id = f'CUST_{random.randint(1, 1000):05d}'
            product_id = f'PROD_{random.randint(1, 500):05d}'
            category = random.choice(categories)
            amount = round(random.uniform(10, 500), 2)
            timestamp = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
            
            writer.writerow([transaction_id, customer_id, product_id, category, amount, timestamp])
    
    print(f'Generated {num_records} records in {output_file}')

if __name__ == '__main__':
    generate_sample_data('data/staging/raw_transactions.csv', num_records=10000)
