# Data preprocessing utilities

import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(filepath='data/raw/synthetic_data.csv', test_size=0.2, random_state=42):
    df = pd.read_csv(filepath)
    X = df.drop('aprovado', axis=1)
    y = df['aprovado']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def preprocess_features(X):
    # Simple scaling if needed
    return X