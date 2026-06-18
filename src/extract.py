
import pandas as pd

def extract_data(file_path):
    """
    Reads the loan data and returns a pandas DataFrame.
    """

    df = pd.read_csv(file_path)
    print(f"Data loaded successfully: {df.shape}")
    return df

