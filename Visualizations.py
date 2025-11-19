# Databricks notebook source
#Revenue Trend
df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "revenue"))


# COMMAND ----------

#  Revenue vs COGS vs Gross Profit
df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "revenue", "cogs", "gross_profit"))


# COMMAND ----------

#  YoY Revenue Growth (%)
df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "revenue_yoy_pct"))


# COMMAND ----------

# Profit Breakdown
df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "gross_profit", "operating_income", "net_income"))


# COMMAND ----------

# Margins Over Time
df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "gross_margin", "operating_margin", "net_margin"))


# COMMAND ----------

#  Rolling Margins
df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "gross_margin_rolling3", "net_margin_rolling3"))


# COMMAND ----------

#   KPI Table (to use Counter visualizations on dashboard)
df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "roa", "roe"))


# COMMAND ----------

# ROA & ROE Over Time
df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "roa", "roe"))


# COMMAND ----------

# BALANCE SHEET (gold_balance_sheet)
df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","total_assets","total_liabilities","total_equity"))


# COMMAND ----------

# Working Capital Trend
df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","working_capital"))


# COMMAND ----------

# Assets / Liabilities / Equity
df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","delta_assets","delta_liabilities","delta_equity"))


# COMMAND ----------

# CASH FLOW (gold_cashflow)
df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year","cash_flow_operations","cash_flow_investing","cash_flow_financing"))


# COMMAND ----------

# Free Cash Flow
df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year","free_cash_flow"))


# COMMAND ----------

#  Net Change in Cash
df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year","net_change_in_cash"))


# COMMAND ----------

# DATA QUALITY TABLES
df = spark.table("gold_completeness").orderBy("year")
display(df.select("company","year","completeness_pct"))



# COMMAND ----------

# Missing Years
df = spark.table("gold_missing_years")
display(df)


# COMMAND ----------

df = spark.table("gold_pnl")
display(df)
