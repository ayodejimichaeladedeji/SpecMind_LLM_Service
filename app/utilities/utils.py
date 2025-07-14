import io
import fitz
from docx import Document

from pathlib import Path
from app.errors.error import Error

import logging

from fastapi import HTTPException, UploadFile

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
            logger.exception(f"Error loading prompt file '{file_name}': {e}")
            raise Error(f"An error occurred. Please try again later", 500)

    @staticmethod
    def extract_text_from_file(file: UploadFile) -> str:
        try:
            ext = file.filename.split(".")[-1].lower()
            content = file.file.read()

            if ext == "pdf":
                doc = fitz.open(stream=content, filetype="pdf")
                return "\n".join([page.get_text() for page in doc])
            elif ext == "docx":
                doc = docx.Document(io.BytesIO(content))
                return "\n".join([para.text for para in doc.paragraphs])
            else:
                logger.exception(f"Unsupported file type. Upload a PDF or DOCX.")
                raise Error("Unsupported file type. Upload a PDF or DOCX.", 400)
        except Exception as e:
            logger.exception(f"Error extracting text from user story: {e}")
            raise Error(f"An error occurred. Please try again later", 500)
