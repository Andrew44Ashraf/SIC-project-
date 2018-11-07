#from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
#from keras import *
from declerations import INST
#import numpy as np 
from numpy import array
#from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import one_hot
#from declerations import INST

#from keras.models import Sequential
#from declerations import INST
# define documents
from keras.models import Sequential
from keras.layers import Dense
#from keras.layers import Flatten
from keras.layers.embeddings import Embedding

docs= INST

# integer encode the documents
vocab_size = len(INST)+15
encoded_docs = [one_hot(d, vocab_size) for d in docs]
#print(encoded_docs)
# pad documents to a max length of 4 words

#from pandas import * 

# e = Embedding(13, 3, input_length=3)
# define documents

tokenizer = Tokenizer()
tokenizer.fit_on_texts(INST)
sequence_of_int = tokenizer.texts_to_sequences(INST)


# integer encode the documents
#vocab_size = 50
#encoded_docs = [one_hot(d, vocab_size) for d in docs]
output = to_categorical(sequence_of_int)
final= array(output)
encoded_docs= array(encoded_docs)


#print(output)
model = Sequential()
model.add(Embedding(vocab_size, 3, input_length= 1))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
# summarize the model
print(model.summary())
# fit the model
model.fit(encoded_docs, final ,epochs=50, verbose=0)

# evaluate the model
loss, accuracy = model.evaluate(encoded_docs, output, verbose=0)
print('Accuracy: %f' % (accuracy*100))

