# coding=utf-8

# this file colect all the needed data to applys Dupont model
# use  the same pattern in the csv structure to works porperly with your data

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

def pib():
    selic = pd.read_csv("pib.csv", index_col="data")
    return(selic)



