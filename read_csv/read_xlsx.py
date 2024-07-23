import pandas as pd

# Reading xlsx file
file = 'Cities_Probability(1).xlsx'           # Path of the file
df = pd.read_excel(file)

# Saving data into a separate file
with open ('Printed_Data.py',"w") as f:
    f.write(f"data={df.to_dict(orient='list')}")

# Central tendency
print("Mean of literacy: ", df['Literacy'].mean())
print("Median of literacy: ", df['Literacy'].median())
print("Mode of literacy: ", df['Literacy'].mode()[0])
