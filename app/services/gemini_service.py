import os
import json
import logging
from google import genai
from dotenv import load_dotenv
from app.errors.error import Error
import typing_extensions as typing
from app.utilities.utils import Utility
from app.interfaces.llm_provider import LLMProvider

load_dotenv()

logger = logging.getLogger(__name__)

class TestScenarios(typing.TypedDict):
    scenarios: list[str]

class TestCases(typing.TypedDict):
    scenarios: list[str]

class GeminiService(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

    async def generate_scenarios(self, requirement: str) -> list[str]:
        try:
            prompt = Utility.load_prompt("test_scenario_prompt_one.txt", data={"requirement": requirement}) + "\n" + Utility.load_prompt("test_scenario_prompt_two.txt")

            client = genai.Client(api_key=self.api_key)

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                config=genai.types.GenerateContentConfig(
                    temperature=0.7,
                    response_mime_type="application/json",
                    response_schema=TestScenarios,
                ),
                contents=prompt
            )

            generated_text = response.text
            return json.loads(generated_text)
        except Exception as e:
            logger.exception(f"Error generating test scenario: {e}")
            raise Error("An error occured. Please try again later", 500)
        
    async def generate_test_cases(self, scenario: str) -> list[str]:
        try:
            prompt = Utility.load_prompt("test_case_prompt_one.txt", data={"scenario": scenario}) + "\n" + Utility.load_prompt("test_case_prompt_two.txt")

            client = genai.Client(api_key=self.api_key)

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                config=genai.types.GenerateContentConfig(
                    temperature=0.7,
                    response_mime_type="application/json",
                    response_schema=TestCases,
                ),
                contents=prompt
            )

            generated_text = response.text
            return json.loads(generated_text)
        except Exception as e:
            logger.exception(f"Error generating test cases: {e}")
            raise Error("An error occured. Please try again later", 500)