import speech_recognition as sr
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class SpeechAbuseDetector:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

        # Load model and tokenizer
        model_name_or_path = 'ibm-granite/granite-guardian-hap-38m'
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    def modelwork(self, text):
        """Tokenize the input text and classify it using the model."""
        inputs = self.tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        logits = self.model(**inputs).logits
        prediction = torch.argmax(logits, dim=1).detach().numpy().tolist()  # Binary prediction
        return prediction

    def listen_and_recognize(self):
        """Capture audio from microphone and return recognized text."""
        with sr.Microphone() as source:
            print("Listening for voice input...")
            try:
                audio = self.recognizer.listen(source)
                print("Processing audio...")
                # Convert audio to text
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized text: {text}")
                return text
            except sr.UnknownValueError:
                return "Could not understand the audio."
            except sr.RequestError as e:
                return f"Error with Google Speech Recognition service: {e}"