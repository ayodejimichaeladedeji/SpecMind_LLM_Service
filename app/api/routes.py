from fastapi import APIRouter, Depends
from app.schemas.responses import APIResponse
from app.interfaces.llm_provider import LLMProvider
from app.services.gemini_service import GeminiService
from app.schemas.requests import CaseRequest, ScenarioRequest

router = APIRouter()

generator = GeminiService()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/generate-scenarios")
async def gen_scenarios(req: ScenarioRequest, gen: LLMProvider = Depends(lambda: generator)): 
    try:
        result = await gen.generate_scenarios(req.requirement)
        return APIResponse(
            isSuccess=True,
            body=result,
            message="Test scenarios generated successfully"
        )
    except Exception as e:
        return APIResponse(
            isSuccess=False,
            errorMessage=str(e),
            message="Failed to generate test scenarios"
        )

@router.post("/generate-test-cases")
async def gen_test_cases(req: CaseRequest, gen: LLMProvider = Depends(lambda: generator)):
    try:
        result = await gen.generate_test_cases(req.scenario)
        return APIResponse(
            isSuccess=True,
            body=result,
            message="Test cases generated successfully"
        )
    except Exception as e:
        return APIResponse(
            isSuccess=False,
            errorMessage=str(e),
            message="Failed to generate test cases"
        )