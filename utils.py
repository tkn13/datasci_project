import pandas as pd
import os
from google.colab import drive

def get_connection():
    if not os.path.exists('/content/drive'):
        drive.mount('/content/drive')
    
    base_path ='/content/drive/My Drive/datamine_shared/'
    return base_path

def load_data(version='v1'):
    base = get_connection()
    file_map = {
        'raw': 'data_raw.csv',
        'v1': 'data_clean_v1.csv',
    }
    
    path = os.path.join(base, file_map[version])
    print(f"Loading {file_map[version]}...")
    return pd.read_csv(path)

def save_data(df, filename):
    base = get_connection()
    path = os.path.join(base, filename)
    df.to_csv(path, index=False)
    print(f"Data saved to {filename}")
