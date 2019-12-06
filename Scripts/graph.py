import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

datos = pd.read_csv('rankingParaAction.csv', nrows=10)
df = pd.DataFrame(datos)
aux1 = df.groupby(df.developer).sum().plot(kind='bar', legend = 'Reverse', color='black')
plt.xlabel("Developers")
plt.ylabel("Positives Votes")
plt.title("Categoria: "+sys.argv[1])
plt.show()