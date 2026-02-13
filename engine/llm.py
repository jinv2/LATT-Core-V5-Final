import requests

class OllamaLLM:
    def __init__(self, model_name="qwen2.5:7b"):
        self.url = "http://127.0.0.1:11434/api/generate"
        self.model_name = model_name

    def chat(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            # 增加到 300 秒，哪怕模型在慢爬，连接也不会断
            response = requests.post(self.url, json=payload, timeout=300)
            response.raise_for_status()
            return response.json().get("response", "无响应")
        except Exception as e:
            return f"LLM Error: {str(e)}"
