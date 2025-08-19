import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=True)
        return df
    except Exception as e:
        print("Error loading CSV:", e)
        return None
def preprocess_data(df, date_col=None):
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
    df = df.dropna()
    return df
