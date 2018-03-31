import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import statistics as st

# Reading in the data:
os.chdir('/home/trevor/Documents/GitHub/cs290AK/titanic')
ledger = pd.read_csv('ledger.csv')

# Check the dimensions of the data and the types of data:
# print(ledger.shape)
# print(ledger.dtypes)

# Look at the first 5 rows:
# print(ledger.head(5))

# Have a look at the descriptive data:
# print(ledger.describe())

# View categorical data:
# categorical = ledger.dtypes[ledger.dtypes == "object"].index
# print(ledger[categorical].describe())

# ===================================================
# VARIABLE DESCRIPTIONS:
# survival        Survival
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare
# cabin           Cabin
# embarked        Port of Embarkation
#                 (C = Cherbourg; Q = Queenstown; S = Southampton)
# =====================================================

# Decide if variables are needed and remove those which aren't:
# =============================================================

# Passenger ID is arbitrary -- remove it:
del ledger["PassengerId"]

# Our analysis concludes ticket numbers are not useful:
# print(ledger["Ticket"][0:15])
# print(ledger["Ticket"].describe())
del ledger["Ticket"]

# Are cabin numbers useful? Maybe.

# print(ledger["Cabin"][0:15])
# print(ledger["Cabin"].describe())
# print(ledger["Cabin"].unique())

# char_cabin = ledger["Cabin"].astype(str)
# new_Cabin = np.array([cabin[0] for cabin in char_cabin])
# new_Cabin = pd.Categorical(new_Cabin)
# print(new_Cabin.describe())


# "Pclass" is numeric... that doesn't make sense. Let's fix it...
#
# new_Pclass = pd.Categorical(ledger["Pclass"])
# new_Pclass = new_Pclass.rename_categories(["Class1","Class2","Class3"])
# print(new_Pclass.describe())

# Looking for null values:
#
# dummy_vector = pd.Series([1,None,3,None,7,8])
# print(dummy_vector.isnull())

# print(ledger["Age"])
# print(ledger["Age"].describe())
# missing = np.where(ledger["Age"].isnull() == True)
# print(missing)
# print(len(missing[0]))


# Binary numbers for survived / died changed to categories:
#
# new_survived = pd.Categorical(ledger["Survived"])
# new_survived = new_survived.rename_categories(["Died","Survived"])

# print(new_survived.describe())

# Now, let's have a look at the age distribution...

ledger.hist(column='Age',
        figsize=(9,6),
        bins=20)

plt.show() # don't forget this... (oops)
