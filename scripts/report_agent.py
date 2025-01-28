import os
import json
import glob
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from schemas import GovernanceBody # ADJUSTABLE
from tcagent import TCAgent
import time
from tqdm import tqdm
from pydantic import BaseModel

load_dotenv()

class ReportAgent:
    def __init__(self, model_name, company, schema: BaseModel):
        self.company = company
        self.model_name = model_name
        self.schema = schema
        self.llm = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        with open('scripts/prompts.yml', 'r', encoding='utf-8') as f:
            self.prompts = yaml.safe_load(f)

    def get_data(self):
        query = self.prompts['query'].strip().format(company=self.company, data_model=self.schema.model_json_schema())
        system_prompt = self.prompts['system'].strip()
        structured_prompt = self.prompts['structurize'].strip()
        
        agent = TCAgent(self.model_name, system_prompt, self.company)
        raw_response, sources = agent.invoke(query)
        
        sllm = self.llm.with_structured_output(self.schema)
        structured_response = sllm.invoke(
            structured_prompt.format(raw=raw_response, data_model=self.schema.model_json_schema()),
            config={"run_name": "Structurize Output"}
        )
        return {
            "data": structured_response.model_dump(),
            "sources": list(set(sources))
        }


# ADJUSTABLE: Pastikan variable files ada isinya.
json_dir = "data/JSON"
output_dir = "results"
files = glob.glob(os.path.join(json_dir, "*", "*.json"))

# Membuat direktori output jika belum ada
os.makedirs(output_dir, exist_ok=True)

for file in tqdm(files, desc="Processing Companies"):
    try:
        # Ekstrak nama perusahaan dari path file
        company_name = os.path.splitext(os.path.basename(file))[0]
        
        # Inisialisasi agent dan proses data
        agent = ReportAgent(os.environ["LLM"], company_name, GovernanceBody) # ADJUSTABLE
        result = agent.get_data()
        
        # Membuat path output dan memastikan direktori tersedia
        relative_path = os.path.relpath(file, json_dir)
        output_path = os.path.join(output_dir, relative_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Simpan hasil
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=4)
            
    except Exception as e:
        print(f"\nError processing {company_name}: {str(e)}")
    
    time.sleep(30) 
