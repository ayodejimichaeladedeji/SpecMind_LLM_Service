from fastapi import APIRouter, UploadFile, File, Depends
from app.schemas.responses import APIResponse
from app.interfaces.llm_provider import LLMProvider
from app.services.gemini_service import GeminiService
from app.schemas.requests import CaseRequest, ScenarioRequest
from app.utilities.utils import Utility

router = APIRouter()

generator = GeminiService()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/generate-scenarios")
async def gen_scenarios(req: ScenarioRequest, gen: LLMProvider = Depends(lambda: generator)):
    result = await gen.generate_scenarios(req.requirement)
    return APIResponse(
        isSuccess=True,
        body=result,
        message="Test scenarios generated successfully"
    )

@router.post("/generate-test-cases")
async def gen_test_cases(req: CaseRequest, gen: LLMProvider = Depends(lambda: generator)):
    result = await gen.generate_test_cases(req.scenario)
    return APIResponse(
        isSuccess=True,
        body=result,
        message="Test cases generated successfully"
    )

@router.post("/generate-test-scenarios-from-user-story")
async def generate_scenarios_from_user_story(user_story: UploadFile = File(...), gen: LLMProvider = Depends(lambda: generator)):
    text = Utility.extract_text_from_file(user_story)
    scenarios = await gen.generate_scenarios_from_user_story(text)
    return APIResponse(
        isSuccess=True,
        body=scenarios,
        message="Test scenarios generated from document"
    )