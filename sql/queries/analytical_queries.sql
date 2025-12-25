-- Analytical queries for Phase 4

-- Top 10 products by sales
SELECT 
    p.product_name,
    SUM(ft.amount) as total_sales,
    COUNT(ft.fact_id) as num_transactions
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_products p ON ft.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Daily sales trend
SELECT 
    ft.transaction_date,
    SUM(ft.amount) as daily_sales,
    COUNT(*) as transaction_count
FROM warehouse.fact_transactions ft
GROUP BY ft.transaction_date
ORDER BY ft.transaction_date DESC;

-- Customer spending summary
SELECT 
    c.customer_name,
    COUNT(ft.fact_id) as num_purchases,
    SUM(ft.amount) as total_spending,
    AVG(ft.amount) as avg_purchase_amount
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_customers c ON ft.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spending DESC;

-- Category performance
SELECT 
    p.category,
    SUM(ft.amount) as category_sales,
    COUNT(DISTINCT ft.customer_id) as unique_customers
FROM warehouse.fact_transactions ft
JOIN warehouse.dim_products p ON ft.product_id = p.product_id
GROUP BY p.category
ORDER BY category_sales DESC;
