import pandas as pd
import os
from google.colab import drive

def get_connection():
    if not os.path.exists('/content/drive'):
        drive.mount('/content/drive')
    
    base_path ='/content/drive/My Drive/datasci_dataset/'
    return base_path

def load_data(version='v1'):
    base = get_connection()
    file_map = {
        'v1': 'data_raw.csv',
    }
    
    path = os.path.join(base, file_map[version])
    print(f"Loading {file_map[version]}...")
    return pd.read_csv(path)
