from pydantic import BaseModel, Field
from typing import List, Literal

# Define the structure for each working experience entry
class WorkingExperienceEntry(BaseModel):
    workexp_position: str = Field(description="The job title or role held by the individual.")
    workexp_company_name: str = Field(description="The name of the company where the position was held.")
    workexp_start_month: Literal[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December", "N/A"
    ] = Field(description="The month the position started. Use 'N/A' if unknown.")
    workexp_start_year: str = Field(description="The year the position started. Use 'N/A' if unknown.")
    workexp_end_month: Literal[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December", "N/A"
    ] = Field(description="The month the position ended. Use 'N/A' if unknown or ongoing.")
    workexp_end_year: str = Field(description="The year the position ended. Use 'N/A' if unknown or ongoing.")
    workexp_tenure_months: str = Field(description="The total duration of the position in months. Use 'N/A' if unknown.")

# Define the structure for each education entry
class EducationEntry(BaseModel):
    edu_major: str = Field(description="The major or field of study.")
    edu_grade: str = Field(description="The academic degree or grade (e.g., BACHELOR, MASTER).")
    edu_university: str = Field(description="The name of the university or institution attended.")
    edu_country: str = Field(description="The country where the university is located.")
    edu_start_month: Literal[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December", "N/A"
    ] = Field(description="The month the education started. Use 'N/A' if unknown.")
    edu_start_year: str = Field(description="The year the education started. Use 'N/A' if unknown.")
    edu_end_month: Literal[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December", "N/A"
    ] = Field(description="The month the education ended. Use 'N/A' if unknown or ongoing.")
    edu_end_year: str = Field(description="The year the education ended. Use 'N/A' if unknown or ongoing.")
    edu_tenure_months: str = Field(description="The total duration of the education in months. Use 'N/A' if unknown.")

# Main models for overall records
class GovernanceBody(BaseModel):
    directors: List[str] = Field(description="List of full names of all directors.")
    commissioners: List[str] = Field(description="List of full names of all commissioners.")

class WorkingExperience(BaseModel):
    name: str = Field(description="Full name of the director/commissioner.")
    current_position: str = Field(description="The current role/title held by the individual.")
    current_position_company_name: str = Field(description="Company where the individual currently holds a position.")
    current_position_start_month: Literal[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December", "N/A"
    ] = Field(description="The month the current position started. Use 'N/A' if unknown.")
    current_position_start_year: str = Field(description="The year the current position started. Use 'N/A' if unknown.")
    current_position_tenure_months: str = Field(description="The duration of the current position in months. Use 'N/A' if unknown.")
    working_experience_details: List[WorkingExperienceEntry] = Field(
        description="List of working experience records, each represented by a structured dictionary."
    )

class EducationBackground(BaseModel):
    name: str = Field(description="Full name of the director/commissioner.")
    current_position: str = Field(description="The current role/title held by the individual.")
    education_background: List[EducationEntry] = Field(
        description="List of educational records, each represented by a structured dictionary."
    )
