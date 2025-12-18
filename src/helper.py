import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("User said:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Speech Recognition error: {e}"


def llm_model(user_text):
    try:
        model = genai.GenerativeModel("models/gemini-flash-latest")
        response = model.generate_content(user_text)

        if hasattr(response, "text") and response.text:
            return response.text

        if response.candidates:
            return response.candidates[0].content.parts[0].text

        return "Sorry, I could not generate a response."

    except Exception as e:
        return f"LLM Error: {str(e)}"



def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")
