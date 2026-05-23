"""Flask web app for emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_detector():
    """Run emotion detection and return a formatted response string."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
