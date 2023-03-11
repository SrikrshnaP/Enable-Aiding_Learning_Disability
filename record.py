import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write

def record():
    fs = 44100
    seconds = 5
    st.write("Please wait for the recording to finish in 5 seconds...")

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  
    write('output.wav', fs, myrecording)