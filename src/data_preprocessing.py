import pandas as pd 
import os
RAW_DATA_PATH = "../data/raw/train_FD001.txt"
PROCESSED_DATA_PATH = "../data/processed/train_cleaned.csv"

def load_data(filepath) :
    return pd.read_csv(filepath, delimiter = ' ',skipinitialspace=True, header=None)

   

def clean_data(df) :
    df = df.dropna(axis=1, how='all')
    # changer les noms des colonnes  
    columns = ['Unit number','cycle', 'opst1', 'opst2','opst3'] + [f"sensor{i}" for i in range (1,22)]
    df.columns = columns

    # supprimer les colonnes qui n'ont pas de variations
    colonnes_asupp = ["opst3","sensor1", "sensor5", "sensor6","sensor10", "sensor16", "sensor19", "sensor18"]
    for element in colonnes_asupp :
        df = df.drop(columns=element, axis=1)
    return df


def save_data(df, filepath) : 
    """Sauvegarder les données nettoyées dans un fichier CSV """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    print(df)
    df.to_csv(filepath, index=False)

if __name__== "__main__"  : 
    print("chargement des données") 
    data = load_data(RAW_DATA_PATH)
    
    print("nettoyage des données")
    cleaned_data = clean_data(data)

    print("sauvegarder les données nettoyées") 
    save_data(cleaned_data,PROCESSED_DATA_PATH)    

