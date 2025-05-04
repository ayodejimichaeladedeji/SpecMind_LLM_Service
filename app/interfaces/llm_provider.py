from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    async def generate_scenarios(self, requirement: str) -> list[str]:
        pass

    @abstractmethod
    async def generate_test_cases(self, scenario: str) -> list[str]:
        pass
    