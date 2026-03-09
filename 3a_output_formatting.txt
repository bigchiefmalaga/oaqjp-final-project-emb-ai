import json
import requests

def emotion_detector(text_to_analyse):
    # Votre API emotion
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    texta = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = texta, headers=headers)
    response_dic = json.loads(response.text)
    emotion = response_dic['emotionPredictions'][0]['emotion']
    emotion_sort = dict(sorted(emotion.items()))
    emotion_max = max(emotion, key = emotion.get)
    emotion_sort['dominant_emotion'] = emotion_max
    return emotion_sort