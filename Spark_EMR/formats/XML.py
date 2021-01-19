# Transform XML files into  DataFrame
# write cvs files to the destination
# XML file -- semi-structured
# Process: XML files --- RDD (TEXTFiles) --- flatmap  --- ToDF
# https://q15928.github.io/2019/07/14/parse-xml/

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType
import xml.etree.ElementTree as ET
import datetime
# create sessions

spark = SparkSession.builder.appName('xmltransformation').getOrCreate()

# read each xml file as one row, then convert to RDD
file_rdd = spark.read.text("./data/*.xml", wholetext=True) # this is DF
file_rdd = spark.read.text("./data/*.xml", wholetext=True).rdd  # this is rdd

# Parse XML files, extract the records, and expand into multiple RDDs
# parse each xml content into records according the pre-defined schema.
# Python standard library xml.etree.ElementTree to parse
# and extract the xml elements into a list of record
# Missing value = value and set up datatype


def parse_xml(rdd):
    """
    Read the xml string from rdd, parse and extract the elements,
    then return a list of list.
    """
    results = []
    root = ET.fromstring(rdd[0]),
    ELEMENTS_TO_EXTRAT = ["author", "title", "genre", "price", "publish_date", "description"]

    for b in root.findall('book'):
        rec = []
        rec.append(b.attrib['id'])
        for e in ELEMENTS_TO_EXTRAT:
            if b.find(e) is None:
                rec.append(None)
                continue
            value = b.find(e).text
            if e == 'price':
                value = float(value)
            elif e == 'publish_date':
                value = datetime.strptime(value, '%Y-%m-%d')
            rec.append(value)
        results.append(rec) 

    return results


# iteration by flatmap()
# parse xml tree, extract the records and transform to new RDD
records_rdd = file_rdd.flatMap(parse_xml)

# Convert RDDs into DataFrame
# convert RDDs to DataFrame with the pre-defined schema
my_schema = StructType([
    StructField("book_id", StringType(), True),
    StructField("author", StringType, True),
    StructField("title", StringType(), True),
    StructField("genre", StringType, True),
    StructField("price", StringType(), True),
    StructField("publish_date", StringType, True),
    StructField("description", StringType(), True)
])
book_df = records_rdd.toDF(my_schema)

# save DataFrame as csv file
# write to csv
book_df.write.format("csv").mode("overwrite")\
    .save("./output")