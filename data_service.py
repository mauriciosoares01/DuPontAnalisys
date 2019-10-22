# coding=utf-8

import pandas as pd

def financial():
    financial_data = pd.read_csv("financial_data.csv")
    return(financial_data)

def ipca():
    ipca = pd.read_csv("ipca.csv", index_col ="Mês/Ano")
    return(ipca)

def selic():
    selic = pd.read_csv("selic.csv", index_col ="Mês/Ano")
    return(selic)


