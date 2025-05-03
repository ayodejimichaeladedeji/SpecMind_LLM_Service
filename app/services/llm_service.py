# import os
# import json
# from google import genai
# from dotenv import load_dotenv
# import typing_extensions as typing

# load_dotenv()

# LLM_API_KEY = os.getenv("GEMINI_API_KEY")

# class TestScenarios(typing.TypedDict):
#     scenarios: list[str]

# def load_prompt(requirement: str) -> str:
#     try:
#         with open("./prompts/requirements_prompt_one.txt", "r", encoding="utf-8") as file1:
#             part1 = file1.read().format(requirement=requirement.strip())
#         with open("./prompts/requirements_prompt_two_copy.txt", "r", encoding="utf-8") as file2:
#             part2 = file2.read()
#         return part1 + "\n" + part2
#     except Exception as e:
#         print(f"Error loading prompt parts: {e}")
#         return ""

# async def generate_scenarios(requirement: str):
#     try:
#         prompt = load_prompt(requirement)
#         if not prompt:
#             return []

#         client = genai.Client(api_key=LLM_API_KEY)

#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             config=genai.types.GenerateContentConfig(
#                 temperature=0.7,
#                 response_mime_type="application/json",
#                 response_schema=TestScenarios,
#             ),
#             contents=prompt
#         )

#         generated_text = response.text

#         try:
#             json_output = json.loads(generated_text)
#             return json_output
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON: {e}")
#             return None

#     except Exception as e:
#         print(f"Error generating scenarios: {e}")
#         return []