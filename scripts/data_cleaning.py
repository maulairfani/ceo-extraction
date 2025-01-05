import json
import pandas as pd
import glob
import os

files = glob.glob("results/json/*.json")
files = [os.path.normpath(file) for file in files]

work_data = []
edu_data = []

for file in files:
    with open(file) as f:
        data = json.load(f)

    for d in data:
        general_data = {
            "name": d["name"], 
            "company": d["company"], 
            "current_position": d['working_experience']["current_position"]
        }
        work_general = {
            "current_position_company_name": d['working_experience']["current_position_company_name"], 
            "current_position_start_month": d['working_experience']["current_position_start_month"], 
            "current_position_start_year": d['working_experience']["current_position_start_year"], 
            "current_position_tenure_months": d['working_experience']["current_position_tenure_months"], 
        }
        work_num = len(d['working_experience']['working_experience_details'])

        for i in range(work_num):
            work_data.append({
                **general_data,
                **work_general,
                **d['working_experience']['working_experience_details'][i]
            })

        edu_num = len(d['education_background']['education_background'])
        for i in range(edu_num):
            edu_data.append({
                **general_data,
                **d['education_background']['education_background'][i]
            })

# Simpan data ke Excel
work_data = pd.DataFrame(work_data)
edu_data = pd.DataFrame(edu_data)

work_data.to_excel("results/xlsx/working_experience.xlsx", index=False)
edu_data.to_excel("results/xlsx/education_background.xlsx", index=False)