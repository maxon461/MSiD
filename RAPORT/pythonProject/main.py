import os.path
import subprocess
import pandas as pd
import zipfile

# Dataset name from Kaggle
dataset_name = "oles04/top-leagues-player"

# Download dataset from Kaggle
subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name])

# Directory to extract the dataset
ls = "/Users/maxon462/Desktop/PWR/Metody systemowe i decyzyjne/RAPORT/pythonProject"

# Check if the ZIP file exists before extracting
zip_file = os.path.join(ls, 'top-leagues-player.zip')
if os.path.exists(zip_file):
    # Extract the ZIP file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(ls)

    # Load the CSV file into a DataFrame
    csv_file = "/Users/maxon462/Desktop/PWR/Metody systemowe i decyzyjne/RAPORT/pythonProject/top5_leagues_player.csv"
    df = pd.read_csv(csv_file)
    print("Dataset loaded successfully.")
else:
    print("ZIP file not found.")

