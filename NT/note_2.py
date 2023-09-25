from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('DF_workflow_1').getOrCreate()

spark

#read the dataset
workflow_1=spark.read.option('header','true').csv('/content/sample_data/california_housing_test.csv', inferSchema=True)

#Check the schema
workflow_1.printSchema()

workflow_1=spark.read.csv('/content/sample_data/california_housing_test.csv', header=True, inferSchema=True)
workflow_1.show()

workflow_1.head(1)

workflow_1.select(['longitude', 'latitude', 'total_rooms']).show(5)

workflow_1.dtypes

workflow_1.describe().show()

#Adding columns in data frame
workflow_1.withColumn('habitants',workflow_1['population']/10)

#drop columns
workflow_1.drop('housing_median_age').show(5)

workflow_1.withColumnRenamed('longitude', 'Longitud').show(5)