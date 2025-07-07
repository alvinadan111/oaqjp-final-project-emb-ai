import requests
import json


def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Initialize scores and dominant emotion
    anger_score = disgust_score = fear_score = joy_score = sadness_score = None
    dominant_emotion = None

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Check if response is OK
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Extract emotion scores
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        # Build a dictionary of scores
        scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
        }

        # Get the dominant emotion
        dominant_emotion = max(scores, key=scores.get)

    elif response.status_code == 400:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None

    if dominant_emotion == None:
        return "Invalid text! Please try again!"

    # Return all emotions and dominant emotion
    return {
        "emotions": {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
        },
        "dominant_emotion": dominant_emotion,
    }


# in python shell/interpreter using command: python3.11
# 1.) from emotion_detection import emotion_detector
# 2.) emotion_detector("I love this new technology")
