from pathlib import Path

class Utility:
    @staticmethod
    def load_prompt(file_name: str, data: str = None) -> str:
        try:
            base_dir = Path(__file__).resolve().parent.parent
            prompt_file_path = base_dir / "prompts" / file_name

            # with open(prompt_file_path, "r", encoding="utf-8") as file:
            #     if data:
            #         prompt = file.read().format(requirement=data.strip())
            #     else:
            #         prompt = file.read()

            with open(prompt_file_path, "r", encoding="utf-8") as file:
                prompt_template = file.read()

                if data:
                    prompt = prompt_template.format(**{k: v.strip() for k, v in data.items()})
                else:
                    prompt = prompt_template

            return prompt
        except Exception as e:
            print(f"Error loading prompt file '{file_name}': {e}")
            return ""