# E-Commerce Data Pipeline Project

Student Name: Kella KANAKA LAVANYA
Roll Number: 23A91A1228
Submission Date: 25-12-2025

## Project Overview

This project implements a complete end-to-end data engineering pipeline for an e-commerce analytics platform. It demonstrates proficiency in:

- **Data Pipeline Development**: Complete ETL/ELT workflow from data generation to BI dashboards
- **Database Design**: Normalized production schemas and dimensional warehouse models
- **Data Quality Assurance**: Comprehensive validation and monitoring systems
- **Automation & Orchestration**: Automated scheduled pipelines with error handling
- **Business Intelligence**: Professional dashboards with actionable insights
- **DevOps Practices**: Containerization, CI/CD, testing, and documentation

## Success Criteria Achieved

✓ Processes 30,000+ records with 100% referential integrity
✓ Three-tier schema design (staging, production, warehouse)
✓ Comprehensive data quality validation across 5 dimensions
✓ Idempotent ETL pipeline with transaction atomicity
✓ SCD Type 2 dimensional modeling for historical tracking
✓ 10 optimized analytical queries on warehouse schema
✓ Professional BI dashboard with 16+ visualizations
✓ Complete automation with error handling and monitoring
✓ Docker containerization with health checks
✓ GitHub CI/CD pipeline with automated testing
✓ 80%+ unit test coverage

## Technology Stack

- **Data Generation**: Python (Faker library)
- **Database**: PostgreSQL (Local/Docker)
- **Data Processing**: Python (Pandas, SQLAlchemy)
- **Orchestration**: Python scheduler with error handling
- **Visualization**: Tableau Public / Power BI Desktop
- **Containerization**: Docker & Docker Compose
- **Testing**: Pytest
- **Version Control**: Git & GitHub
- **CI/CD**: GitHub Actions

## Project Structure

```
ecommerce-data-pipeline/
├── data/
│   ├── raw/                    # Generated CSV files
│   ├── staging/                # Staging schema data
│   └── processed/              # Processed output
├── scripts/
│   ├── data_generation/        # Data generation scripts
│   ├── ingestion/              # Data ingestion scripts
│   ├── transformation/         # ETL transformation scripts
│   └── quality_checks/         # Data quality validation
├── sql/
│   ├── ddl/                    # Table creation scripts
│   ├── dml/                    # Data manipulation
│   └── queries/                # Analytical queries
├── dashboards/
│   ├── tableau/                # Tableau workbooks
│   ├── powerbi/                # Power BI files
│   └── screenshots/            # Dashboard screenshots
├── docker/
│   ├── Dockerfile              # Container configuration
│   └── docker-compose.yml      # Service orchestration
├── config/
│   └── config.yaml             # Configuration file
├── logs/                       # Log files
├── docs/
│   ├── architecture.md         # Architecture documentation
│   ├── dashboard_guide.md      # Dashboard guide
│   └── api_documentation.md    # Pipeline documentation
├── tests/                      # Unit tests
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Docker & Docker Compose
- Git
- Tableau Public or Power BI Desktop

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Lavanyakanaka/ecommerce-analytics-data-pipeline-23A91A1228.git
cd ecommerce-analytics-data-pipeline-23A91A1228
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start Docker services:
```bash
docker-compose up -d
```

### Running the Pipeline

```bash
python scripts/pipeline_orchestrator.py
```

## Database Configuration

- **Database Name**: ecommerce_db
- **Staging Schema**: staging
- **Production Schema**: production
- **Warehouse Schema**: warehouse

## Key Features

### Data Generation
- 1,000 customers with realistic data distribution
- 500 products across multiple categories
- 10,000 transactions with 15,000-25,000 transaction items
- 100% referential integrity (zero orphan records)

### Data Quality
- 5 quality dimensions: completeness, uniqueness, validity, consistency, referential integrity
- Weighted quality scoring methodology
- Detailed JSON reports for violations

### ETL Pipeline
- Staging schema for fast bulk loading
- Production schema with 3NF normalization
- Data cleansing and enrichment
- Business rule application
- Transaction atomicity

### Warehouse
- Star schema dimensional modeling
- 4 dimension tables (customers, products, date, payment_method)
- 1 fact table with SCD Type 2 support
- 3 aggregate tables for performance

### Analytics
- 10 optimized analytical queries
- Advanced SQL techniques (CTEs, window functions, subqueries)
- Professional BI dashboard
- Interactive filters and visualizations

### Automation
- Pipeline orchestrator with error handling
- Exponential backoff retry logic
- Scheduled execution via Cron/Airflow
- Comprehensive logging and monitoring

## Key Insights from Analytics

- Top performing product categories and revenue trends
- Customer segmentation by spending patterns
- Geographic analysis of sales distribution
- Payment method preferences
- Daily sales patterns and seasonal trends
- Product profitability analysis

## Challenges & Solutions

1. **Data Consistency**: Implemented database transactions and idempotent load strategies
2. **Performance**: Created strategic indexes and aggregate tables for query optimization
3. **Service Dependencies**: Used Docker health checks with service_healthy conditions
4. **SCD Type 2**: Managed surrogate keys and version control for dimensional history
5. **Quality Validation**: Balanced thoroughness with performance through weighted scoring

## Future Enhancements

- Real-time streaming with Apache Kafka
- Cloud deployment (AWS/GCP/Azure)
- Advanced ML models for predictive analytics
- Real-time alerting system
- Incremental SCD Type 4 support
- API layer for data access

## Contact

For questions or issues, please contact:
- Email: lavanyakanaka@example.com
- GitHub: https://github.com/Lavanyakanaka/ecommerce-analytics-data-pipeline-23A91A1228

---

## Submission Information

**GitHub Repository**: https://github.com/Lavanyakanaka/ecommerce-analytics-data-pipeline-23A91A1228
**Status**: ✓ Submitted Successfully
**Deadline**: 27 Dec 2025, 04:59 PM
