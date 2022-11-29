# Import

import streamlit as st
# import cv2
import numpy as np
from PIL import Image
import pixellib
# from pixellib.instance import instanceSegmentation
from pixellib.torchbackend.instance import instanceSegmentation
import io


################# TITLE #################

st.set_page_config(layout="centered", page_title="PointRend")
logo = Image.open('./logo.png')
st.image(logo)
st.markdown("# IMAGE DETECTION AND SEGMENTATION")
st.markdown("-----")


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        with st.form(key ='PASS1'):
            st.text_input("Username", key="username")
            st.text_input(
                "Password", type="password", key="password"
            )
            st.form_submit_button(label="Login",on_click=password_entered, help=None, args=None, kwargs=None)

        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        with st.form(key ='PASS1'):
            st.text_input("Username", key="username")
            st.text_input(
                "Password", type="password", key="password"
            )
            st.error("Unknown user or incorrect password. Please retry!")
            st.form_submit_button(label="Login", help=None, on_click=password_entered, args=None, kwargs=None)

        return False
    else:
        # Password correct.
        return True

if check_password():

        

    # segment_image = instanceSegmentation()
    # segment_image.load_model("pointrend_resnet50.pkl")

    @st.cache(max_entries=5,ttl=15, allow_output_mutation=True)
    def model():
        segment_image = instanceSegmentation()
        segment_image.load_model("pointrend_resnet50.pkl")
        return segment_image
    
    segment_image = model()



    def show(input, output):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Input")
            st.image(input)

        with col2:
            st.markdown("### Output")
            st.image(output)
            # with open("output.jpg", "rb") as file:
            #         btn = st.download_button(
            #                 label="Download image",
            #                 data=file,
            #                 file_name="flower.png",
            #                 mime="image/png"
            #             )


    ################# Type #################

    st.markdown("## Select Input Type")
    input_type = st.selectbox('Options:',(None, 'Example Image', 'Upload Image', 'Webcam Image'))



    if input_type == 'Upload Image':

        st.markdown("## Upload Image")
        uploaded_file = st.file_uploader("Choose an image file:", type=["jpg", 'jpeg','png'])
        check = st.button('Run')

        
        if (uploaded_file is not None) and (check == True) :
            with st.spinner('Processing...'):
                # Convert the file to an opencv image.
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                uploaded_image = Image.open(io.BytesIO(file_bytes))

                temp_image_save = uploaded_image.save("temp.jpg")
                # Now do something with the image! For example, let's display it:

                segment_image.segmentImage("temp.jpg", show_bboxes = True, output_image_name = "output.jpg")
                out = Image.open('./output.jpg')

                st.markdown("## Prediction")
                show(uploaded_image, out)
                st.success('Done!')
        # check = None

    elif input_type == 'Example Image':
            st.markdown("## Select Example Image")
            option = st.selectbox('Options:',('Example 1', 'Example 2', 'Example 3'))
            check = st.button('Run')
            if check:
                with st.spinner('Processing...'):
                    segment_image.segmentImage(f"{option}.jpg", show_bboxes = True, output_image_name = "output.jpg")
                    out = Image.open('./output.jpg')
                    input = Image.open(f'{option}.jpg')
                    st.markdown("## Prediction")
                    show(input, out)
                    st.success('Done!')
        # check = None

        
    elif input_type == 'Webcam Image':
        st.markdown("## Take a picture")
        img_file_buffer = st.camera_input("Say cheese:")

        if img_file_buffer is not None:
            # To read image file buffer as a PIL Image:
            with st.spinner('Processing...'):
                uploaded_image = Image.open(img_file_buffer)
                temp_image_save = uploaded_image.save("temp.jpg")

                segment_image.segmentImage("temp.jpg", show_bboxes = True, output_image_name = "output.jpg")
                out = Image.open('./output.jpg')

                st.markdown("## Prediction")
                show(uploaded_image, out)

                st.success('Done!')
        # img_file_buffer =None

    # next = False


