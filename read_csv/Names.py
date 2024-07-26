import pandas as pd

file_name = './Data-for-Certificate.xlsx'

def Names(file_name):
    # Read the Excel file
    data = pd.read_excel(file_name)
    cols = list(data.columns)
    d = data.to_dict()


    names = [d[cols[1]][i] for i in d[cols[1]]]
    # print(names)
    return names

print(Names(file_name))