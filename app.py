from flask import Flask, render_template, request, jsonify
from detector import SpeechAbuseDetector

class FlaskApp:
    def __init__(self):
        # Initialize Flask app
        self.app = Flask(__name__)
        self.detector = SpeechAbuseDetector()

        # Set up Flask routes
        self.setup_routes()

    def setup_routes(self):
        """Define the routes for the Flask app."""
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/process', methods=['POST'])
        def process():
            """Process the speech recognition and classify the text."""
            if request.method == 'POST':
                recognized_text = self.detector.listen_and_recognize()
                if "Error" in recognized_text or "Could not" in recognized_text:
                    return jsonify({'text': recognized_text, 'classification': 'Error processing audio'})

                # Classify the recognized text
                prediction = self.detector.modelwork(recognized_text)
                classification = "abusive" if prediction == [1] else "not abusive"

                return jsonify({'text': recognized_text, 'classification': classification})

    def run(self):
        """Run the Flask app."""
        self.app.run(debug=True)

if __name__ == "__main__":
    app = FlaskApp()
    app.run()