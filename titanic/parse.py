import numpy as np
import pandas as pd
import os

os.chdir('/home/slugzzz/Desktop/titanic')

ledger = pd.read_csv('ledger.csv')

categorical = ledger.dtypes[ledger.dtypes == "object"].index
print(ledger[categorical].describe())




# print(ledger)
# print(ledger.shape) 
# print(ledger.dtypes)
# print(ledger.head(5))
# print(ledger.describe())

