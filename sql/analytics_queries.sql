-- E-Commerce Analytics Queries
-- This file contains SQL queries for business intelligence and analytics

-- Query 1: Total Revenue by Month
SELECT 
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(total_amount) AS total_revenue,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(*) AS transaction_count
FROM transactions
WHERE status = 'Completed'
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY month DESC;

-- Query 2: Top 10 Products by Revenue
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    SUM(t.total_amount) AS total_revenue,
    COUNT(*) AS transaction_count,
    AVG(t.total_amount) AS avg_transaction
FROM products p
JOIN transactions t ON p.product_id = t.product_id
WHERE t.status = 'Completed'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- Query 3: Customer Segmentation by Purchase Value
SELECT 
    customer_id,
    COUNT(*) AS purchase_count,
    SUM(total_amount) AS total_spent,
    AVG(total_amount) AS avg_transaction_value,
    CASE 
        WHEN SUM(total_amount) > 5000 THEN 'VIP'
        WHEN SUM(total_amount) > 1000 THEN 'Premium'
        ELSE 'Regular'
    END AS customer_segment
FROM transactions
WHERE status = 'Completed'
GROUP BY customer_id
ORDER BY total_spent DESC;

-- Query 4: Monthly Growth Rate
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', transaction_date) AS month,
        SUM(total_amount) AS revenue
    FROM transactions
    WHERE status = 'Completed'
    GROUP BY DATE_TRUNC('month', transaction_date)
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND(((revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100)::NUMERIC, 2) AS growth_rate_pct
FROM monthly_sales
ORDER BY month DESC;

-- Query 5: Payment Method Analysis
SELECT 
    payment_method,
    COUNT(*) AS transaction_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_transaction,
    ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER())::NUMERIC, 2) AS percentage_of_total
FROM transactions
WHERE status = 'Completed'
GROUP BY payment_method
ORDER BY total_revenue DESC;

-- Query 6: Product Category Performance
SELECT 
    p.category,
    COUNT(DISTINCT p.product_id) AS product_count,
    COUNT(*) AS transaction_count,
    SUM(t.total_amount) AS total_revenue,
    ROUND((SUM(t.total_amount) * 100.0 / SUM(SUM(t.total_amount)) OVER())::NUMERIC, 2) AS revenue_percentage
FROM products p
JOIN transactions t ON p.product_id = t.product_id
WHERE t.status = 'Completed'
GROUP BY p.category
ORDER BY total_revenue DESC;

-- Query 7: Customer Geographic Distribution
SELECT 
    country,
    COUNT(DISTINCT customer_id) AS customer_count,
    SUM(t.total_amount) AS total_revenue,
    ROUND((SUM(t.total_amount) * 100.0 / SUM(SUM(t.total_amount)) OVER())::NUMERIC, 2) AS revenue_percentage,
    ROUND(SUM(t.total_amount) / COUNT(DISTINCT c.customer_id)::NUMERIC, 2) AS avg_customer_value
FROM customers c
LEFT JOIN transactions t ON c.customer_id = t.customer_id AND t.status = 'Completed'
GROUP BY country
ORDER BY total_revenue DESC;

-- Query 8: Transaction Status Distribution
SELECT 
    status,
    COUNT(*) AS transaction_count,
    ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER())::NUMERIC, 2) AS percentage,
    SUM(total_amount) AS revenue_impact
FROM transactions
GROUP BY status
ORDER BY transaction_count DESC;

-- Query 9: Customer Retention Metrics
WITH customer_timeline AS (
    SELECT 
        customer_id,
        MIN(transaction_date) AS first_purchase,
        MAX(transaction_date) AS last_purchase,
        COUNT(*) AS lifetime_transactions,
        SUM(total_amount) AS lifetime_value
    FROM transactions
    WHERE status = 'Completed'
    GROUP BY customer_id
)
SELECT 
    DATE_TRUNC('month', first_purchase)::DATE AS cohort_month,
    COUNT(*) AS cohort_size,
    SUM(lifetime_transactions) AS total_transactions,
    ROUND((SUM(lifetime_value) / COUNT(*))::NUMERIC, 2) AS avg_clv
FROM customer_timeline
GROUP BY DATE_TRUNC('month', first_purchase)
ORDER BY cohort_month DESC;

-- Query 10: Product Performance Trend
SELECT 
    DATE_TRUNC('month', t.transaction_date)::DATE AS month,
    p.product_name,
    COUNT(*) AS units_sold,
    SUM(t.total_amount) AS revenue
FROM transactions t
JOIN products p ON t.product_id = p.product_id
WHERE t.status = 'Completed'
GROUP BY DATE_TRUNC('month', t.transaction_date), p.product_name
ORDER BY month DESC, revenue DESC;
