from typing import Annotated
from pydantic import BaseModel, StringConstraints, field_validator

class ScenarioRequest(BaseModel):
    requirement: Annotated[str, StringConstraints(min_length=1)]

    @field_validator("requirement")
    @classmethod
    def validate_requirement(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Requirement must not be empty")
        return v

class CaseRequest(BaseModel):
    scenario: Annotated[str, StringConstraints(min_length=1)]

    @field_validator("scenario")
    @classmethod
    def validate_scenario(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Scenario must not be empty")
        return v