
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








