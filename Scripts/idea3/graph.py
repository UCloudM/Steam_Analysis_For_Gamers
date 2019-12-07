

# COMANDO DE PRUEBA:
# --------------------------------------------------------------------------
# python3 graph.py "rankingParaAction-Valve.csv" "Action"
# --------------------------------------------------------------------------


import pandas as pd
import matplotlib.pyplot as plt
import sys

csv = sys.argv[1]
genre = sys.argv[2]

datos = pd.read_csv(csv, nrows=10)
df = pd.DataFrame(datos)
aux1 = df.groupby(df.developer).sum().plot(kind='bar', legend = 'Reverse', color='black', figsize=(10, 10))

plt.xlabel("Developers")
plt.ylabel("Positives Votes")
plt.title("Genre: " + genre, fontsize=20)
plt.subplots_adjust(left=0.12, bottom=0.30, right=0.9, top=0.88, wspace=0.20, hspace=0.20)
name = csv.split(".")[0]
plt.savefig(name + ".png")
plt.show()