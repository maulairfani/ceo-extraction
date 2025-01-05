import os
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
from schemas2 import GovernanceBody, WorkingExperience, EducationBackground
from tc_agent import TCAgent
import yaml
import json
import glob
from dotenv import load_dotenv
load_dotenv()

class ReportAgent:
    def __init__(self, model_name, company):
        self.company = company
        self.model_name = model_name
        self.llm = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        self.prompts = self._load_prompts()

    def get_governance_body(self):
        system_prompt = self.prompts['govern_system'].strip()
        structured_prompt = self.prompts['govern_structured'].strip()
        query = self.prompts['govern_query'].strip().format(company=self.company)

        sllm = self.llm.with_structured_output(GovernanceBody)
        agent = TCAgent(self.model_name, system_prompt, self.company)

        raw_response = agent.invoke(query)
        structured_response = sllm.invoke(structured_prompt.format(text=raw_response), config={"run_name": "Structurize Output"})
        return structured_response
    
    def get_working_experience(self, name):
        system_prompt = self.prompts['working_system'].strip()
        structured_prompt = self.prompts['working_structured'].strip()
        query = self.prompts['working_query'].strip().format(name=name)

        sllm = self.llm.with_structured_output(WorkingExperience)
        agent = TCAgent(self.model_name, system_prompt, self.company)

        raw_response = agent.invoke(query)
        structured_response = sllm.invoke(structured_prompt.format(text=raw_response), config={"run_name": "Structurize Output"})
        return structured_response
    
    def get_education_background(self, name):
        system_prompt = self.prompts['edu_system'].strip()
        structured_prompt = self.prompts['edu_structured'].strip()
        query = self.prompts['edu_query'].strip().format(name=name)

        sllm = self.llm.with_structured_output(EducationBackground)
        agent = TCAgent(self.model_name, system_prompt, self.company)

        raw_response = agent.invoke(query)
        structured_response = sllm.invoke(structured_prompt.format(text=raw_response), config={"run_name": "Structurize Output"})
        return structured_response

    def _load_prompts(self):
        with open('scripts/prompts2.yml', 'r', encoding='utf-8') as f:
            prompts = yaml.safe_load(f)
        return prompts

company_list = glob.glob("data/AR_JSON/*.json")
company_list = [os.path.basename(company).replace(".json", "") for company in company_list]

for company in company_list:
    with get_openai_callback() as cb:
        agent = ReportAgent("gpt-4o", company)
        govern = agent.get_governance_body()

        directors = govern.directors
        commissioners = govern.commissioners

        data = []
        for name in directors+commissioners:
            working_experience = agent.get_working_experience(name)
            education_background = agent.get_education_background(name)

            data.append({
                "company": company,
                "name": name,
                "working_experience": working_experience.dict(),
                "education_background": education_background.dict()
            })

            with open(f"results/json/{company}.json", 'w') as f:
                json.dump(data, f, indent=4)

    print(cb)