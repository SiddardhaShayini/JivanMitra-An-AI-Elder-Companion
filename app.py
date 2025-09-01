# app.py

import os
import streamlit as st
from gtts import gTTS
import google.generativeai as genai
from dotenv import load_dotenv
from streamlit_mic_recorder import mic_recorder
import json
import io

# 1. Initial Configuration and Setup

st.set_page_config(page_title="JivanMitra", page_icon="🤖", layout="wide")

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}", icon="🚨")
    st.stop()

# Initialize session state
if 'reminders' not in st.session_state:
    st.session_state.reminders = []
# Add a new state to track the ID of the last processed audio
if 'last_audio_id' not in st.session_state:
    st.session_state.last_audio_id = None

# 2. Helper Functions (text_to_speech)

def text_to_speech(text, lang):
    """Converts text to speech using gTTS and returns the audio bytes."""
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Use an in-memory binary stream to hold the audio data
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        
        # Go to the beginning of the stream
        fp.seek(0)
        
        # Read the bytes from the stream
        audio_bytes = fp.read()
        return audio_bytes
    except Exception as e:
        st.error(f"Error in Text-to-Speech: {e}")
        return None

def check_for_reminder(user_text):
    """Uses Gemini to check if the user text is a reminder request."""
    prompt = f"""
    Analyze the following text to determine if it is a reminder request.
    If it is a reminder, extract the core reminder task. Respond ONLY with a JSON object.
    The JSON should have one key: "reminder_task".
    If a reminder is found, the value should be the string of the task. If not, the value should be null.
    Text to analyze: "{user_text}"
    """
    try:
        response = model.generate_content(prompt)
        json_response = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(json_response)
    except Exception as e:
        st.warning(f"Could not check for reminder due to an error: {e}")
        return {"reminder_task": None}

# 3. Streamlit User Interface

with st.sidebar:
    st.title("JivanMitra Settings")
    st.write("Your AI Elder Companion")
    
    language_code = st.selectbox(
        "Choose your language:",
        ("en", "hi", "te"),
        format_func=lambda x: {"en": "English", "hi": "हिंदी (Hindi)", "te": "తెలుగు (Telugu)"}[x]
    )
    language_full_name = {"en": "English", "hi": "Hindi", "te": "Telugu"}[language_code]

    st.divider()
    st.subheader("Your Reminders")
    if not st.session_state.reminders:
        st.info("You have no reminders set.")
    else:
        for i, reminder in enumerate(st.session_state.reminders):
            st.info(f"{i+1}. {reminder}")

st.title("🤖 JivanMitra")
st.markdown(f"Hello! I am JivanMitra. How can I help you today? (Speaking in **{language_full_name}**)")

audio_info = mic_recorder(
    start_prompt="Click to speak",
    stop_prompt="Click to stop",
    key='recorder'
)

# 4. Core Logic: Process Audio and Generate Response

if audio_info and audio_info['bytes']:
    # Check if this audio is new. If we've already processed it, do nothing.
    if audio_info['id'] != st.session_state.last_audio_id:

        st.info("Processing your request...")
        
        # Save audio and transcribe
        with open("input_audio.mp3", "wb") as f:
            f.write(audio_info['bytes'])

        with st.spinner("Transcribing audio..."):
            try:
                audio_file = genai.upload_file(path="input_audio.mp3")
                transcribe_prompt = "Transcribe the following audio recording and provide only the text."
                response = model.generate_content([transcribe_prompt, audio_file])
                user_text = response.text
                st.write(f"**You said:** *{user_text}*")
            except Exception as e:
                st.error(f"Sorry, I could not understand the audio: {e}", icon="🚨")
                st.stop()
        
        # Check for reminder
        reminder_data = check_for_reminder(user_text)
        reminder_task = reminder_data.get("reminder_task")

        if reminder_task:
            st.session_state.reminders.append(reminder_task)
            confirmation_text = f"Okay, I will remind you to: {reminder_task}"
            st.success(confirmation_text)
            audio_response = text_to_speech(confirmation_text, language_code)
            if audio_response:
                st.audio(audio_response, format="audio/mp3")

            # Remember that we've processed this audio file
            st.session_state.last_audio_id = audio_info['id']
            st.rerun()

        else:
            # Normal conversation
            system_prompt = f"""
            You are 'JivanMitra', a warm, empathetic, and patient AI companion for elderly individuals in India.
            Your personality is like a caring grandchild. You must respond in {language_full_name} only.
            Keep your responses simple, positive, and respectful.
            You can share culturally relevant stories, spiritual quotes, or simple health tips if relevant.
            """
            with st.spinner("JivanMitra is thinking..."):
                try:
                    response = model.generate_content([system_prompt, user_text])
                    ai_response_text = response.text
                    st.text_area("JivanMitra's Response:", value=ai_response_text, height=200)

                    audio_response = text_to_speech(ai_response_text, language_code)
                    if audio_response:
                        st.audio(audio_response, format="audio/mp3")
                except Exception as e:
                    st.error(f"Error generating response from Gemini: {e}")

            # Remember that we've processed this audio file here too
            st.session_state.last_audio_id = audio_info['id']

