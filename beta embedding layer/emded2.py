from numpy import array
#from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import one_hot
from declerations import INST

#from keras.models import Sequential
#from declerations import INST
# define documents
docs= INST
#labels = array([1,1,1,1,1,0,0,0,0,0])
# integer encode the documents
vocab_size = len(INST)
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)
# pad documents to a max length of 4 words
