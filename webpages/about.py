# About Me page
import streamlit as st
import base64

def show():
    """Display the About Me page content."""
    st.markdown("# About Me")
    st.markdown("### Meet the brain behind this project!")
    st.divider()

    row1 = st.container()
    with row1:
        st.markdown("#### Karanbir Singh Pelia")
        st.markdown("##### Computer Science Aficionado | Lifelong Learner")
        column1, column2 = st.columns(2)
        with column1:
            st.image("images/developer.png", use_container_width=True)
        with column2:
            st.markdown('''I'm a Master's candidate in Computer Science at Stony Brook University, specializing in AI and data science. As a Graduate Research Assistant, I've advanced visual storytelling and evaluated LLM alignment with human cognition. With internship experience automating data workflows and leading database initiatives, I excel in Python, TensorFlow, OpenCV, and machine learning. Here, I present my plant disease recognition system—a classifier trained on leaf imagery for accurate disease detection. In addition to this, I've also built driver fatigue detectors and automated webpage-to-presentation pipelines. I'm passionate about crafting innovative, data-driven solutions that enhance decision-making and user experience.''')
    st.divider()

    row2 = st.container()
    with row2:
        st.markdown("### Connect with me!")
        columns = st.columns(6)
        with columns[0]:
            st.markdown(''' <a href = "https://www.linkedin.com/in/karanbir-singh-pelia/">
            <img src = "data:image/webp;base64, {}" width="48" height="48" style="display: block; margin: auto;"> </a>
        '''.format(base64.b64encode(open("images/linkedin.webp",
                                        "rb").read()).decode()),
            unsafe_allow_html=True
            )
        with columns[1]:
            st.markdown(''' <a href = "https://github.com/karanbir-pelia">
            <img src = "data:image/png;base64, {}" width="48" height="48" style="display: block; margin: auto;"> </a>
        '''.format(base64.b64encode(open("images/github.png",
                                        "rb").read()).decode()),
            unsafe_allow_html=True
            )
        with columns[2]:
            st.markdown(''' <a href = "mailto:karanbirsinghpelia@gmail.com">
            <img src = "data:image/webp;base64, {}" width="48" height="48" style="display: block; margin: auto;"> </a>
        '''.format(base64.b64encode(open("images/email.png",
                                        "rb").read()).decode()),
            unsafe_allow_html=True
            )
        with columns[3]:
            st.markdown(''' <a href = "https://drive.google.com/drive/folders/1E5J3iqiNt7qkAwn2VaDFz3qUsORdl7c6?usp=sharing">
            <img src = "data:image/webp;base64, {}" width="48" height="48" style="display: block; margin: auto;"> </a>
        '''.format(base64.b64encode(open("images/resume.png",
                                        "rb").read()).decode()),
            unsafe_allow_html=True
            )
    st.divider()