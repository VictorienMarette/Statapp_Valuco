import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ValueCo data extract - ENSAE research project.csv')
df_filtré = df[df['score_kind'] == 'E']
print(df.head())
plt.plot(df_filtré['period'], df_filtré['consensus'], marker='o')
plt.title('Titre du graphique')
plt.xlabel('Nom de la colonne Abscisse')
plt.ylabel('Nom de la colonne Ordonnée')
plt.show()

