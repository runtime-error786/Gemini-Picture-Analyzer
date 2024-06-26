import google.generativeai as genai
import streamlit as st
from PIL import Image
from io import BytesIO

# Configure Google Gemini API (Replace with your actual API key)
genai.configure(api_key='AIzaSyCiSQRuCyIr0A4k-wjDVKREtNXklBiTMDg')
model = genai.GenerativeModel('gemini-pro-vision')

st.title('Gemini Receipt Visualizer')
st.sidebar.title('Upload an Image')

# Upload image
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def convert_image_to_pil(image):
    return Image.open(BytesIO(image.read()))

if uploaded_file is not None:
    # Convert image to PIL format
    pil_image = convert_image_to_pil(uploaded_file)
    # Display uploaded image
    st.image(pil_image, caption='Uploaded Image.', use_column_width=True)
    st.write('Image has been converted to PIL format.')

# Input field for user question
user_question = st.text_input('Ask a question to the image uploader:')

def send_to_gemini(image, question):
    # Send the image and question to Gemini API
    response = model.generate_content([question, image])
    return response.text

if st.button('Submit Question') and user_question and uploaded_file is not None:
    st.write(f'Question asked: {user_question}')
    try:
        response = send_to_gemini(pil_image, user_question)
        st.write('Response from Gemini:', response)
    except Exception as e:
        st.write('Error:', e)
