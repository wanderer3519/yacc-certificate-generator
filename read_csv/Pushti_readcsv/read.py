import pandas as pd

df = pd.read_excel('Cities_Probability(1).xlsx')    #name of the file
print(df)
mp = df['Literacy']
print("mean of literacy: ",mp.mean())
print("median of literacy: ",mp.median())
print("mode of literacy: ",mp.mode()[0])


