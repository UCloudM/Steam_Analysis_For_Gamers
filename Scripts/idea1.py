from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import functions
import string
'''from pyspark.sql import Row
from pyspark.sql.types import StringType
import string
import sys
import re'''


conf = SparkConf().setMaster('local').setAppName('Script')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# LEEMOS LOS DATASETS EN FORMATO CSV
#----------------------------------
pathSteam = "../datasets/steam.csv"
pathReq = "../datasets/steam_requirements_data.csv"
pathIntel = "../datasets/Intel_CPUs.csv"
pathAMD = "../datasets/amd.csv"

steamDF = sqlContext.read.option("header", "true").csv(pathSteam)
reqDF = sqlContext.read.option("header", "true").csv(pathReq)
intelDF = sqlContext.read.option("header", "true").csv(pathIntel)
amdDF = sqlContext.read.option("header", "true").csv(pathAMD)

# PREPARAMOS LAS VARIABLES QUE VAMOS A UTILIZAR (SIN TERMINAR)
#-----------------------------------------------
intelDF = intelDF.select("Product_Collection", "Vertical_Segment", "Processor_Number",
 "Status", "nb_of_Cores", "nb_of_Threads", "Processor_Base_Frequency",
 "DirectX_Support", "Instruction_Set")

amdDF = amdDF.select("Model", "Family", "Platform", "Launch Date", "# of CPU cores",
 "# of Threads", "Base Clock", "Max Boost Clock")

steamDF = steamDF.select("appid", "name")

reqDF = reqDF.select("steam_appid", "minimum")

#LIMPIAMOS LOS DATASETS
intelRDD = intelDF.rdd.filter(lambda p: (p["Vertical_Segment"] != ' 1600"') & (p["Vertical_Segment"] != '4'))


reqDF = reqDF.withColumn('minimum', functions.lower(functions.col('minimum')))
reqDF = reqDF.filter(reqDF.minimum.contains('hz'))
split = functions.split(reqDF['minimum'], ' ')
reqDF = reqDF.withColumn('Herzios', split.getItem('hz'))
reqDF.show(100)