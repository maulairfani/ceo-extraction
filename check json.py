import json
import glob
import os

def check_json_validity(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False

# Cek validitas file JSON
json_dir = "data/JSON/TESTING SEGOPS"
files = glob.glob(os.path.join(json_dir, "*", "*.json"))
valid_files = [f for f in files if check_json_validity(f)]
print(f"Valid files: {valid_files}")
