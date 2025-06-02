import pandas as pd

df = pd.read_csv("Mall_Customers.csv")

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()


df = df.dropna()


df = df.drop_duplicates()

df['Gender'] = df['Gender'].str.lower()

df['Gender'] = df['Gender'].replace({'male': 'Male', 'female': 'Female'})

df.columns = df.columns.str.lower().str.replace(" ", "_")

df.to_csv("Mall_Customers_Cleaned.csv", index=False)
