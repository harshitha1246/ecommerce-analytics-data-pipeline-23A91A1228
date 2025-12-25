-- Staging schema for raw data
CREATE SCHEMA IF NOT EXISTS staging;

-- Staging table for raw transactions
CREATE TABLE IF NOT EXISTS staging.raw_transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    category VARCHAR(100),
    amount DECIMAL(10, 2),
    timestamp TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staging table for customer data
CREATE TABLE IF NOT EXISTS staging.raw_customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    country VARCHAR(100),
    registration_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staging table for product data
CREATE TABLE IF NOT EXISTS staging.raw_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_staging_transactions_customer ON staging.raw_transactions(customer_id);
CREATE INDEX idx_staging_transactions_timestamp ON staging.raw_transactions(timestamp);
