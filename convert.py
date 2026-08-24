import pandas as pd

df = pd.read_excel('LFB_Incident_data_from_2024_onwards.xlsx', sheet_name='Sheet1')
df.to_csv("lfb.csv", index=False)
print("done, there are rows: ", len(df))
