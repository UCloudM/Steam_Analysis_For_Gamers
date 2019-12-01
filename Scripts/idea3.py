from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import Row
from pyspark.sql.types import StringType
import string
import sys
import re


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


steamMap = dict()

for developer in developerList:
    categoriesMap = dict()

    #Seleccionamos las categorias de la desarrolladora que estamos procesando
    developerInfoDF = dataDF.filter(dataDF.developer == str(developer)).distinct()
    developerInfoList = developerInfoDF.collect()

    # Hacemos un split de cada elemento de la lista de las categorias de cada desarrolladora de forma que cada uno sea la clave en un diccionario
    # El valor de ese diccionario sera una lista con los votos positivos y negativos.
    for row in developerInfoList:
        categories = row["categories"].split(";")
        rating = [int(row["positive_ratings"]), int(row["negative_ratings"])]
        for category in categories:
            if category in categoriesMap.keys():
                categoriesMap[category][0] += rating[0]
                categoriesMap[category][1] += rating[1]
            else:
                categoriesMap[category] = rating

    steamMap[developer] = categoriesMap

for developer, value in steamMap.items():
    print("-----------------------------------------------------------------------------------------")
    for key, values in value.items():
        print("Developer: " + str(developer))
        print("---------")
        print("Categoria: " + str(key))
        print("Votos Positivos: " + str(values[0]))
        print("Votos Negativos: " + str(values[1]))
        print("------------------------------------------------------")







# Idea: Crear un diccionario con otro diccionario dentro que contenga la info como se ve en el documento Notas Proyecto
# diccionario( Desarrolladora, Diccionario( Categoria, Lista(VotosPositivos, VotosNegativos) )

# Sobre ese diccionario realizar las consultas necesarias cuando se introduzca la entrada

# Cada desarrolladora podria tener distintos juegos con distintas categorias cada juego, por lo que si alguna se repite en distintos juegos,
# habria que contabilizar los votos en una misma variable. Por esto seria util tener cada categoria como una clave de un diccionario, para
# que no se repita.
# Aqui hay un ejemplo:
'''categoriesDF = dataDF.filter(dataDF.developer == "Valve").distinct()
count = categoriesDF.count()
categoriesList = categoriesDF.collect()
print(categoriesDF.show(22, False))
categoriesMap = dict()
for row in categoriesList:
    categories = row["categories"].split(";")
    rating = [int(row["positive_ratings"]), int(row["negative_ratings"])]
    for category in categories:
        if category in categoriesMap.keys():
            categoriesMap[category][0] += rating[0]
            categoriesMap[category][1] += rating[1]
        else:
            categoriesMap[category] = rating


for key, values in categoriesMap.items():
    print("Categoria: " + str(key) + ", Votos Positivos: " + str(values[0]) + ", Votos Negativos: " + str(values[1]))'''




# El rating de arriba es el perteneciente a un juego. Habria que sumar todos los votos positivos entre si, los negativos entre si
# de todos los juegos de una misma categoria y obtener un porcentaje que indique lo bueno que es








