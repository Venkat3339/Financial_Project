# Databricks notebook source
df_bronze = spark.read.table("financial_reporting_5000_v_2")
display(df_bronze)

# COMMAND ----------

df_bronze.write.format("delta").mode("overwrite").saveAsTable("finance_bronze")

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog `workspace`;
# MAGIC
# MAGIC alter table `default`.`financial_reporting_5000_v_2`
# MAGIC drop column record_type;
# MAGIC
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Gross Profit` to Gross_Profit;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Operating Expense` to Operating_Expense;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Interest Expense` to Interest_Expense;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Tax Expense` to Tax_Expense;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Net Income` to Net_Income;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Assets` to Total_Assets;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Liabilities` to Total_Liabilities;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Equity` to Total_Equity;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Operations` to Cash_Flow_Operations;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Investing` to Cash_Flow_Investing;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Financing` to Cash_Flow_Financing;
# MAGIC ALTER TABLE `default`.`financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Net Change in Cash` to Net_Change_in_Cash;
# MAGIC
# MAGIC

# COMMAND ----------

