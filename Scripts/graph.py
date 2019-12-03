import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

datos = pd.read_csv('../datasets/steam.csv')
df = pd.DataFrame(datos)
aux1 = df[(df.genres =='Action')].groupby('developer')['positive_ratings'].sum().plot(kind='bar')
plt.show()