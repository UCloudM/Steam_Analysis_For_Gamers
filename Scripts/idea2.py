from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import functions
import string
import re

'''from pyspark.sql import Row
from pyspark.sql.types import StringType
import string
import sys
import re'''


conf = SparkConf().setMaster('local').setAppName('Script')
#sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

#PATHS DE LOS DATASETS
#-----------------------------
pathSteam = "../datasets/steam.csv"
pathReq = "../datasets/steamReq.csv"
pathIntel = "../datasets/Intel_CPUs.csv"
pathAMD = "../datasets/amd.csv"

#PARA LIMPIAR EL CSV
'''req = sc.textFile("../datasets/steam_requirements_data.csv")
req = req.map(lambda line: re.sub(r'<[^<>]+>', ' ', line))
req = req.map(lambda line: re.sub(r"[\']", ' ', line))
req.saveAsTextFile("steamReq.csv")'''

# LEEMOS LOS DATASETS EN FORMATO CSV
#----------------------------------
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
#-----------------------------------------------
intelDF = intelDF[(~intelDF["Vertical_Segment"].contains(' 1600"')) &
                  (~intelDF["Vertical_Segment"].contains('4')) &
                  (~intelDF["Vertical_Segment"].contains('null')) &
                  (~intelDF["Vertical_Segment"].contains('eDP/DP/HDMI'))]

intelDF = intelDF[(~intelDF["Processor_Base_Frequency"].isNull()) & 
                  (~intelDF["Processor_Number"].isNull())]

reqDF = reqDF.withColumn('minimum', functions.lower(functions.col('minimum')))
reqDF = reqDF[(reqDF["minimum"].contains("hz"))]

reqDF = reqDF.withColumn('minimum', 
                         functions.regexp_replace(reqDF['minimum'], 'recommended(.*)', ''))

#HAY 2 PROCESADORES CON FRECUENCIA EN MHZ Y AMBOS ESTAN MAL/INCOMPLETOS
amdDF = amdDF[~amdDF["Base Clock"].contains("MHz")]

#MAPEAMOS EL DATASET DE INTEL
#(FRECUENCIA (EN MHZ), Nº PROCESADOR, Nº NUCLEOS, GENERACIOn)
#----------------------------------------------
def frecuencia(freq) :
    if freq[1] == "GHz":
        return float(freq[0]) * 1000
    else:
        return float(freq[0])


'''def generacion(gen) :
    if gen[3] == "Processors":
        return gen[2]
    elif gen[3] == "Processor":
        return gen[0]
    elif gen[4] == "Series":
        return gen[3] + " Series"
    elif gen[4] == "Family":
        if gen[3] == "Product":
            return gen[3] + " Product Family"
        if gen[2] == "Processor":
            return gen[2] + " " + gen[3] + " Family"
        return gen[3] + " Family"
    elif gen[4] == "Series":
        return gen[3] + " Series"
    else:
        return "null"'''
        

intelRDD = intelDF.rdd.map(lambda p: (frecuencia(p["Processor_Base_Frequency"].split(" ")),
                                      (p["Product_Collection"],
                                       p["nb_of_Cores"],
                                       p["Processor_Number"])))

amdDF = amdDF.withColumn("Base Clock", 
                          functions.regexp_extract(amdDF["Base Clock"], '[0-9]*\.*[0-9]*', 0))
                         
amdRDD = amdDF.rdd.map(lambda p: (float(p["Base Clock"])*1000, 
                                  (p["Family"],
                                   p["# of CPU cores"],
                                   p["Model"])))
