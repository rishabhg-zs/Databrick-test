# Databricks notebook source
df1 = spark.sql("select * from ngpp_dmp_family_tree_hierarchy")
display(df1)

# COMMAND ----------

df2 = spark.sql("select * from ngpp_dmp_ppa_act_itm_dtl_tbl")
display(df2)