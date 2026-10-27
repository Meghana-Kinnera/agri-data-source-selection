import pandas as pd

def load_data(filepath):
    """
    Load agricultural data from CSV file
    """
    return pd.read_csv(filepath)

def normalize_data(data):
    """
    Apply Min-Max normalization to numerical columns
    """

    numeric_columns = data.select_dtypes(include='number').columns

    for col in numeric_columns:
        min_val = data[col].min()
        max_val = data[col].max()
        data[col] = (data[col] - min_val) / (max_val - min_val)

    return data