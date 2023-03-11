import speech_recognition
import streamlit as st
import record

def pronounce():
    recognizer = speech_recognition.Recognizer()
    st.title("Check your pronounciation!")

    st.subheader("Speak the word and compare it with the prompt")
    prompt = "Beautiful"
    st.write("Prompt : ", prompt)
    st.write("Press the button to start recording")

    start_button = st.button("Start")

    while True:
        if start_button:
            record.record()
            break

    with speech_recognition.AudioFile("sample.wav") as source:
        audio = recognizer.record(source)
        try:
            s = recognizer.recognize_google(audio)
            st.write("Recognised Text: "+s)
            if (s.lower() == prompt.lower()):
                st.write("Correct")
            else:
                st.write("Incorrect")
        except Exception as e:
            print("Exception: "+str(e))