import streamlit as st
import streamlit.components.v1 as components
import glob
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.PNG")]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)

def learn_page():
    st.title("Poem")
    components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script type="text/javascript">
        function generate(prompt){
        console.log(prompt)
        const endpoint = 'https://api.openai.com/v1/images/generations';

        const data = {
        "model": "image-alpha-001",
        "prompt": "cartoonise "+ prompt,
        "num_images": 1,
        "size": "256x256",
        "response_format": "url"
        };

        const headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
        };

        fetch(endpoint, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.data[0].url);
            const img = document.getElementById('dalle');
            img.src = data.data[0].url;

            // use the generated image URL
        })
        .catch(error => console.error(error));}
    </script>
    
    <style>
    span{   
        color: #007bff;
        cursor: pointer;
    }

    #dalleimage{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>

    <p>
        Wake up Wake up! It's a lovely day.<br/>
        Please get up And come and play. <br/>
        The <span onclick="generate(this.innerText)">birds are singing in the trees</span>, <br/>
        Arid you can hear the <span onclick="generate(this.innerText)">buzzing bees</span>. <br/>
        Wash and dress And come on oil - Everyone is up and about. <br/>
        The <span onclick="generate(this.innerText)">cow, the horses, the ducks And the sheep</span>, <br/>
        The <span onclick="generate(this.innerText)">tiniest chicken</span><br/>
    </p>
    </div>
    <br/>
    <div id="dalleimage">
    <img src="" id="dalle">
    </div>
    """, height=450,
    )

    if st.button("Generate Video"):
        video_file = open('video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    
       