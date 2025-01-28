from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime

# ALL ADJUSTABLE

class GovernanceBody(BaseModel):
    directors: List[str] = Field(description="A comprehensive list of full names of all individuals serving as directors.")
    commissioners: List[str] = Field(description="A comprehensive list of full names of all individuals serving as commissioners.")

class EducationEntry(BaseModel):
    major: str = Field(
        description="The academic program or field of study pursued by the individual.",
        example="Business Administration"
    )
    university: str = Field(
        description="The name of the university where the individual pursued their education.",
        example="Harvard University"
    )
    country: str = Field(
        description="The country where the individual completed their education.",
        example="United States"
    )

class WorkingEntry(BaseModel):
    position: str = Field(
        description="The job title or role held during the work experience.",
        example="Chief Financial Officer"
    )
    year_start: str = Field(
        description="The starting year of the work experience. Use 'N/A' if the information is unavailable.",
        example="2015"
    )
    year_end: str = Field(
        description="The ending year of the work experience. Use 'N/A' if the information is unavailable.",
        example="2020"
    )
    country: str = Field(
        description="The country where the work experience took place.",
        example="Canada"
    )

class BoardProfile(BaseModel):
    name: str = Field(
        description="The full name of the individual (e.g., CEO, President Director, Managing Director).",
        example="Emily Davis"
    )
    current_position: str = Field(
        description="The title or role currently held by the individual.",
        example="Chief Executive Officer"
    )
    current_position_company_name: str = Field(
        description="The name of the organization where the individual holds their current position.",
        example="TechCorp Inc."
    )
    current_position_start_date: datetime | str = Field(
        description="The date when the individual started their current role. Use 'N/A' if the information is unavailable.",
        example="2021-06-01"
    )
    current_position_end_date: datetime | str = Field(
        description="The date when the individual ended their current role, if applicable. Use 'N/A' if the information is unavailable.",
        example="N/A"
    )
    current_position_tenure_months: str = Field(
        description="The total duration (in months) of the individual’s current role. Use 'N/A' if the information is unavailable.",
        example="18"
    )
    gender: Literal['Male', 'Female', 'N/A'] = Field(
        description="The gender of the individual (e.g., Male or Female).",
        example="Female"
    )
    age: int | str = Field(
        description="The age of the individual. Use 'N/A' if the information is unavailable.",
        example=43
    )
    nationality: str = Field(
        description="The nationality of the individual. Use 'N/A' if the information is unavailable.",
        example="Canadian"
    )
    education_bachelor: List[EducationEntry] = Field(
        description="A list of bachelor's degree education entries pursued by the individual.",
        example=[{
            "major": "Economics",
            "university": "University of Oxford",
            "country": "United Kingdom"
        }]
    )
    education_master: List[EducationEntry] = Field(
        description="A list of master's degree education entries pursued by the individual.",
        example=[{
            "major": "Business Administration",
            "university": "Stanford University",
            "country": "United States"
        }]
    )
    education_doctoral: List[EducationEntry] = Field(
        description="A list of doctoral degree education entries pursued by the individual.",
        example=[{
            "major": "Physics",
            "university": "MIT",
            "country": "United States"
        }]
    )
    working_experiences: List[WorkingEntry] = Field(
        description="A list of the individual's working experiences.",
        example=[{
            "position": "Software Engineer",
            "year_start": "2010",
            "year_end": "2015",
            "country": "United States"
        }, {
            "position": "CTO",
            "year_start": "2016",
            "year_end": "N/A",
            "country": "Germany"
        }]
    )