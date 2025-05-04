from pathlib import Path
from app.errors.error import Error

import logging
logger = logging.getLogger(__name__)

class Utility:
    @staticmethod
    def load_prompt(file_name: str, data: str = None) -> str:
        try:
            base_dir = Path(__file__).resolve().parent.parent
            prompt_file_path = base_dir / "prompts" / file_name

            with open(prompt_file_path, "r", encoding="utf-8") as file:
                prompt_template = file.read()

                if data:
                    prompt = prompt_template.format(**{k: v.strip() for k, v in data.items()})
                else:
                    prompt = prompt_template

            return prompt
        except Exception as e:
            logger.exception(f"Error loading prompt file '{file_name}'")
            raise Error(f"An error occured. Please try again later '{file_name}': {e}")
        