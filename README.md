------------------------------------------------------------

<p align="center">
  <img src="https://github.com/UCloudM/Steam_Analysis_For_Gamers/blob/master/steam.jpg">
</p>
<h1 align="center"> Analysis for Gamers </h1>

------------------------------------------------------------

__Steam Analysis for Gamers__ es un proyecto con el cual hemos realizado un procesamiento por bloques (Batch Data Processing) y su posterior análisis con datos recolectados de la plataforma de videojuegos Steam. 

El proyecto consta de dos ideas principales: 

* La __primera idea__ está basada en la recomendación de una desarrolladora de videojuegos para un género en concreto, en base a las votaciones obtenidas en juegos lanzados anteriormente por la misma desarrolladora que pertenecen a ese mismo género.

* __La segunda idea__ se podría dividir en dos:
	* ¿Qué juegos podríamos ejecutar en nuestro ordenador en función del procesador que tenemos?
	* ¿Qué procesador deberíamos comprar si queremos jugar a determinados juegos?
	
	
Los scripts que se han desarrollado se pueden ver en su correspondiente carpeta y son los siguientes:

```bash
├── Scripts
│   ├── idea1
│   │   ├── idea1_local.py: Fichero que realiza las recomendaciones en modo local. Este permite aprovecharse de los núcleos de tu ordenador además de tener la ruta del dataset enlazada a su carpeta. 
│   │   ├── idea1_cluster.py: Fichero que realiza las recomendaciones en un cluster. Está preparado para poder acceder al dataset una vez esté ubicado en el sistema de ficheros de Hadoop.   
│   │   ├── rankingPara_.csv: Ficheros con los resultados generados por los scripts.
│   │   ├── graph.py: Fichero que permite crear las gráficas con los archivos CSV que generan los scripts mencionados anteriormente.
│   │	├── pruebas.txt: Contiene posibles desarrolladoras y géneros que podríamos meter como entrada
│   │   ├── Capturas: Contiene algunos ejemplos de salida en capturas que se han hecho durante el desarrollo.
│   │   ├── Gráficas: Imagenes generadas por el archivo graph.py
│   │
│   ├── idea2.py: Fichero que realiza el tratamiento de los datasets que se utilizan en dicha idea.
└── 
```

# Requisitos

* Sistema Operativo Linux
* Python 3 
* Apache Spark

# Instalación en Ubuntu

## Python
```bash
$ sudo apt-get install python3
```

## Spark
```bash
$ sudo curl -O http://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz
$ sudo tar xvf ./spark-2.2.0-bin-hadoop2.7.tgz
$ sudo mkdir /usr/local/spark
$ sudo cp -r spark-2.2.0-bin-hadoop2.7/* /usr/local/spark
```

## Configura el entorno 
Añade la siguiente línea al archivo .source:
```bash
$ export PATH="$PATH:/usr/local/spark/bin"
```

# Ejecución

## Idea 1
En el caso de querer ejecutar esta idea en local, se debe ejecutar un comando como el siguiente:
```bash
$ spark-submit idea1_local.py "Nombre desarrolladora" "Genero"
```

En el caso de querer ejecutarlo en un cluster, se debería ejecutar lo siguiente:
```bash
$ spark-submit --num-executors N --executor-cores M idea1_cluster.py "Nombre desarrolladora" "Genero"
```
Siendo "Nombre desarrolladora" y "Genero" datos escogidos del fichero pruebas.txt. Las variables N y M dependen del cluster lanzado.

Estos dos scripts, generarán una salida en la terminal de Apache Spark y otra en un fichero con formato CSV con los resultados obtenidos.

En cuanto al script de las gráficas, valdría con poner un comando en la terminal como el siguiente:
```bash
$  python3 graph.py "rankingPara_.csv" "Genero"
``` 
Siendo "rankingPara_.csv" los resultados que acabamos de generar.

## Idea 2
Esta idea no se ha podido llevar a cabo en su completitud por la complejidad en el tratamiento de los datos. A pesar de esto, este tratamiento se realiza correctamente y es completamente funcional. Se puede comprobar con el siguiente comando:

```bash
$ spark-submit idea2.py
```

# Datasets

* [Steam Store Games](https://www.kaggle.com/nikdavis/steam-store-games)

* [Intel Processors](https://www.kaggle.com/iliassekkaf/computerparts/)

* [AMD Processors](http://cpudb.stanford.edu/manufacturers/1)

# Miembros
* Adrián Ogáyar Sánchez
* Arturo Barbero Pérez
* Jesús Verdúguez Gervaso
* Pedro Martínez Gamero
	


