import google.generativeai as genai
from src.helper import llm_model

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
