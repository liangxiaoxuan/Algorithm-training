# coding=utf-8

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
        # Spark-sql
        spark-sql-file.py

#### 4.Troubleshooting cluster jobs

#### 5.Spark RDD transformation: map / flatmap / Reduce --- RDD just data placeholder 

```python
from pyspark import SparkConf, SparkContext

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

#### 7.SparkSQL (DataFrame and Dataset) # SparkSession内部封装了SparkContext
```python
# coding=utf-8

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
    - Start it with sbin/start-thriftserver.sh
    - Listens on port 10000 by default
    - Connect using bin/beeline -u jdbc:hive2://localhost:10000
    - Have SQL shell to Spark SQL
    - Can create new tables, or query existing ones that were cached using hiveCtx.cacheTable("tablename")
* sparksql-Rdd / sparksql-dataframe: spark-sql-file.py
  
* DataFrame more fit for structured data
* Using SQL Functions:
```python

from pyspark.sql import functions as func
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
func.explode()   # similar to flatmap; explodes columns into rows
inputDF = spark.read.text("file:///SparkCourse/book.txt")
func.split(inputDF.value."\\W+")
func.col("columnName")  # to refer to a column
func.lower()

```
#### 8. Shared variables: 节点间共享内容 -- 不同的node访问同一个变量时
* Broadcast variables (shared variable or shard datasets): 分布式只读共享变量
    - Spark automatically broadcasts the common data needed by tasks within each stage. The data broadcasted this way 
is cached in serialized form and deserialized before running each task 
    - Use spark.broadcast() to ship off whatever you want 
    - Use .value() to get the object back 
```python
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName("NameoftheApp").getOrCreate()

broadcasteVar = spark.sparkContext.broadcast()
broadcasteVar.value  # show ["value"]

```
       
* Accumulators: "added"：分布式只写共享变量-- 共享变量一直在改变
    - each task in a executor will add this accumulator variable. (先分后总)
    
```python
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf = conf)
accum = sc.accumulator(0)  # initial value of 0  
# can be a counter = 0 which in python while loop, increment the counter
accum.add(1)  # add any value to accumulator 
accum.value # Get the accumulated value 
```

#### 9.Spark Graphx: Breath-First Search (iterative) :广度优先搜索算法： 查找最短路径

#### 10. read into RDD VS Dataframe
```python
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf = conf)

# RDD
rdd=sc.textFile("/path_to_csv_file_in_HDFS/factbook.csv")
mappedRdd= rdd.map(lambda x:x.split(";"))  # transformation
mappedRdd.collect() # Action

# DataFrame
# 1.Convert entire RDD to Data Frame
#getting header
headerRdd=sc.textFile("/path_to_csv_file_in_HDFS/factbook.csv").map(lambda x:x.split(";")).take(1)[0]

#Convert Entire CSV to DF 
df=sc.textFile("/path_to_csv_file_in_HDFS/factbook.csv").map(lambda x:x.split(";")).filter(lambda x:x[0]!='Country' and x[0]!='String').toDF(headerRdd)

#Convert SELECTED COLUMNS FROM CSV to DF 
from pyspark.sql import Row
df=sc.textFile("/path_to_csv_file_in_HDFS/factbook.csv").map(lambda x:x.split(";")).filter(lambda x:x[0]!='Country' and x[0]!='String').map(lambda x:Row(country=x[0],birth_rate=x[1],death_rate=x[4],gdp=x[9],highway_km=x[15],import_=x[16],export_=x[8])).toDF()

#Show the DF in tabular format
df.show(5)

# DataFrame (DF) to SQL Temp Table in HIVE
df.registerTempTable("factbook")
mySelectQuery=sqlContext.sql("SELECT * FROM factbook")
mySelectQuery.show(3)


# load data into DataFrame
from pyspark.sql import SparkSession
spark = SparkSession.builder.config("spark.sql.warehouse.dir").appName("jsontransformation").getOrCreate()
df = spark.read.text("path").rdd

```


 






