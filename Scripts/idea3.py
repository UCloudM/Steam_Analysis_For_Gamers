from pyspark import SparkConf, SparkContext, SQLContext
'''from pyspark.sql import Row
from pyspark.sql.types import StringType
import string
import sys
import re'''


conf = SparkConf().setMaster('local').setAppName('Script')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# LEEMOS EL DATASET EN FORMATO CSV
#----------------------------------
pathSteam = "../datasets/steam.csv"
steamDF = sqlContext.read.option("header", "true").csv(pathSteam)

# PREPARAMOS LAS VARIABLES QUE VAMOS A UTILIZAR
#-----------------------------------------------
dataDF = steamDF.select("developer", "categories", "positive_ratings", "negative_ratings")
# Lista de elementos unicos para cada columna
developerList = steamDF.select("developer").distinct().collect()
categoriesList = steamDF.select("categories").distinct().collect()
positiveR_List = steamDF.select("positive_ratings").distinct().collect()
negativeR_List = steamDF.select("negative_ratings").distinct().collect()


for developer in developerList:
    # Hacer split de las categorias de cada desarrolladora de forma que cada elemento que salga, sea la clave en un diccionario




#print(developerDF.show(15, False))



# Idea: Crear un diccionario con otro diccionario dentro que contenga la info como se ve en el documento Notas Proyecto
# diccionario( Desarrolladora, Diccionario( Categoria, Lista(VotosPositivos, VotosNegativos) )

# Sobre ese diccionario realizar las consultas necesarias cuando se introduzca la entrada

# Cada desarrolladora podria tener distintos juegos con distintas categorias cada juego, por lo que si alguna se repite en distintos juegos,
# habria que contabilizar los votos en una misma variable. Por esto sería útil tener cada categoría como una clave de un diccionario, para
# que no se repita.
# Aqui hay un ejemplo:
df = dataDF.filter(dataDF.developer == "Valve")
print(df.show(15, False))

# El rating de arriba es el perteneciente a un juego. Habria que sumar todos los votos positivos entre si, los negativos entre si
# de todos los juegos de una misma categoria y obtener un porcentaje que indique lo bueno que es








