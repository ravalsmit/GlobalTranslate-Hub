# GlobalTranslate Hub

GlobalTranslate Hub is a Streamlit web application that allows users to translate text between different languages and listen to the translated text using text-to-speech (TTS) conversion.

## Features
- **Text Translation**: Translate text from one language to another with support for multiple languages.
- **Text-to-Speech (TTS)**: Convert translated text into speech in the desired language.
- **Language Selection**: Choose source and destination languages from a list of supported languages.

## Technologies Used
- Streamlit
- Googletrans
- gTTS
- Tempfile

## How to Use
1. Enter the text you want to translate in the input text area.
2. Select the source and destination languages from the dropdown menus.
3. Click the "Translate" button to translate the text.
4. Listen to the translated text by clicking the play button next to it.
5. To start over, click the "Clear" button to clear the input text area.

## How to Run Locally
1. Clone this repository.
2. Install the required dependencies (`streamlit`, `googletrans`, `gtts`).
3. Run the Streamlit app using the command `streamlit run main.py`.
4. Access the app in your web browser at `http://localhost:8501`.
