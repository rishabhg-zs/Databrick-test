# Databricks notebook source
df1 = spark.sql("select * from ngpp_dmp_family_tree_hierarchy")
display(df1)

# COMMAND ----------

df2 = spark.sql("select * from ngpp_dmp_ppa_act_itm_dtl_tbl")
display(df2)

# COMMAND ----------

df3 = spark.sql("select * from ngpp_dmp_ppa_adv_wek_tbl_csv")
display(df3)

# COMMAND ----------

df4 = spark.sql("select * from ngpp_dmp_ppa_esp_com_lvl_tbl")
display(df4)

# COMMAND ----------

df5 = spark.sql("select * from ngpp_dmp_ppa_esp_itm_dtl_tbl")
display(df5)

# COMMAND ----------

df6 = spark.sql("select * from ngpp_dmp_ppa_prj_com_lvl_tbl")
display(df6)

# COMMAND ----------

df7 = spark.sql("select * from ngpp_dmp_ppa_prj_itm_dtl_tbl")
display(df7)

# COMMAND ----------

df8 = spark.sql("select * from ngpp_dmp_ppa_sls_typ_tbl")
display(df8)

# COMMAND ----------

df9 = spark.sql("select * from ngpp_dmp_con_upc_div_no")
display(df9)

# COMMAND ----------

df10 = spark.sql("select * from ngpp_dmp_ppa_act_com_lvl_tbl")
display(df10)

# COMMAND ----------

df11 = spark.sql("select * from ngpp_vw_sls_wek_bdv_dpt")
display(df11)

# COMMAND ----------

df12 = spark.sql("select * from ngpp_vw_asl_wek_sto_com_cpr")
display(df12)

# COMMAND ----------

df13 = spark.sql("select * from ngpp_vw_asl_wek_bdv_con_cpr")
display(df13)

# COMMAND ----------

df14 = spark.sql("select * from ngpp_dmp_extract_corp_intermediate")
display(df14)

# COMMAND ----------

df15 = spark.sql("select * from large_div_output_1")
display(df15)

# COMMAND ----------

df16 = spark.sql("select * from ppa_esp_pmy_dpt_lvl_tbl_v2")
display(df16)

# COMMAND ----------

df17 = spark.sql("select * from ngpp_dmp_espquery1")
display(df17)
