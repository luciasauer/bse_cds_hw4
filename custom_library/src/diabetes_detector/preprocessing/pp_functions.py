import pandas as pd

def make_binary_gender(df:pd.DataFrame)-> pd.DataFrame:
    df['is_male'] = df['gender'].apply(lambda x: 1 if x == 'M' else 0)
    df = df.drop(columns='gender')
    return df

def fill_na_with_mean(df:pd.DataFrame, column_to_fill:str)-> pd.DataFrame:
    df.fillna({column_to_fill: df[column_to_fill].mean()}, inplace=True)
    return df

def drop_missing_values_in_subset(df:pd.DataFrame, columns_subset:list)-> pd.DataFrame:
    return df.dropna(subset=columns_subset)
