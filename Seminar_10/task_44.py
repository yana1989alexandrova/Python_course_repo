import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def df2one_hot(df):
    dict = {}
    for column in df.columns:
        unique_values = df[column].unique()
        for value in unique_values:
            dict[value] = (df[column] == value).astype(bool)
    return pd.DataFrame(dict)

df_result = df2one_hot(data)
print(df_result.head())