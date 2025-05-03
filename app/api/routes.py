from pydantic import BaseModel
from fastapi import APIRouter, Depends
from app.interfaces.llm_provider import LLMProvider
from app.services.gemini_service import GeminiService

router = APIRouter()

class ScenarioRequest(BaseModel):
    requirement: str

class CaseRequest(BaseModel):
    scenario: str

generator = GeminiService()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/generate-scenarios")
async def gen_scenarios(req: ScenarioRequest, gen: LLMProvider = Depends(lambda: generator)):
    return await gen.generate_scenarios(req.requirement)

@router.post("/generate-test-cases")
async def gen_test_cases(req: CaseRequest, gen: LLMProvider = Depends(lambda: generator)):
    return await gen.generate_test_cases(req.scenario) 