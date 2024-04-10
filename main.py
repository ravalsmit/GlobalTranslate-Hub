import streamlit as st
from googletrans import Translator
from gtts import gTTS
from tempfile import NamedTemporaryFile


# Function to translate text
def translate_text(text, dest_language, src_language=None):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_language, src=src_language)
        return translated_text.text, translated_text.src
    except Exception as e:
        st.error(f"Translation error: {e}")
        return None, None


# Function to convert text to speech
def text_to_speech(text, language_code):
    try:
        with NamedTemporaryFile(delete=False) as fp:
            tts = gTTS(text, lang=language_code)
            tts.save(fp.name)
            return open(fp.name, "rb").read()
    except Exception as e:
        st.error(f"Text-to-speech conversion error: {e}")
        return None


# Streamlit app layout
def main():
    st.title("GlobalTranslate Hub")

    # Input text area
    input_text = st.text_area("Input Text")  # Unique key added
    st.markdown("""<style>.stTextInput{background-color: #f0f0f5;}</style>""", unsafe_allow_html=True)

    languages = {
        "Automatic": "auto",
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Italian": "it",
        "Japanese": "ja",
        "Chinese": "zh-CN"
    }

    # Language selection in one line
    col1, col2 = st.columns(2)
    with col1:
        src_language = st.selectbox("Source Language", list(languages.keys()),
                                    index=list(languages.keys()).index("English"))
    with col2:
        dest_language = st.selectbox("Destination Language", list(languages.keys()))

    # Translate button
    if st.button("Translate 🌐"):
        if input_text:
            src_lang_code = languages[src_language]
            dest_lang_code = languages[dest_language]

            # Translate text
            translated_text, src_lang_detected = translate_text(input_text, dest_lang_code, src_lang_code)
            if translated_text:
                st.write("Translated Text:")
                st.write(translated_text)

                # Text-to-speech
                audio_bytes = text_to_speech(translated_text, dest_lang_code)
                if audio_bytes:
                    st.audio(audio_bytes, format="audio/mp3", start_time=0)
        else:
            st.warning("Please enter some text to translate.")


if __name__ == "__main__":
    main()
