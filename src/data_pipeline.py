import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    # Handle missing records as per Day 2
    df.dropna(inplace=True)
    # Normalize scores (0 to 1)
    df['normalized_score'] = df['quiz_score'] / 100
    return df