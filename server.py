"""
Flask web app for emotion detection
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion():
    """Returns emotion detection result"""
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        message = "<b>Invalid text! Please try again!</b>"
        return message
    message = "For the given statement, the system response is 'anger': " \
    f"{result['anger']}, 'disgust': {result['disgust']}, 'joy': {result['joy']}" \
    f" and 'sadness': {result['sadness']}." \
    f" The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    return message

@app.route("/")
def index():
    """Returns default index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    