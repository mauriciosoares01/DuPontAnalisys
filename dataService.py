import pandas as pd

def header(msg):
    print("-" * 50)
    print("[" + msg + "]")
    
def read():
    return pd.read_csv("financialData.csv")


header("Resultados financeiros")
print(read())