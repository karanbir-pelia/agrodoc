# Disease Recognition page
import streamlit as st
from time import sleep
from utils.model import disease_recognition
from utils.data import get_remedial_measures
from utils.helpers import validate_image

def show():
    """Display the Disease Recognition page content."""
    st.markdown("# Disease Recognition")
    st.divider()

    input_image = st.file_uploader("**Upload an image**")

    if input_image is not None and validate_image(input_image):
        st.markdown("**Image uploaded successfully**")

        column1, column2 = st.columns(2)

        with column1:
            if st.button("View Image", use_container_width=True):
                st.image(input_image, use_container_width=True)

        with column2:
            run_recognition = True if st.button("Run Disease Recognition",
                                                use_container_width=True) else False

        if run_recognition:
            detected_crop, detected_condition = disease_recognition(input_image)

            with st.spinner("Please wait..."):
                remedial_measures = get_remedial_measures()

                if detected_condition != "Healthy":
                    remedial_measures_text = remedial_measures[detected_crop][detected_condition]
                else:
                    remedial_measures_text = ""

                sleep(2.5)
                st.success(f'''Detected Crop: {detected_crop}
                            \nDetected Condition: {detected_condition}\n
                            {remedial_measures_text}''')