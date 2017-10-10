import pandas as pd


data = pd.read_csv('D:/o2o/table1.csv', header=0)
col = data.iloc[:,-2:]
#print(col[col['Date_received']>'20160601'])
print(col.oloc[1048272])