import os 
from os import listdir
from os.path import isfile, join
import pandas as pd 

df = pd.read_csv('players.csv') 


df.fillna('', inplace=True)

print(df)