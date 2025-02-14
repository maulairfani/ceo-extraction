import os
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from scripts.tcagent import TCAgent
from pydantic import BaseModel

load_dotenv()

class ReportAgent:
    def __init__(self, model_name, schema: BaseModel, query_prompt: str):
        self.model_name = model_name
        self.schema = schema
        self.query_prompt = query_prompt
        self.llm = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        with open('scripts/prompts.yml', 'r', encoding='utf-8') as f:
            self.prompts = yaml.safe_load(f)

    def get_data(self, prompt_data: dict):
        query = self.query_prompt.strip().format(**prompt_data)
        system_prompt = self.prompts['system'].strip()
        structured_prompt = self.prompts['structurize'].strip()
        
        agent = TCAgent(self.model_name, system_prompt, prompt_data['company'])
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