import streamlit as st

st.set_page_config(
        page_title="Enable Educational Aid",
        page_icon=":books:",
    )

import learn
import readaloud
import jago
import wordwrite
import quiz
import pronounce

def main():
    
    st.title("Enable Educational Aid")
    st.subheader("A tool to help you learn your lessons")

    feature_menu = ["Choose what you want to do!", "Learn English Lessons", "Read aloud with me", "Quiz time", "Practice pronounciations", "Write your words","Meet your companion Jago"]

    feature_choice = st.sidebar.selectbox("It's study time!", feature_menu)
    match feature_choice:
        case "Learn English Lessons":
            learn.learn_page()
        case "Read aloud with me":
            readaloud.read_aloud()
        case "Meet your companion Jago":
            jago.jagochat()
        case "Write your words":
            wordwrite.writeocr()
        case "Practice pronounciations":
            pronounce.pronounce()
        case "Quiz time":
            quiz.quiz()



if __name__ == '__main__':
    main()