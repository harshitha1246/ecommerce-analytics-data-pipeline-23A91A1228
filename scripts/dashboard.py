#!/usr/bin/env python3
"""
BI Dashboard for E-Commerce Analytics Pipeline
Interactive dashboard using Streamlit for visualizing e-commerce metrics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("📊 E-Commerce Analytics Dashboard")
st.markdown("---")
st.write(
    "Real-time analytics dashboard for e-commerce business metrics, customer insights, and sales performance."
)

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    date_range = st.date_input(
        "Select date range",
        value=(datetime(2023, 1, 1), datetime(2023, 12, 31))
    )
    
    metrics_selection = st.multiselect(
        "Select metrics to display",
        ["Revenue", "Transactions", "Customer Insights", "Product Performance", "Payment Methods"],
        default=["Revenue", "Transactions", "Customer Insights"]
    )

# Create sample data for demonstration
@st.cache_data
def load_sample_data():
    """Load and cache sample data"""
    # This would load actual data from the pipeline
    np.random.seed(42)
    
    # Revenue by month
    months = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    revenue = np.random.uniform(50000, 100000, len(months))
    
    # Transactions by date
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    transactions = pd.DataFrame({
        'date': dates,
        'transactions': np.random.randint(50, 300, len(dates)),
        'revenue': np.random.uniform(10000, 50000, len(dates))
    })
    
    # Product data
    products = pd.DataFrame({
        'category': ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'],
        'revenue': np.random.uniform(50000, 200000, 5),
        'units_sold': np.random.randint(100, 1000, 5)
    })
    
    # Payment methods
    payment_methods = pd.DataFrame({
        'method': ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'],
        'transactions': [3500, 2100, 1800, 1200],
        'revenue': [150000, 95000, 85000, 62000]
    })
    
    # Customer data
    customers = pd.DataFrame({
        'segment': ['VIP', 'Premium', 'Regular'],
        'count': [250, 1200, 3550],
        'avg_clv': [5000, 1500, 500]
    })
    
    return transactions, products, payment_methods, customers, revenue, months

transactions_df, products_df, payment_df, customers_df, revenue_data, months = load_sample_data()

# KPI Metrics
st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Revenue",
        value=f"${revenue_data.sum()/1000:.0f}K",
        delta="+12.5% vs last month"
    )

with col2:
    st.metric(
        label="Total Transactions",
        value=f"{int(transactions_df['transactions'].sum()):,}",
        delta="+8.2% vs last month"
    )

with col3:
    st.metric(
        label="Average Order Value",
        value=f"${(revenue_data.sum() / transactions_df['transactions'].sum()):.2f}",
        delta="+5.1% vs last month"
    )

with col4:
    st.metric(
        label="Customer Count",
        value=f"{customers_df['count'].sum():,}",
        delta="+15.3% vs last month"
    )

st.markdown("---")

# Revenue and Transactions Charts
if "Revenue" in metrics_selection or "Transactions" in metrics_selection:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Trend")
        fig_revenue = px.line(
            x=months,
            y=revenue_data,
            labels={'x': 'Month', 'y': 'Revenue ($)'},
            title="Monthly Revenue Trend"
        )
        fig_revenue.update_traces(fill='tozeroy')
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        st.subheader("Daily Transactions")
        fig_transactions = px.bar(
            transactions_df.head(30),
            x='date',
            y='transactions',
            labels={'date': 'Date', 'transactions': 'Transactions'},
            title="Daily Transaction Volume (First 30 Days)"
        )
        st.plotly_chart(fig_transactions, use_container_width=True)

# Product and Category Performance
if "Product Performance" in metrics_selection:
    st.subheader("Product Performance")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_revenue_cat = px.bar(
            products_df,
            x='category',
            y='revenue',
            color='revenue',
            labels={'category': 'Category', 'revenue': 'Revenue ($)'},
            title="Revenue by Product Category"
        )
        st.plotly_chart(fig_revenue_cat, use_container_width=True)
    
    with col2:
        fig_units = px.pie(
            products_df,
            names='category',
            values='units_sold',
            title="Units Sold by Category"
        )
        st.plotly_chart(fig_units, use_container_width=True)

# Payment Method Analysis
if "Payment Methods" in metrics_selection:
    st.subheader("Payment Method Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_payment_revenue = px.bar(
            payment_df,
            x='method',
            y='revenue',
            color='method',
            labels={'method': 'Payment Method', 'revenue': 'Revenue ($)'},
            title="Revenue by Payment Method"
        )
        st.plotly_chart(fig_payment_revenue, use_container_width=True)
    
    with col2:
        fig_payment_trans = px.bar(
            payment_df,
            x='method',
            y='transactions',
            color='method',
            labels={'method': 'Payment Method', 'transactions': 'Transactions'},
            title="Transactions by Payment Method"
        )
        st.plotly_chart(fig_payment_trans, use_container_width=True)

# Customer Insights
if "Customer Insights" in metrics_selection:
    st.subheader("Customer Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_customer_seg = px.bar(
            customers_df,
            x='segment',
            y='count',
            color='segment',
            labels={'segment': 'Customer Segment', 'count': 'Count'},
            title="Customer Distribution by Segment"
        )
        st.plotly_chart(fig_customer_seg, use_container_width=True)
    
    with col2:
        fig_customer_clv = px.bar(
            customers_df,
            x='segment',
            y='avg_clv',
            color='segment',
            labels={'segment': 'Segment', 'avg_clv': 'Avg CLV ($)'},
            title="Average Customer Lifetime Value"
        )
        st.plotly_chart(fig_customer_clv, use_container_width=True)

st.markdown("---")
st.write(
    "_Dashboard Last Updated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "_"
)
st.write(
    "For more information about the data pipeline, visit the [project documentation](../docs)"
)
