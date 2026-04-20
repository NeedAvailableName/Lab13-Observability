from __future__ import annotations

import os
from openai import OpenAI
from .mock_llm import FakeResponse, FakeUsage
from .tracing import observe

class OpenAILLM:
    def __init__(self, model: str = "gpt-4o-mini") -> None:
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    @observe(as_type="generation")
    def generate(self, prompt: str) -> FakeResponse:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Keep your answer under 50 words and use the provided docs."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content or ""
        input_tokens = response.usage.prompt_tokens if response.usage else 0
        output_tokens = response.usage.completion_tokens if response.usage else 0
        
        return FakeResponse(
            text=answer, 
            usage=FakeUsage(input_tokens, output_tokens), 
            model=self.model
        )
