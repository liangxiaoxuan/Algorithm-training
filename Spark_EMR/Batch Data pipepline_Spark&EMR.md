

### Spark: 
in memory, fast batch computation framework, with rich set of APIs including SparkSQL, PySpark, SparkR
#### AWS EMR: 
EMR is easy to use, supports numerous distributed framework, such as Spark.which is no need for in house cluster management.

#### Spark: RDD (resilient distributed datasets) 
* Create sub datasets without any data, the sub datasets called RDD
* Data will be loaded into sub datasets when we submit a Spark job 
* Create RDD's from a txt file: sc.textFile("file dict from S3n:// or hdfs://)
* Create RDD's from Hive: 
    * hiveCtx = HiveContect(sc)
    * rows = hiveCtx.sql("select**")
  

### Run Spark on EMR Cluster:
#### 1.Connect Putty with EC2 and EMR
dict: Spark_EMR/pUTTY connect EC2&EMR

#### 2.Write data analysis or transformation codes using Pyspark and save into S3
#### 3.To run on EMR successfully + output results for Star Wars:
        aws s3 cp s3://sundog-spark/MovieSimilarities1M.py ./ (s3 py file)
        aws s3 cp s3://sundog-spark/ml-1m/movies.dat ./   （用于look up 的file）
        spark-submit --executor-memory 1g MovieSimilarities1M.py 260

#### 4.Troubleshooting cluster jobs

#### 5.Spark RDD transformation: map / flatmap / Reduce --- RDD just data placeholder 

```python
from pyspark import SparkContest

# initializing Spark
conf = SparkConf()  # For configuring Spark.
sc = SparkContext(conf=conf)  # Main entry point for Spark functionality
list1 = [1,2,3,4,5,6]

# Parallelized Collections
l = sc.parallelize(list1) 

y = l.map(lambda x : (x,x**2)

```
* 1. **map()**: Return a new distributed dataset formed by passing each element of the
  source through a function func.
     
* 2. **filerMap()**: Similar ro map(), but each input item can be mapped to 0 or more items 
     (func should return a Seq rather than a single item)
     
* 3. **sc.parallelize(list)**:the distributed dataset (distData) from list can be operated on in parallel For example, 
     we can call distData.reduce(lambda a, b: a + b) to add up the elements of the list
     * parallelize(list,number of partitions)
    
* 4. **foreach()**: it executes a function specified in for each element of Dataframe/Datasets
    
* 5. **collect()**: return all the elements of the dataset as an array at the driver.
     retrieve/feed all the elements of the dataset (from all nodes) to the driver node
     
#### 6.RDD get Data from hdfs
* After RDD transformation --- will trigger a spark job ---  retrieve data from hdfs to RDD 

#### 7.SparkSQL (DataFrame and Dataset)
```python

from pyspark.sql import SparkSession, Row
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
inputData = spark.read.json("dataFile")
inputData.createOrReplaceTempView("myStructuredStuff")  # it looks like DB table
myResultDataFrame = spark.sql("sql scripts")

# DataFrame
myResultDataFrame.show()
myResultDataFrame.select("someFiledName")
myResultDataFrame.filter(myResultDataFrame("someFileName" > 200))
myResultDataFrame.groupBy(myResultDataFrame("someFileName")).mean()
# turn back to RDD
myResultDataFrame.rdd().map("mapperfunction")


```

* Extend RDD to a "DataFrame" object 
* DataFrame: MLlib and Spaek Streaming are moving toward using DataFrames instead of Rdd
* Dataset: More in Scala
* SparkSQL exposes a JDBC/ODBC server (if you built Spark with Hive support)
    1.Start it with sbin/start-thriftserver.sh
    2.Listens on port 10000 by default
    3.Connect using bin/beeline -u jdbc:hive2://localhost:10000
    4.Have SQL shell to Spark SQL
    5.Can create new tables, or query existing ones that were cached using hiveCtx.cacheTable("tablename")


 




