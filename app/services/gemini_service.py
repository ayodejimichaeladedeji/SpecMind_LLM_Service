# app/services/gemini_service.py
import os
import json
from pathlib import Path
from google import genai
from dotenv import load_dotenv
import typing_extensions as typing
from app.utilities.utils import Utility
from app.interfaces.llm_provider import LLMProvider

load_dotenv()

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
            
            if not prompt:
                return []

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
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except Exception as e:
            print(f"Error generating scenarios: {e}")
            return []
        
    async def generate_test_cases(self, scenario: str) -> list[str]:
        try:
            prompt = Utility.load_prompt("test_case_prompt_one.txt", data={"scenario": scenario}) + "\n" + Utility.load_prompt("test_case_prompt_two.txt")
            
            if not prompt:
                return {}

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
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except Exception as e:
            print(f"Error generating test cases: {e}")
            return {}