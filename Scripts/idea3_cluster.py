

# COMANDO DE PRUEBA:
# --------------------------------------------------------------------------
# spark-submit idea3_cluster.py "Valve" "Action"
# --------------------------------------------------------------------------


from pyspark import SparkConf, SparkContext, SQLContext
import operator
import csv
import sys
import time

starting_point = time.time()


# Local
conf = SparkConf().setAppName('Script')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# ENTRADA
# ----------------------------------
dev = sys.argv[1]
genre = sys.argv[2]


# LEEMOS EL DATASET EN FORMATO CSV
# ----------------------------------
pathSteam = "steam.csv"

steamDF = sqlContext.read.option("header", "true").csv(pathSteam)

# PREPARAMOS LAS VARIABLES QUE VAMOS A UTILIZAR
# -----------------------------------------------
dataDF = steamDF.select("developer", "genres", "positive_ratings", "negative_ratings")

# Lista de desarrolladoras
developerList = steamDF.select("developer").distinct().collect()


# ALGORITMO
# ------------------------------------------------

# Tiene la forma: ranking( Desarrolladora, Votos del genero escogido)
ranking = dict()

for row in developerList:
    rating = 0

    # Seleccionamos los datos de la desarrolladora que estamos procesando
    developerInfoDF = dataDF.filter(dataDF.developer == row["developer"]).distinct()
    developerInfoList = developerInfoDF.collect()

    # Hacemos un split de cada elemento de la lista de los generos de cada desarrolladora y comprobamos si esta el que buscamos.

    for game in developerInfoList:
        genres = game["genres"].split(";")

        if genre in genres:
            rating += (int(game["positive_ratings"]) - int(game["negative_ratings"]))

    if rating != 0:
        ranking[row["developer"]] = rating


ranking_sorted = sorted(ranking.items(), key=operator.itemgetter(1), reverse=True)

with open("rankingPara" + str(genre) + ".csv", 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["developer", "votes"])
    for i in ranking_sorted:
        wr.writerow(i)

recommendedDevelopers = ranking_sorted[0:3]

print("Las mejores son: ")
print(recommendedDevelopers)

if (any(dev in tuple for tuple in recommendedDevelopers)) :
    print("Por tanto, te recomendamos la desarrolladora que has elegido.")
else :
    print("Por tanto, no la recomendamos en absoluto.")



# CALCULO DEL TIEMPO DE EJECUCION
# ------------------------------------------------
elapsed_time = time.time() - starting_point
elapsed_time_int = int(elapsed_time)

elapsed_time_minutes = elapsed_time_int / 60
elapsed_time_seconds = elapsed_time_int % 60

print("Tiempo final: " + str(elapsed_time_minutes) + " minutos y " + str(elapsed_time_seconds) + " segundos transcurridos.")