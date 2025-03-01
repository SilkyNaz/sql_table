#Nazier Reina
#Period D

import sqlite3
import pandas as pd

conn = sqlite3.connect('Rivals.sqlite')

cursor = conn.cursor()

#Pandas table for heroes

df = pd.read_csv("C:/Users/nazad/Downloads/Heros.csv")
df.to_sql( 'heroes', conn, if_exists='append', index=False)

#pandas table for abilities

df2 = pd.read_csv("C:/Users/nazad/Downloads/Abilities.csv")
df2.to_sql( 'abilities', conn, if_exists='append', index=False)

conn.commit()
conn.close()