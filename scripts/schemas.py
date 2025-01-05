from pydantic import BaseModel, Field
from typing import List

class GovernanceBody(BaseModel):
    directors: List[str] = Field(description="List of directors' full names.")
    commissioners: List[str] = Field(description="List of commissioners' full names.")

class WorkingExperience(BaseModel):
    name: str = Field(description="Full name of the director/commissioner.")
    current_position: str = Field(description="The current position/title held by the individual.")
    current_position_company_name: str = Field(description="The name of the company where the individual holds their current position.")
    current_position_tenure_in_months: int = Field(description="The duration (in months) the individual has held the current position, calculated up to December 2022.")
    working_experience_positions: List[str] = Field(description="A list of past positions held by the individual, separated by ';'. Ensure the count matches the company name and tenure lists.")
    working_experience_company_name: List[str] = Field(description="A list of companies corresponding to the past positions, separated by ';'. Ensure the count matches the positions and tenure lists.")
    working_experience_tenure_in_months: List[str] = Field(description="A list of durations (in months) for each past position, separated by ';'. If the duration is unknown, use 'N/A'. Ensure the count matches the positions and company lists.")
    number_of_working_experience: int = Field(description="The total number of distinct working experiences listed.")

class EducationBackground(BaseModel):
    name: str = Field(description="Full name of the director/commissioner.")
    current_position: str = Field(description="The current position/title held by the individual.")
    education_major: List[str] = Field(description="A list of majors or fields of study, separated by ';'. Ensure the count matches other education-related lists.")
    education_grade: List[str] = Field(description="A list of academic degrees or grades (e.g., BACHELOR, MASTER), separated by ';'. Ensure the count matches other education-related lists.")
    education_university: List[str] = Field(description="A list of universities attended, separated by ';'. Ensure the count matches other education-related lists.")
    education_country: List[str] = Field(description="A list of countries corresponding to the universities, separated by ';'. Ensure the count matches other education-related lists.")
    education_graduate_year: List[str] = Field(description="A list of graduation years for each degree. If the year is unknown, use 'N/A'. Ensure the count matches other education-related lists.")
