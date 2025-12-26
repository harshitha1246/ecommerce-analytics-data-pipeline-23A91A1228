# E-Commerce Analytics Data Pipeline - Complete Guide

## Project Overview

This is a production-ready data pipeline for e-commerce analytics that processes 30,000+ records, maintains data integrity, and provides meaningful business insights through visual analytics.

### Key Features
- ✅ **Data Generation**: Creates 30,000+ synthetic e-commerce records
- ✅ **Data Quality**: Comprehensive validation and quality checks
- ✅ **Data Transformation**: Cleans and transforms raw data
- ✅ **Analytics Queries**: 10+ pre-built SQL analytics queries
- ✅ **Interactive Dashboard**: Streamlit-based BI dashboard
- ✅ **Unit Tests**: Complete test coverage
- ✅ **Documentation**: Comprehensive guides and documentation

## Project Structure

```
.
├── dataraw/                    # Raw data folder
│   ├── customers/
│   ├── products/
│   └── transactions/
├── datastaging/                # Staging data folder
├── dataprocessed/              # Processed data folder
├── scripts/                    # Python scripts
│   ├── data_generation/
│   │   └── generate_data.py
│   ├── data_quality_transformation.py
│   ├── dashboard.py
│   └── pipeline_orchestrator.py
├── sql/                        # SQL scripts
│   └── analytics_queries.sql
├── tests/                      # Test files
│   └── test_pipeline.py
├── config/                     # Configuration files
├── docker/                     # Docker setup
├── docs/                       # Documentation
└── requirements.txt            # Python dependencies
```

## Data Pipeline Phases

### Phase 1: Data Generation
**Script**: `scripts/data_generation/generate_data.py`

Generates synthetic e-commerce data with:
- **5,000 customers** with attributes: ID, name, email, country, signup date, lifetime value
- **500 products** with attributes: ID, name, category, price, stock quantity, supplier ID
- **30,000 transactions** with attributes: ID, customer ID, product ID, date, quantity, price, total, payment method, status

**Command**:
```bash
python scripts/data_generation/generate_data.py
```

### Phase 2: Data Quality & Transformation
**Script**: `scripts/data_quality_transformation.py`

Performs:
- Missing value detection
- Duplicate detection
- Data type validation
- Date conversions
- Field enrichment (full name, price ranges, monthly aggregation)

**Command**:
```bash
python scripts/data_quality_transformation.py
```

### Phase 3: Analytics & Insights
**SQL Queries**: `sql/analytics_queries.sql`

Includes:
1. Total Revenue by Month
2. Top 10 Products by Revenue
3. Customer Segmentation
4. Monthly Growth Rate
5. Payment Method Analysis
6. Product Category Performance
7. Customer Geographic Distribution
8. Transaction Status Distribution
9. Customer Retention Metrics
10. Product Performance Trend

### Phase 4: Visualization
**Script**: `scripts/dashboard.py`

Streamlit-based interactive dashboard with:
- KPI metrics (revenue, transactions, AOV, customer count)
- Revenue trends and daily transaction volume
- Product performance analysis
- Payment method breakdown
- Customer segmentation insights

**Command**:
```bash
streamlitrun scripts/dashboard.py
```

## Installation

### Prerequisites
- Python 3.8+
- pip
- PostgreSQL (optional, for production)

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/Lavanyakanaka/ecommerce-analytics-data-pipeline-23A91A1228.git
cd ecommerce-analytics-data-pipeline-23A91A1228
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Create data directories**:
```bash
mkdir -p dataraw/customers dataraw/products dataraw/transactions
mkdir -p datastaging dataprocessed
```

## Usage

### Complete Pipeline Execution

```bash
# 1. Generate synthetic data
python scripts/data_generation/generate_data.py

# 2. Apply data quality and transformations
python scripts/data_quality_transformation.py

# 3. Run tests
python -m pytest tests/

# 4. View analytics dashboard
streamlit run scripts/dashboard.py
```

### Individual Components

**Data Generation Only**:
```bash
python scripts/data_generation/generate_data.py
```

**Data Validation Only**:
```bash
python scripts/data_quality_transformation.py
```

**Run Tests**:
```bash
python -m pytest tests/test_pipeline.py -v
```

## Data Quality Checks

The pipeline performs comprehensive quality checks:

- **Missing Values**: Detects and reports null values
- **Duplicates**: Identifies duplicate records
- **Data Types**: Validates data type consistency
- **Negative Values**: Checks for invalid negative amounts
- **Foreign Keys**: Validates relationships between tables
- **Data Integrity**: Ensures referential integrity

## Analytics Queries

### Revenue Analysis
```sql
-- Total Revenue by Month
SELECT DATE_TRUNC('month', transaction_date) AS month,
       SUM(total_amount) AS revenue
FROM transactions
WHERE status = 'Completed'
GROUP BY month;
```

### Customer Insights
```sql
-- Customer Segmentation
SELECT customer_id,
       SUM(total_amount) AS total_spent,
       CASE WHEN SUM(total_amount) > 5000 THEN 'VIP'
            WHEN SUM(total_amount) > 1000 THEN 'Premium'
            ELSE 'Regular' END AS segment
FROM transactions
GROUP BY customer_id;
```

### Product Performance
```sql
-- Top Products
SELECT p.product_name,
       SUM(t.total_amount) AS revenue,
       COUNT(*) AS transactions
FROM products p
JOIN transactions t ON p.product_id = t.product_id
GROUP BY p.product_name
ORDER BY revenue DESC LIMIT 10;
```

## Testing

### Run Unit Tests
```bash
python -m pytest tests/test_pipeline.py -v
```

### Test Coverage
The test suite covers:
- Data generation (customers, products, transactions)
- Data quality checks (missing values, duplicates)
- Data transformations
- Data integrity validation
- Pipeline execution

## Configuration

### Environment Variables
```bash
# Database connection (if using PostgreSQL)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_analytics
DB_USER=postgres
DB_PASSWORD=password
```

### Configuration File
Edit `config/pipeline_config.json` to customize:
- Number of records to generate
- Data paths
- Data quality thresholds

## Output Files

### Raw Data
- `dataraw/customers/customers_raw.csv` - 5,000 customer records
- `dataraw/products/products_raw.csv` - 500 product records
- `dataraw/transactions/transactions_raw.csv` - 30,000 transaction records
- `dataraw/metadata.json` - Data generation metadata

### Processed Data
- `dataprocessed/customers_processed.csv` - Transformed customer data
- `dataprocessed/products_processed.csv` - Transformed product data
- `dataprocessed/transactions_processed.csv` - Transformed transaction data

## Performance Metrics

- **Data Generation**: ~2-3 seconds for 30,000 transactions
- **Data Transformation**: ~1-2 seconds
- **Dashboard Load**: <1 second
- **Query Performance**: <500ms for most analytics queries

## Troubleshooting

### Missing Data Files
```bash
# Ensure data directories exist
mkdir -p dataraw/customers dataraw/products dataraw/transactions
python scripts/data_generation/generate_data.py
```

### Import Errors
```bash
# Update dependencies
pip install -r requirements.txt --upgrade
```

### Dashboard Not Displaying
```bash
# Ensure Streamlit is installed
pip install streamlit>=1.0
streamlit run scripts/dashboard.py
```

## Contributing

To contribute improvements:
1. Create a feature branch
2. Make your changes
3. Add/update tests
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation in `/docs`
- Review SQL queries in `/sql`

## Version History

- **v1.0.0**: Initial release with complete pipeline
  - Data generation (30,000 records)
  - Quality checks and transformation
  - 10 analytics queries
  - Interactive dashboard
  - Comprehensive tests
  - Full documentation
