# run > pip install -r requirements.txt

import pandas as pd
from matplotlib import pyplot as plt
import data_service
import dupont_model

def main():
    financial_data = data_service.financial()      # stores the values of the financial demonstrative by quarter
    ipca = data_service.ipca()                    # stores the values of the IPCA interest by month
    selic =data_service.selic()                   # stores the values of the SELIC insterest by month

    # adjust ipca and selic values to quarter
    adjusted_ipca = adjust_values_to_quarter(ipca).T
    adjusted_selic = adjust_values_to_quarter(selic).T

    # extract only the values from the dataframe
    ipca_to_list = adjusted_ipca.values
    selic_to_list = adjusted_selic.values

    ipca_serie = []
    selic_serie = []

    # transforms to a serie
    for i in range(0,len(ipca_to_list)):
        ipca_serie.extend(ipca_to_list[i])
        selic_serie.extend(selic_to_list[i])

    # make the calculations and saves in a file
    result = dupont_frame(financial_data, ipca_serie, selic_serie)   
    save_results(result)

    graph_plot(result)

# group values by quarter
def adjust_values_to_quarter(data):

    data_quarter = pd.DataFrame(columns=data.columns)   # create an empty DataFrame

    count = 1       # quarter count
    for i in range(0, len(data.index), 3):
        grouped_months = data[i:i+3].apply(quarters_interest)   # group months and apply make the adjust to quarter
        grouped_months.name = "%d_quarter"%count                # set the quartes name
        data_quarter = data_quarter.append(grouped_months)      # set a new DataFrame with the adjusted values
        count+=1

    return data_quarter

# converts the month interest in to quarters interest
def quarters_interest(column):
    return (column[0] + 1) * (column[1] + 1) * (column[2] + 1) - 1  # month to quarter conversion

# set a DataFrame for DuPont's Model results and stores into a csv file
def dupont_frame(data, ipca_data, selic_data):
    # set the empty DataFrame
    data_per_year = pd.DataFrame(columns=["ano", "trimestre", "margem liquida", "giro de ativos", "alavancagem", "roa", "roe", "ipca", "selic"])

    # iterates the DataFrame with the financial data per row
    for i in range (0, len(data.index)):
        data_serie = data.iloc[i]      # stores the i-row
        # calculates all DuPonts ratios
        profit_margin = dupont_model.calc_profit_margin(data_serie.iloc[2],data_serie.iloc[3])
        asset_turnover = dupont_model.calc_asset_turnover(data_serie.iloc[3],data_serie.iloc[4]) 
        leverage = dupont_model.calc_leverage(data_serie.iloc[4],data_serie.iloc[5])
        roa = dupont_model.calc_roa(profit_margin,asset_turnover)
        roe = dupont_model.calc_roe(roa,leverage)
        
        # stores the quarters serie in a temporary variable
        tmp = [data_serie.iloc[0],data_serie.iloc[1],profit_margin,asset_turnover,leverage,roa,roe,ipca_data[i],selic_data[i]]

        # insert each quarter in the end of the dataframe
        data_per_year = data_per_year.append(pd.Series(tmp, index=data_per_year.columns), ignore_index="True")

    return data_per_year

def save_results(data):
    # saves the results into a .csv file
    data.to_csv(r'./dupont_analisys_result.csv')

def graph_plot(data):
    # set the period of your database replacing the 'start' and 'end' parameters
    main_graph = pd.DataFrame(data, columns=['roa', 'roe', 'ipca', 'selic']).set_index(pd.date_range(start='1/1/2012', end='1/1/2019', freq="Q"))
    roa_roe_graph = pd.DataFrame(data, columns=['roa', 'roe']).set_index(pd.date_range(start='1/1/2012', end='1/1/2019', freq="Q"))
    roa_ipca_selic_graph = pd.DataFrame(data, columns=['roa', 'ipca', 'selic']).set_index(pd.date_range(start='1/1/2012', end='1/1/2019', freq="Q"))
    roe_ipca_selic_graph = pd.DataFrame(data, columns=['roe', 'ipca', 'selic']).set_index(pd.date_range(start='1/1/2012', end='1/1/2019', freq="Q"))

    main_graph.plot(grid=True)
    roa_roe_graph.plot(grid=True)
    roa_ipca_selic_graph.plot(grid=True)
    roe_ipca_selic_graph.plot(grid=True)

    plt.show()

main()




