import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

model_face_mesh = mp_face_mesh.FaceMesh()

st.title("OpenCV Operations")
st.subheader("Image operations")


st.write("This application performs various operations with OpenCV")


add_selectbox = st.sidebar.selectbox(
    "What operations you would like to perform?",
    ("About", "Grayscale", "Blue", "Meshing")
)


if add_selectbox == "About":
    st.write("This application is a demo for streamlit.")

elif add_selectbox == "Grayscale":
    image_file_path = st.sidebar.file_uploader("Upload image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        st.image(gray_image)

elif add_selectbox == "Blue":
    image_file_path = st.sidebar.file_uploader("Upload image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        zeros = np.zeros(image.shape[:2], dtype="uint8")
        r, g, b = cv2.split(image)
        blue_image = cv2.merge([zeros, zeros, b])
        st.image(blue_image)

elif add_selectbox == "Meshing":
    image_file_path = st.sidebar.file_uploader("Upload image")
    if image_file_path is not None:
        image = np.array(Image.open(image_file_path))
        st.sidebar.image(image)
        results = model_face_mesh.process(image)

        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image, face_landmarks)
        st.image(image)


color_schemes = st.sidebar.radio("Choose your color",
                                 ("B", "G", "R")
                                 )


image = None
image_file_path = st.sidebar.file_uploader("Upload image")
if image_file_path is not None:
    image = np.array(Image.open(image_file_path))
    st.sidebar.image(image)
if color_schemes == "B":
    st.write("Converting to blue")
    st.write(image)

elif color_schemes == "G":
    st.write("Converting to Green")
elif color_schemes == "R":
    st.write("Converting to Red")