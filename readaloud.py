import pyttsx3
import streamlit as st

def read_aloud():
    st.title("Read Aloud With Me!")

    if st.button("Read Aloud", key='submit'):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate+50)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        if st.button("Stop"):
            engine.stop()

        report = []
        res_box = st.empty()
        passage = """Wake up! It's a lovely day. Please get up And come and play. The birds are singing in the trees, Arid you can hear the buzzing bees. Wash and dress And come on oil -Everyone is up and about. The cow, the horses, the ducks And the sheep, The tiniest chicken."""
        passage = passage.split()
        for resp in passage:
            report.append(resp)
            result1 = " ".join(report[:-1]).strip()
            result2 = report[-1]
            result1 = result1.replace("\n", " ")
            res_box.markdown(f'*{result1}* **:red[{result2}]**')
            engine.say(resp)
            engine.runAndWait()
            