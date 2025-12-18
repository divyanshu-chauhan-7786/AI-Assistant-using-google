import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech


def main():
    st.set_page_config(page_title="Multimodal AI Assistant")
    st.title("Multimodal AI Assistant")
    st.write("Click the button and ask your question using your voice.")

    if st.button("Ask anything to me"):
        status = st.empty()

        with st.spinner("Listening..."):
            user_text = voice_input()

        if not user_text or user_text.strip() == "":
            status.warning("No voice detected. Please try again.")
            return

        status.success(f"You said: {user_text}")

        with st.spinner("Generating response..."):
            response = llm_model(user_text)

        if not response or response.strip() == "":
            st.error("Model did not return any response.")
            return

        
        text_to_speech(response)
        with open("speech.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.text_area(
            label="AI Response",
            value=response,
            height=320
        )

        st.audio(audio_bytes)

        st.download_button(
            label="Download Speech",
            data=audio_bytes,
            file_name="speech.mp3",
            mime="audio/mp3"
        )


if __name__ == "__main__":
    main()
