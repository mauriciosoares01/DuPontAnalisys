# coding=utf-8

import pandas as pd

# def header(msg):
#     print("-" * 50)
#     print("[" + msg + "]")
    
def financial():
    financialData = pd.read_csv("financialData.csv")
    return(financialData)

def ipca():
    ipca = pd.read_csv("ipca.csv", index_col ="Mês/Ano")
    return(ipca)

def selic():
    selic = pd.read_csv("selic.csv", index_col ="Mês/Ano")
    return(selic)



