import json
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
import datetime
from news_data import news_search
import billboard
import time
from pygame import mixer
from search import search_internet
from weather import weather_data

import random
import pickle


with open('intents.json') as file:
    data = json.load(file)
labels = pickle.load(open('labels.pkl','rb'))


# load trained model
model = load_model('my_model.h5')

# load tokenizer
with open('tokenizer.pickle', 'rb') as token:
        tokenizer = pickle.load(token)
        
# load label encoder
with open('label_encoder.pickle', 'rb') as enc:
    label_enc = pickle.load(enc)
    
max_len = 20    


def predict_label(x):
    result = model.predict(pad_sequences(tokenizer.texts_to_sequences([x]),
                                         truncating='post', maxlen = max_len))
    tag = label_enc.inverse_transform([np.argmax(result)])
    return tag    


def getting_response(data, tag):
    
    intent_list = data['intents']
    
    if tag == 'time':
        print(time.strftime("%H:%M"))
        
    if tag == 'date':
        print(time.strftime("%A %d %B %Y"))
    
    if tag == 'google':
        # to search
        search_internet.search_google(data)
        
    if tag=='news':
        print(news_search.news())
        
    
    if tag=='song':
        chart = billboard.ChartData('hot-100')
        print('The top 10 songs at the moment are:')
        for i in range(10):
            song = chart[i]
            print(song.title,'- ',song.artist)
    
    if tag=='timer':        
        mixer.init()
        x = input('min: ')
        y = input('sec: ')
        time.sleep(float(x)*60+int(y))
        mixer.music.load('Handbell-ringing-sound-effect.mp3')
        mixer.music.play()
    
    if tag=="weather":
        weather_data.weather()
    
    if tag=="wikipedia":
        search_internet.wiki_summary(data)
    
    
    for i in intent_list:
        if tag == i['tag']:
            result = random.choice(i['responses'])
    return result
        

def chat():
    print("Initiating 'SAM' \nStart messaging with the bot (Type: 'bye' or 'quit' or 'exit' to terminate)")
    while True:
        user_input = input("You: ")
        tag = predict_label(user_input)
        if tag == 'goodbye':
            break
        print('Sam: ',end = '')
        print(getting_response(data, tag))
                 
chat()