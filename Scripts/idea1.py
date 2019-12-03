from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import functions
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
pathAMD = "../datasets/amd_cpu.csv"

steamDF = sqlContext.read.option("header", "true").csv(pathSteam)
reqDF = sqlContext.read.option("header", "true").csv(pathReq)
intelDF = sqlContext.read.option("header", "true").csv(pathIntel)
amdDF = sqlContext.read.option("header", "true").csv(pathAMD)

# PREPARAMOS LAS VARIABLES QUE VAMOS A UTILIZAR (SIN TERMINAR)
#-----------------------------------------------
intelDF = intelDF.select("Product_Collection", "Vertical_Segment", "Processor_Number",
 "Status", "Recommended_Customer_Price", "nb_of_Cores", "nb_of_Threads", "Processor_Base_Frequency",
 "DirectX_Support", "Instruction_Set")

amdDF = amdDF.select("Processor Family", "Processor Code Name", "Microarchitecture", "Processor Model",
 "Processor Date", "Processor Clock [MHz]", "Threads/core", "Cores")

steamDF = steamDF.select("appid", "name")

reqDF = reqDF.select("steam_appid","minimum")


#LIMPIAMOS LOS DATASETS
intelRDD = intelDF.rdd.filter(lambda p: (p["Vertical_Segment"] != ' 1600"') & (p["Vertical_Segment"] != '4'))

reqRDD = reqDF.rdd.filter(lambda x: 'Hz' or 'hz' in x["minimum"])

reqDF = reqRDD.toDF()

split = functions.split(reqDF['minimum'], 'Hz' or 'hz')
reqDF = reqDF.withColumn('Herzios', split.getItem(0))
reqDF.show(100)