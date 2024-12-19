from langchain.llms.base import BaseLLM
from langchain.schema import LLMResult, Generation
from typing import Optional, List, Any
from groq import Groq

class GroqAPI(BaseLLM):
    api_key: str
    model_name: str

    def __init__(self, api_key: str, model_name: str):
        super().__init__(api_key=api_key, model_name=model_name)
        self._client = Groq(api_key=api_key)
        self.model_name = model_name

    @property
    def _llm_type(self) -> str:
        return "GroqAPI"

    @property
    def client(self) -> Groq:
        return self._client

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
        messages = [{"role": "user", "content": prompt}]
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model_name,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Groq API returned error: {e}")

    def _generate(self, prompts: List[str], stop: Optional[List[str]] = None, **kwargs: Any) -> LLMResult:
        generations = []
        for prompt in prompts:
            response = self._call(prompt, stop=stop, **kwargs)
            generations.append([Generation(text=response)])
        return LLMResult(generations=generations)