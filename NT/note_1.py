
import pyspark

import pandas as pd
pd.read_csv('online-retail-dataset.csv')

from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Repo').getOrCreate()

spark

df_pyspark=spark.read.csv('online-retail-dataset.csv')

df_pyspark=spark.read.option('header', 'true').csv('online-retail-dataset.csv')

df_pyspark.printSchema()