
import gradio as gr
from PIL import Image
from transformers import pipeline
import scipy.io.wavfile as wavfile
import numpy as np



caption_image = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

Narrator = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")





