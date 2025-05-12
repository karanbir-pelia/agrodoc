import streamlit as st
from streamlit_option_menu import option_menu
from webpages import home, readme, disease_recognition, about
import os

os.system('python -m pip install -r requirements.txt')

def main():
    """Main application entry point."""
    # Configure the app
    st.set_page_config(page_title="AgroDoc",
                      page_icon="images/logo.png",)

    # Sidebar navigation
    with st.sidebar:
        app_mode = option_menu(
            "Menu",
            ["Home", "Read Me", "Disease Recognition", "About Me"],
            icons=["house", "book", "search", "person-video3"],
            menu_icon="list",
            default_index=0
        )

        st.markdown('''
                    ### Disclaimer
                    \nThis project is for educational purposes only and should not be used as a substitute for professional advice.''')

    # Display appropriate page based on navigation selection
    if app_mode == "Home":
        home.show()
    elif app_mode == "Read Me":
        readme.show()
    elif app_mode == "Disease Recognition":
        disease_recognition.show()
    elif app_mode == "About Me":
        about.show()

if __name__ == "__main__":
    main()