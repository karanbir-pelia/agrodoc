# Home page
import streamlit as st

def show():
    """Display the Home page content."""
    st.markdown("# 🌱 CropDoc")
    st.markdown("### Crop Disease Recognition System")
    st.divider()

    st.image(image="images/home_background.jpg", use_container_width=True)

    st.markdown('''
                #### A healthy crop leads to full bellies and thriving communities!

                This web app is designed to help farmers detect crop diseases early and accurately. With this system, we aim to revolutionize the way plant diseases are detected and managed in agriculture. By harnessing the power of advanced technology, specifically convolutional neural networks (CNNs), we strive to provide farmers with a reliable and efficient tool for early disease identification. Ultimately, our goal is to safeguard crop yields, bolster food security, and ensure the prosperity of farming communities worldwide.

                ##### To continue, please select an option from the dashboard.''')