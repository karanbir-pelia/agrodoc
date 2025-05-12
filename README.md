# 🌱 AgroDoc - Crop Disease Recognition System

## Overview

AgroDoc is a web application designed to help farmers detect and manage plant diseases early and accurately. By leveraging convolutional neural networks (CNNs), the system analyzes images of plant leaves to identify diseases, providing timely insights that can help protect crop yields and ensure food security.

## Features

-   **Disease Recognition**: Upload images of plant leaves to detect and classify diseases
-   **Comprehensive Database**: Supports multiple crops and their associated diseases
-   **Remedial Measures**: Provides guidance on how to treat identified plant diseases
-   **User-Friendly Interface**: Simple and intuitive design for ease of use

## Supported Crops

The system currently supports disease detection for the following crops:

-   Apple
-   Bell Pepper
-   Blueberry
-   Cherry
-   Corn
-   Grape
-   Orange
-   Peach
-   Potato
-   Raspberry
-   Soybean
-   Squash
-   Strawberry
-   Tomato

## Installation

### Prerequisites

-   Python 3.11+
-   pip package manager

### Setup

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/agrodoc.git
    cd agrodoc
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the application:
    ```
    streamlit run app.py
    ```

## Usage

1. Navigate to the application in your web browser (typically at http://localhost:8501)
2. Use the sidebar to navigate between different sections:
    - **Home**: Overview of the application
    - **Read Me**: Detailed information about the project
    - **Disease Recognition**: Upload plant leaf images for analysis
    - **About Me**: Information about the developer
3. In the Disease Recognition section, upload an image of a plant leaf
4. Click "Run Disease Recognition" to analyze the image
5. View the results and recommended remedial measures

## Technologies Used

-   **Programming Languages**: Python, HTML, CSS
-   **Libraries and Frameworks**:
    -   Streamlit: For the web application interface
    -   TensorFlow: For the CNN model implementation
    -   NumPy: For numerical computations
    -   Matplotlib: For data visualization
    -   OpenCV: For image processing
-   **Tools**: Anaconda, Jupyter Notebook, Kaggle, Visual Studio Code

## Project Structure

-   `app.py`: Main application entry point
-   `model/`: Contains the trained CNN model and notebooks
-   `utils/`: Utility functions for data handling and model operations
-   `webpages/`: Different pages of the web application
-   `images/`: Images used in the application

## Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional agricultural advice.

## License

[Include your license information here]

## Acknowledgements

-   Dataset sourced from Kaggle
-   [Add any other acknowledgements here]
