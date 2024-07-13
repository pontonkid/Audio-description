

import gradio as gr
from PIL import Image
from transformers import pipeline
import scipy.io.wavfile as wavfile
import numpy as np



caption_image = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

Narrator = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")


def generate_audio(text):
    # Generate speech from the input text using the Narrator (VITS model)
    Narrated_Text = Narrator(text)
    
    # Extract the audio data and sampling rate
    audio_data = np.array(Narrated_Text["audio"][0])
    sampling_rate = Narrated_Text["sampling_rate"]
    
    # Save the generated speech as a WAV file
    wavfile.write("generated_audio.wav", rate=sampling_rate, data=audio_data)
    
    # Return the filename of the saved audio file
    return "generated_audio.wav"


def caption_my_image(pil_image):
    # Use BLIP to generate a textual description (semantics) of the input image
    semantics = caption_image(images=pil_image)[0]["generated_text"]
    
    # Generate audio from the textual description using the generate_audio function
    return generate_audio(semantics)


demo = gr.Interface(
    fn=caption_my_image,
    inputs=[gr.Image(label="Select Image", type="pil")],
    outputs=[gr.Audio(label="Generated Audio")],
    title="Project 8: Audio Caption Image",
    description="This application provides audio captions for images."
)

demo.launch()








