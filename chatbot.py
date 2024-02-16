import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json', encoding="utf8").read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words (sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class (sentence):
    bow = bag_of_words (sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice (i['responses'])
            break
    return result

print("GO! Bot is running!")

def solveEq(arr):
    if(len(arr) == 2):
        a = float(arr[0])
        b = float(arr[1])
        if(a == 0 and b != 0):
            print("Phương trình vô nghiệm")
        elif(a == 0 and b == 0):
            print("Phương trình vô số nghiệm")
        else:
            print("Giá trị của biểu thức là %f" % (-b/a))
    elif(len(arr) == 3):
        a = float(arr[0])
        b = float(arr[1])     
        c = float(arr[2])
        delta = pow(b,2) - 4*a*c
        if(a == 0):
            print("Phương trình được cho không phải bậc 2, hãy thử lại sau")
        elif():
    

while True:
    message = input("")
    ints = predict_class (message)
    res = get_response (ints, intents)
    
    res = res.split("**")


    if len(res) > 1:

        numerical_input = []

        for i in range(len(res)):
            temp = input(res[i])
            numerical_input.append(temp)
    
        solveEq(numerical_input)

    else: 
        print (res[0])

    