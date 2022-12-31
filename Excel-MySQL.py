from pickle import APPENDS
from sqlalchemy import create_engine
import pandas as pd

db ="sistema"
table = "DataPrueba"
path = "C:\Users\DONALD\Desktop\DataPrueba.xlxs"

url="mysql+mysqlconnector://root:@localhost"

engine = create_engine(url + db, echo=False)

df=pd.read_excel(path)

print("Read ok")

df.to_sql(name=table, con =engine, if_exists= 'append', index=False )




