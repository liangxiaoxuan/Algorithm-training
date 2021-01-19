from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# create session
spark = SparkSession.builder.config("spark.sql.warehouse.dir").appName("jsontransformation").getOrCreate()

# simple json
# read into dataframe
readJSONDF = spark.read.json('Simple.json')
readJSONDF.show(truncate=False)

# Multi-Line Complex JSON

# use multiline = true to read multi line JSON file
readComplexJSONDF = spark.read.option("multiLine", "true").json('ComplexJSON.json')

# Explode Array to Structure
explodeArrarDF = readComplexJSONDF.withColumn('Exp_RESULTS', F.explode(F.col('details'))).drop('details')

# Read location and name
dfReadSpecificStructure = explodeArrarDF.select("Exp_RESULTS.user.location.*","Exp_RESULTS.user.name.*")
dfReadSpecificStructure.show(truncate=False)


from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf=conf)



