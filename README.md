📊 Financial Reporting Automation Framework

A complete end-to-end system for automated financial data ingestion, cleansing, transformation, warehousing, and reporting using Python, BigQuery, Streamlit, and multi-source financial datasets.

📘 Overview

This project automates the financial reporting lifecycle by consolidating multiple data sources (Yahoo Finance, Kaggle, custom CSVs), applying transformation logic, loading a governed warehouse model into BigQuery, and generating dynamic financial statements through a Streamlit application.

The system follows a Medallion Architecture (Bronze → Silver → Gold) to ensure data quality, lineage, and analytical readiness.

🎯 Objectives

Automate extraction of financial data from multiple sources

Cleanse and normalize heterogeneous financial datasets

Design a dimensional BigQuery warehouse with facts & dimensions

Enable standardized P&L, Balance Sheet, and Cash Flow statements

Automate period-end close processes and variance reporting

Provide a Streamlit UI for interactive analysis & export

🛠️ Tech Stack / Tools Used

Python (ETL, transformations, APIs)

Google BigQuery (staging, warehouse, marts)

Streamlit (UI for statements & analytics)

Yahoo Finance API

Kaggle Financial Datasets

Pandas / NumPy

Medallion Architecture

📥 Data Sources
Source	Type	Description
Yahoo Finance	REST / CSV	Market prices, fundamentals, financials
Kaggle Financial Open Data	CSV	Financial statements & macro indicators
Custom CSV Inputs	User-provided	GL balances, transactions, COA mappings
🧱 Architecture
External Sources 
   ↓
Python ETL 
   ↓
BigQuery 
  (Bronze → Silver → Gold)
   ↓
Streamlit App (Financial Statements + KPIs)

🗂️ Dimensional Warehouse Model
Dimensions
Table	Description
dim_account	COA details, hierarchy, rollups
dim_entity	Legal entities, regions, currencies
dim_date	Calendar + fiscal date attributes
Facts
Table	Grain	Description
fact_gl_balances	Account x Entity x Period	Opening, movement, closing balances
fact_transactions	Journal entry lines	Debit/credit, amounts, txn metadata
🥇 Medallion Layers in BigQuery
🟤 Bronze Layer (Raw)

Stores raw CSV/API extracts

Minimal parsing

Example: bronze.gl_raw, bronze.marketdata_raw

⚪ Silver Layer (Cleansed)

Data quality checks

Standardized COA mappings

SCD Type 2 for dimensions

Example: silver.dim_account, silver.fact_transactions

🟡 Gold Layer (Curated Marts)

Final analytical models

KPIs, statements, dashboards

Example:

gold.pnl_statement

gold.balance_sheet

gold.cashflow_statement

gold.kpi_finance

📊 Features of the Streamlit App
✔️ Standardized Reports

Profit & Loss

Balance Sheet

Cash Flow (Indirect)

✔️ Variance Analysis

YoY / QoQ

Actual vs Budget

Forecast vs Actual

✔️ KPI Dashboard

Gross Margin

Operating Margin

ROA, ROE

Free Cash Flow

✔️ Export Capabilities

CSV, Excel, and PDF downloads

🔄 Period-End Automation

Includes automated processes for:

Data completeness checks

Missing file detection

Late-submission alerts

Calendar-driven close workflow

📂 Project Structure
├── data/
│   ├── raw/
│   ├── processed/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── sql/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
├── streamlit/
│   ├── app.py
├── config/
│   ├── settings.yaml
├── README.md

🚀 How to Run the Project
1. Install Dependencies
pip install -r requirements.txt

2. Configure BigQuery Credentials
gcloud auth application-default login

3. Run ETL
python etl/extract.py
python etl/transform.py
python etl/load.py

4. Launch Streamlit App
streamlit run streamlit/app.py

📁 Sample Dataset Included

This repo includes a sample financial CSV dataset (FINANCIAL.csv) for:

Cleansing

Transformation

Validation

Warehouse loading

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue to discuss what you’d like to modify
