import sqlite3
import pandas as pd

conn = sqlite3.connect("db.sqlite3")
df = pd.read_csv("loaddata\data.csv")
df['id'] = df.index
df = df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]

df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)
