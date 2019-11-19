from pyspark import SparkConf, SparkContext, SQLContext, sql
from pyspark.sql import Row
from pyspark.sql.types import StringType
import string
import sys
import re

conf = SparkConf().setMaster('local').setAppName('Script')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

RDDvar1 = sc.textFile("steam.csv")
RDDvar2 = sc.textFile("steam_requirements_data.csv")
sqlContext.createDataFrame(RDDvar1, StringType()).show()

sqlContext.createDataFrame(RDDvar2, StringType()).show()
'''
par = RDDvar.map(lambda fila: (((re.split(r',', fila)[3]), float(re.split(r',',fila)[4]))))

atuple = (0,0.0) 

resul = par\
		.aggregateByKey(atuple, lambda x, y: (x[0] + y, x[1]+1.0),
					lambda x, y: (x[0] + y[0], x[1]+y[1]))\
		.mapValues(lambda v: v[0]/v[1])\
		.sortByKey()
df = sqlContext.createDataFrame(resul,["Type", "Average"]).show()'''

