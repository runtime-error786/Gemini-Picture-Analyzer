import google.generativeai as genai
import streamlit as st
from PIL import Image
from io import BytesIO

# Configure Google Gemini API (Replace with your actual API key)
genai.configure(api_key='AIzaSyCiSQRuCyIr0A4k-wjDVKREtNXklBiTMDg')
model = genai.GenerativeModel('gemini-pro-vision')

