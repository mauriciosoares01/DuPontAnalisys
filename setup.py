import pandas as pd
import dataService

def main():
    financialData = dataService.financial()      #stores the values of the financial demonstrative by quarter
    ipca = dataService.ipca()
    selic =dataService.selic()   

    adusted_ipca = adjust_values_to_quarter(ipca)
    adusted_selic = adjust_values_to_quarter(selic)

    print(adusted_ipca)
    print(adusted_selic)

def adjust_values_to_quarter(data):

    data_quarter = pd.DataFrame(columns=data.columns)

    count = 1
    for i in range(0, len(data.index), 3):
        grouped_months = data[i:i+3].apply(quarters_interest)
        grouped_months.name = "%d_quarter"%count
        data_quarter = data_quarter.append(grouped_months)
        count+=1

    return data_quarter

def quarters_interest(column):
    return (column[0] + 1) * (column[1] + 1) * (column[2] + 1) - 1

main()



