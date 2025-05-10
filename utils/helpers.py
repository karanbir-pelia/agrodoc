# Contains helper functions for the application
import streamlit as st
from utils.data import get_class_names_by_plant

def print_classname():
    """
    Display supported plants and their possible conditions in the UI.
    """
    class_names = get_class_names_by_plant()

    st.divider()

    column1, column2 = st.columns(2)
    current_column = column2

    for plant in class_names:
        # Alternate between columns
        if current_column == column2:
            current_column = column1
        else:
            current_column = column2

        with current_column:
            st.markdown(f"##### {plant}")
            for condition in class_names[plant]:
                st.markdown(f"- {condition}")

def validate_image(file):
    """
    Validate if the uploaded file is a valid image.

    Args:
        file: Uploaded file object

    Returns:
        bool: True if valid, False otherwise
    """
    import pathlib
    import unicodedata

    if file is not None:
        name = unicodedata.normalize("NFKC", file.name).strip()
        suffix = pathlib.Path(name).suffix.lower()

        if suffix not in {".jpg", ".jpeg", ".png"}:
            st.error(f"Sorry, `{suffix}` files aren't allowed. Please upload a .jpg/.jpeg/.png")
            return False
        return True
    return False