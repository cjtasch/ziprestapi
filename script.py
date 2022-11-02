from audioop import cross
import pandas as pd
import sqlite3

con = sqlite3.connect('crosswalk.db')


def loadData():
    crosswalk = pd.read_excel('ZIPCodetoZCTACrosswalk2021UDS.xlsx', usecols=['ZIP_CODE','PO_NAME','STATE'], dtype={'ZIP_CODE':object,'PO_NAME':object,'STATE':object})
    crosswalk.to_sql('zip',con, if_exists='replace', index=False)

df = pd.read_sql('SELECT * FROM zip', con)
print(df)