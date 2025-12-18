import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import uuid

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def llm_model(user_text: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(user_text)

        if hasattr(response, "text") and response.text:
            return response.text


        if response.candidates:
            return response.candidates[0].content.parts[0].text

        return "Sorry, I could not generate a response."

    except Exception as e:
        return f"LLM Error: {str(e)}"


def text_to_speech(text: str) -> str:
    filename = f"speech_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("audio", filename)

    os.makedirs("audio", exist_ok=True)

    tts = gTTS(text=text, lang="en")
    tts.save(filepath)

    return filename
