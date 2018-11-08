from __future__ import print_function
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, LSTM, Dense
import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import CuDNNLSTM
from keras.models import load_model
import pickle
from prettytable import PrettyTable
latent_dim =256# Latent dimensionality of the encoding space.
# Path to the data txt file on disk.
data_path = 'input.txt'

def printtable(dictionary):
    t = PrettyTable(['key', 'value'])
    for key, val in dictionary.items():
        t.add_row([key, val])
    print (t)




input_texts = []

input_characters = set()

with open(data_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
for line in lines:
    input_text= line
    # We use "tab" as the "start sequence" character
    # for the targets, and "\n" as "end sequence" character.
    input_texts.append(input_text)


#load tokenization
pickle_in=open("input_token_index.pickle","rb")
input_token_index=pickle.load(pickle_in)
pickle_in.close()

pickle_in=open("target_token_index.pickle","rb")
target_token_index=pickle.load(pickle_in)
pickle_in.close()

printtable(target_token_index)
printtable(input_token_index)

num_encoder_tokens = len(input_token_index)
num_decoder_tokens = len(target_token_index)

#to do:fix
max_encoder_seq_length =500
max_decoder_seq_length =500


#input to network
encoder_input_data = np.zeros(
    (len(input_texts), max_encoder_seq_length, num_encoder_tokens),
    dtype='float32')
decoder_input_data = np.zeros(
    (len(input_texts), max_decoder_seq_length, num_decoder_tokens),
    dtype='float32')

#tokenization
for i, (input_text) in enumerate(input_texts):
    for t, char in enumerate(input_text):
        encoder_input_data[i, t, input_token_index[char]] = 1.

model=load_model('s2s.h5')

print(model.layers)

