import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        formatted_response = formatted_response['emotionPredictions'][0]['emotion']
        emotions_list = list(formatted_response.keys())
        scores_list = list(formatted_response.values())
        dominant_emotion_score = max(scores_list)
        ind = scores_list.index(dominant_emotion_score)
        dominant_emotion = emotions_list[ind]
        formatted_response['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        formatted_response = None
    
    return formatted_response