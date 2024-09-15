# **Speech Abuse Detector**

## **1. Files Overview**

- **`app.py`**:  
   The main entry point of the application, handles the routing and runs the Flask server. It sets up the `/` route to serve the front-end interface and `/process` to handle the speech recognition and classification requests.

- **`detector.py`**:  
   This file contains the `SpeechAbuseDetector` class, which encapsulates the logic for:
   - Capturing audio via microphone.
   - Converting audio to text using the `SpeechRecognition` library.
   - Using a pre-trained model from Hugging Face to classify text as "abusive" or "not abusive".

- **`templates/index.html`**:  
   The HTML template for rendering the user interface. The user interacts with the app by clicking a button to start recording their voice.

- **`static/script.js`**:  
   JavaScript logic to make a POST request to the server when the user clicks the button, sending the speech recognition result to the backend for classification.

---

## **2. Dependencies**

Before running the project, ensure you have the following dependencies installed:

```bash
pip install flask speechrecognition transformers torch

## **How to Run the Project**

### **1. Setup**

1. **Install dependencies**:  
   First, install the necessary Python libraries by running the following command:
   ```bash
   pip install flask speechrecognition transformers torch
### **2. Running the Flask Application**

1. Navigate to the project directory in your terminal.

2. Start the Flask application by running the following command:
   ```bash
   python app.py
