import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from .base_llm import BaseLLM
from openai import OpenAI
from source.config import API_BASE, QWEN_API_KEY, MODEL

class QwenLLM(BaseLLM):
    def __init__(self, api_key: str, model: str):
        super().__init__()

        self.client = OpenAI(api_key=api_key, base_url=API_BASE)
        self.model = model

    def chat(self, prompt: str):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        res = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return res.choices[0].message.content
    
if __name__ == "__main__":
    llm = QwenLLM(api_key=QWEN_API_KEY, model=MODEL)
    print(llm.chat("请给我一个5个单词的英文句子"))
