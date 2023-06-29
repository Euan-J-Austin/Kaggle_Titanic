import pandas as pd

def glance(x):
    print(f"SHAPE:\n{x.shape}\n")
    print(f"DESCRIPTION:\n{x.describe()}\n")
    print(f"DESCRIPTION OF OBJECT DATA TYPES:\n{x.describe(include=['O'])}\n")
    print(f"DATATYPES:\n{x.dtypes.sort_values()}\n") #works in notebook
    print(f"NULL VALUES:\n{x.isnull().sum()}\n")