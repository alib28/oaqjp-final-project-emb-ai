import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input, headers=header)
    if response.status_code == 400:
        emotion = {"anger": None, "disgust": None, "fear": None, 
                    "joy": None, "sadness": None, "dominant_emotion":None}
        return emotion
    response_formatted = json.loads(response.text)
    emotions_response = response_formatted['emotionPredictions'][0]['emotion']
    emotions_response['dominant_emotion'] = max(emotions_response, key=emotions_response.get)
    return emotions_response