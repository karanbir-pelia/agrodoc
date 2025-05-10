# Read Me page
import streamlit as st
from utils.helpers import print_classname

def show():
    """Display the Read Me page content."""
    st.markdown("# Read Me")
    st.divider()
    st.markdown('''
                ### How to Use
                - **Home**: Return to the home page.
                - **Read Me**: View the project overview, system workflow, technologies used, and supported crops and conditions.
                - **Disease Recognition**: Upload an image of a plant leaf to detect and classify plant diseases.
                - **About Us**: Learn more about the developers behind this project.

                ### Project Overview
                - **Objective**: Develop a crop disease recognition system to help farmers detect and manage plant diseases.
                - **Methodology**: Utilize convolutional neural networks (CNNs) to classify plant diseases based on images of plant leaves.
                - **Dataset**: Kaggle dataset containing images of diseased and healthy plant leaves.
                - **Model**: CNN model trained on the dataset to classify plant diseases.

                ### System Workflow
                - **Input Image**: A user uploads an image of a plant leaf showing signs of some disease.
                - **Image Analysis**: The system analyzes the image using advanced technology to identify if any disease is present.
                - **Display Result**: The user receives clear and understandable results on their device, displaying the detected crop and disease (if any).

                ### Technologies Used
                - **Programming Languages**: Python, HTML, CSS
                - **Libraries and Frameworks**: Matplotlib, NumPy, OpenCV, Streamlit, TensorFlow
                - **Tools**: Anaconda, Jupyter Notebook, Kaggle, Visual Studio Code

                ### Supported Crops and Conditions''')

    with st.expander("**Click here to view the supported crops and conditions**"):
        print_classname()