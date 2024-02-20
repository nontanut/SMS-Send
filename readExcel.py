import pandas as pd

df = pd.read_excel (r'PA+ NCAP 19.02.24.xlsx')

data = df["MobilePhone"].apply(str)
print(','.join(data.values.tolist()))