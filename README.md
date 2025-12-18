#  Multimodal AI Assistant using Google Gemini

A **Multimodal AI Assistant** that allows users to interact using **voice or text**, powered by **Google Gemini models**, with responses delivered in **both text and speech**.

This repository contains **two implementations**:
-  **Streamlit App** – quick demo & local testing
-  **Flask Web App** – browser-based professional UI with JavaScript microphone support

---

##  Features

-  Voice input (Speech-to-Text)
-  AI responses using **Google Gemini**
-  Text-to-Speech audio output
-  Browser microphone support (Flask + JavaScript)
-  Streamlit interface for rapid prototyping
-  Secure API key handling using `.env`
-  Clean and GitHub-friendly project structure

---

##  Architecture Overview

This architecture illustrates how the **Multimodal AI Assistant** processes user voice input and delivers AI-generated voice responses in a web environment.

### 1️⃣ Browser (JavaScript Microphone)
- The user interacts with the application through a web browser.
- Microphone access is handled **entirely on the client side** using the **Web Speech API**.
- This avoids backend microphone access issues and ensures browser-level permissions.

---

### 2️⃣ Speech-to-Text (Client Side)
- The browser converts spoken voice into **text**.
- Only the **recognized text** is sent to the backend.
- This design is **secure, scalable, and production-ready**.

---

### 3️⃣ Flask Backend (API Layer)
- Flask exposes an API endpoint (`POST /ask`).
- It receives the text query in JSON format.
- Flask does **not** handle microphone or speech recognition directly.

---

### 4️⃣ Google Gemini LLM
- The text query is forwarded to **Google Gemini** (`models/gemini-flash-latest`).
- Gemini processes the input and generates a **context-aware AI response**.
- This layer is responsible for reasoning and language understanding.

---

### 5️⃣ Text Response Handling
- The AI-generated response is returned to the Flask backend.
- The response is validated to avoid empty or failed outputs.
- This ensures a reliable user experience.

---

### 6️⃣ Text-to-Speech (TTS Engine)
- The validated text response is converted into speech using **gTTS**.
- An MP3 audio file is generated with a **unique filename**.
- This approach is safe for multi-user scenarios.

---

### 7️⃣ Browser Audio Playback
- The generated audio file is sent back to the browser.
- The browser plays the audio using the HTML `<audio>` element.
- The user hears the AI’s response as natural speech.

---

###  Why This Architecture is Correct

- ✔ Browser mic access (no backend blocking)
- ✔ Scalable for multiple users
- ✔ Secure API key handling
- ✔ Separation of concerns (UI, API, AI)
- ✔ Industry-standard web AI design

This architecture closely mirrors how **real-world AI assistants** are implemented in production systems.

---

## ⚙️ Installation & Setup

Follow the steps below to set up the project locally.

###  Clone the Repository

```bash
git clone https://github.com/divyanshu-chauhan-7786/AI-Assistant-using-google.git
cd AI-Assistant-using-google
```
```bash
python -m venv venv
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
### run for streamlit demo
```bash
streamlit run app.py
```
### run for the flask

```bash
python flask_app.py
```
### Supported Gemini Model
```bash
models/gemini-flash-latest
gemini-3-flash-preview
```

---
## Developer

### Divyanshu Chauhan
####  AI & ML Engineer | Data Analyst | Full-Stack AI Developer

## 🔗 Portfolio:
https://divyanshu-chauhan-7786.github.io/divyanshu-chauhan/

## 🔗 GitHub:
https://github.com/divyanshu-chauhan-7786
