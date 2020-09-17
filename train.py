import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

#Preprocess the Data
words=[]
classes = []
documents = []
ignore_letters = ['?', '!', ',', '.']
data_file = open('intents.json').read()
intents = json.loads(data_file)
for intent in intents['intents']:
	for pattern in intent['patterns']:
	#tokenize each word
	word = nltk.word_tokenize(pattern)
	words.extend(word)
	#add documents in the corpus
	documents.append((word, intent['tag']))
	# add to our classes list
	if intent['tag'] not in classes:
		classes.append(intent['tag'])
print(documents)

#lemmaztize and lower each word and remove duplicates

words = [lemmatizer.lemmaztize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))

#sort classes

classes = sorted(list(set(classes)))

lbahsjvaskjadjasd
asdasdsa
asdsadasd