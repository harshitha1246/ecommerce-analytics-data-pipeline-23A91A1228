-- Warehouse schema for analytics
CREATE SCHEMA IF NOT EXISTS warehouse;

-- Fact table for transactions
CREATE TABLE IF NOT EXISTS warehouse.fact_transactions (
    fact_id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    amount DECIMAL(10, 2),
    transaction_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sales aggregates table
CREATE TABLE IF NOT EXISTS warehouse.sales_aggregates (
    aggregate_id SERIAL PRIMARY KEY,
    product_id VARCHAR(50),
    total_sales DECIMAL(15, 2),
    transaction_count INTEGER,
    aggregation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customer dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    email VARCHAR(255),
    country VARCHAR(100)
);

-- Product dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Create indexes
CREATE INDEX idx_warehouse_transactions_date ON warehouse.fact_transactions(transaction_date);
CREATE INDEX idx_warehouse_products ON warehouse.dim_products(product_id);
