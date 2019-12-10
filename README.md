------------------------------------------------------------

<p align="center"><img src="https://github.com/UCloudM/Steam_Analysis_For_Gamers/blob/master/steam.jpg"></p>
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
│   │   ├── idea1_local.py: Fichero que realiza las recomendaciones en modo local. Este permite aprovecharse de los núcleos de tu 	│   │   │	ordenador además de tener la ruta del dataset enlazada a su carpeta. 
│   │   ├── idea1_cluster.py: Fichero que realiza las recomendaciones en un cluster. Está preparado para poder acceder al dataset una   │   │  	│	vez esté ubicado en el sistema de ficheros de Hadoop.   
│   │   ├── rankingPara_.csv: Ficheros con los resultados generados por los scripts.
│   │   ├── graph.py: Fichero que permite crear las gráficas con los archivos CSV que generan los scripts mencionados anteriormente.
│   │	├── pruebas.txt: Contiene posibles desarrolladoras y géneros que podríamos meter como entrada
│   │   ├── Capturas: Contiene algunos ejemplos de salida en capturas que se han hecho durante el desarrollo.
│   │   ├── Gráficas: Imagenes generadas por el archivo graph.py
│   │
│   ├── idea2.py: Fichero que realiza el tratamiento de los datasets que se utilizan en dicha idea.
└── 
```


# Datasets

* [Steam Store Games](https://www.kaggle.com/nikdavis/steam-store-games)

* [Intel Processors](https://www.kaggle.com/iliassekkaf/computerparts/)

* [AMD Processors](http://cpudb.stanford.edu/manufacturers/1)
	


