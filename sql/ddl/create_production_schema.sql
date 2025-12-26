-- Create production schema - Phase 2
-- This schema contains fully normalized, validated data (3NF)
-- Ready for business operations with full integrity constraints

CREATE SCHEMA IF NOT EXISTS production;

-- CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS production.customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    registration_date DATE NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    age_group VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_format CHECK (email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'),
    CONSTRAINT valid_registration_date CHECK (registration_date <= CURRENT_DATE)
);

CREATE INDEX idx_customers_email ON production.customers(email);
CREATE INDEX idx_customers_registration_date ON production.customers(registration_date);

-- PRODUCTS TABLE
CREATE TABLE IF NOT EXISTS production.products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    sub_category VARCHAR(100),
    price DECIMAL(12, 2) NOT NULL,
    cost DECIMAL(12, 2) NOT NULL,
    brand VARCHAR(100),
    stock_quantity INT DEFAULT 0,
    supplier_id VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT price_positive CHECK (price > 0),
    CONSTRAINT cost_positive CHECK (cost > 0),
    CONSTRAINT cost_less_than_price CHECK (cost < price),
    CONSTRAINT stock_non_negative CHECK (stock_quantity >= 0)
);

CREATE INDEX idx_products_category ON production.products(category);
CREATE INDEX idx_products_price ON production.products(price);

-- TRANSACTIONS TABLE
CREATE TABLE IF NOT EXISTS production.transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_time TIME,
    payment_method VARCHAR(50),
    shipping_address VARCHAR(500),
    total_amount DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES production.customers(customer_id),
    CONSTRAINT total_amount_positive CHECK (total_amount > 0),
    CONSTRAINT valid_transaction_date CHECK (transaction_date <= CURRENT_DATE)
);

CREATE INDEX idx_transactions_customer_id ON production.transactions(customer_id);
CREATE INDEX idx_transactions_date ON production.transactions(transaction_date);
CREATE INDEX idx_transactions_payment_method ON production.transactions(payment_method);

-- TRANSACTION_ITEMS TABLE
CREATE TABLE IF NOT EXISTS production.transaction_items (
    item_id VARCHAR(20) PRIMARY KEY,
    transaction_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(12, 2) NOT NULL,
    discount_percentage DECIMAL(5, 2) DEFAULT 0,
    line_total DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_transaction FOREIGN KEY (transaction_id) REFERENCES production.transactions(transaction_id),
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES production.products(product_id),
    CONSTRAINT quantity_positive CHECK (quantity > 0),
    CONSTRAINT unit_price_positive CHECK (unit_price > 0),
    CONSTRAINT discount_valid CHECK (discount_percentage >= 0 AND discount_percentage <= 100),
    CONSTRAINT line_total_positive CHECK (line_total > 0)
);

CREATE INDEX idx_transaction_items_transaction_id ON production.transaction_items(transaction_id);
CREATE INDEX idx_transaction_items_product_id ON production.transaction_items(product_id);

-- LOADING ORDER NOTES:
-- 1. Load customers first (no dependencies)
-- 2. Load products second (no dependencies)
-- 3. Load transactions third (depends on customers)
-- 4. Load transaction_items last (depends on transactions and products)
