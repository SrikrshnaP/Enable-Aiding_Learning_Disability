import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import easyocr

def writeocr():
    def identify(image):
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)
        print(result)
        return result[0][1] 

    # lis = ['GOOD', "DAD", "MOM", "BAD"]
    # prompt = random.choice(lis)
    prompt = "GOOD"
    st.markdown(f'*{prompt}*')

    stroke_width = 15 #st.sidebar.slider("Stroke width: ", 1, 25, 3)
    stroke_color = "#000000" #st.sidebar.color_picker("Stroke color hex: ")
    bg_color = "#EEEEEE" #st.sidebar.color_picker("Background color hex: ", "#eee")
    #bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
    drawing_mode = "freedraw" #st.sidebar.selectbox("Drawing tool:", ("freedraw", "transform", "line", "rect", "circle", "polygon", "point"))
    realtime_update = True #st.sidebar.checkbox("Update in realtime", True)

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=None,
        update_streamlit=realtime_update,
        height=300,
        width=1000,
        drawing_mode=drawing_mode,
        display_toolbar=True, #st.sidebar.checkbox("Display toolbar", True),
        key="full_app",
    )
    
    if(st.button("Submit", key='submit')):
        image = canvas_result.image_data
        result = identify(image)
        st.write(result)
        if(result == prompt):
            response = "CORRECT"
            st.success(response)
        else:
            response = "INCORRECT"
            st.error(response)


