# speech-abuse-detector

1.1 Files Overview
app.py: The main entry point of the application, handles the routing and runs the Flask server. It sets up the / route to serve the front-end interface and /process to handle the speech recognition and classification requests.

detector.py: This file contains the SpeechAbuseDetector class, which encapsulates the logic for:

Capturing audio via microphone.
Converting audio to text using the SpeechRecognition library.
Using a pre-trained model from Hugging Face to classify text as "abusive" or "not abusive".
templates/index.html: The HTML template for rendering the user interface. The user interacts with the app by clicking a button to start recording their voice.

static/script.js: JavaScript logic to make a POST request to the server when the user clicks the button, sending the speech recognition result to the backend for classification.

3. Dependencies
Before running the project, ensure you have the following dependencies installed:

pip install flask speechrecognition transformers torch

Python Libraries
Flask: A lightweight web framework used to build the web interface and APIs.
SpeechRecognition: Used for capturing and transcribing voice input from the user.
Transformers: A library from Hugging Face that provides access to pre-trained models for NLP tasks.
Torch: PyTorch is the deep learning framework used by the transformers library.

4. How to Run the Project
4.1 Setup
Install dependencies: First, install the necessary Python libraries by running the following command:

pip install flask speechrecognition transformers torch

Project structure: Ensure that the project follows the given directory structure. The main Flask application is in app.py, the core logic is in detector.py, and the front-end files are located in the templates and static directories.

4.2 Running the Flask Application
Navigate to the project directory in your terminal.

Start the Flask application:

python app.py
Open your browser and go to:
http://127.0.0.1:5000/

