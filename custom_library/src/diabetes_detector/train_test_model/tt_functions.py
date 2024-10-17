import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

def apply_one_hot_encode(df:pd.DataFrame, column_to_encode:str) -> pd.DataFrame:
    encoder = OneHotEncoder(sparse_output=False)
    encoded_variable = encoder.fit_transform(df[[column_to_encode]])
    df_encoded = pd.DataFrame(encoded_variable, columns=encoder.get_feature_names_out([column_to_encode]))
    df_encoded = df_encoded.reset_index(drop=True)
    df = df.drop(columns=[column_to_encode])
    df = df.reset_index(drop=True)
    df_final = pd.concat([df, df_encoded], axis=1)
    return df_final

def split_dataset(df:pd.DataFrame):
    MESSI_SEED = 10
    target_col = "diabetes_mellitus"
    X = df[list(set(df.columns)-set(target_col))]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=MESSI_SEED)
    return X_train, X_test, y_train, y_test

def keep_only_important_features(df:pd.DataFrame)->pd.DataFrame:
    feature_columns = ["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", 
    "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]
    df = df[feature_columns]
    return df

def train_rfc(X_train, y_train):
    MESSI_SEED = 10
    clf = RandomForestClassifier(random_state=MESSI_SEED)
    clf.fit(X_train, y_train)
    return clf

def calculate_roc_auc_score(y_true, y_predicted):
    roc = roc_auc_score(y_true, y_predicted[:, 1])
    print(f'Train ROC AUC: {roc:.4f}')
