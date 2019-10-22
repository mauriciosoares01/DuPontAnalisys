import pandas as pd
import data_service
import dupont_model

def main():
    financial_data = data_service.financial()      # stores the values of the financial demonstrative by quarter
    ipca = data_service.ipca()                    # stores the values of the IPCA interest by month
    selic =data_service.selic()                   # stores the values of the SELIC insterest by month

    # adjust ipca and selic values to quarter
    adjusted_ipca = adjust_values_to_quarter(ipca)
    adjusted_selic = adjust_values_to_quarter(selic)

    dupont_frame(financial_data)
    # print(adjusted_ipca)
    # print(adjusted_selic)

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

# set a DataFrame for DuPont's Model results
def dupont_frame(data):
    # set the empty DataFrame
    data_per_year = pd.DataFrame(columns=["ano", "trimestre", "margem liquida", "giro de ativos", "alavancagem", "roa", "roe"])

    for i in range (0, len(data.index)):
        pass

main()



