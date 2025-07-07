"""Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

# Import Flask, render_template, request from the flask pramework package : TODO
# Import the emotion_detector function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
# Initiate the flask app : TODO


@app.route("/emotionDetector")
def sent_analyzer():
    """Retrieve the text to analyze from the request arguments"""
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and dominant_emotion from the response
    emotions = response["emotions"]
    dominant_emotion = response["dominant_emotion"]

    emotion_scores = ""
    for emotion, score in emotions.items():
        emotion_scores += f"{emotion}: {score}\n"

    # Handle invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Return a summary string
    return (
        f"Emotion scores: \n"
        f"{emotion_scores}"
        f"For the given statement, the system response is: "
        f"{dominant_emotion} with a score of {emotions[dominant_emotion]}."
    )


@app.route("/")
def render_index_page():
    """Home"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

# python3.11 server.py
