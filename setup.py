from setuptools import find_packages, setup

setup(
    name="multilingual virtual ai assistant",
    version="0.0.0",
    author="Divyanshu Chauhan",
    author_email="divyanshuchauhan471@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit","flask"]
)