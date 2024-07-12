# Audio-description

This app generates audio descriptions for images using Vision Language Models (VLM) and Text-to-Speech (TTS) technology.



# Purpose
This application is designed to assist visually impaired users by providing audio descriptions of images. It can also be used in various scenarios such as creating audio captions for educational materials, enhancing accessibility for digital content, and more.

# Technologies/Tools Used
Framework: Gradio

VLM: Blip

TTS: Kakao


# Limits
The quality of the description depends on the image clarity and content.
The application might not work well with images that have complex scenes or unclear subjects.
Audio generation time may vary depending on the input image size and content.


Demo 

<script
	type="module"
	src="https://gradio.s3-us-west-2.amazonaws.com/4.37.2/gradio.js"
></script>

<gradio-app src="https://pontonkid-image-audio-description.hf.space"></gradio-app>
