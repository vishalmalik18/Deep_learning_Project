import numpy as np
import pickle
from keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
# from keras.preprocessing.text import Tokenizer
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from keras.models import load_model

__model = None

def load_saved_artificats():
    global __model
    if __model is None:
        model_path = "C:/Users/visha/Fake News Detection/model.h5"
        __model = load_model(model_path)

def Fake_news_detecation(message):
    voc_size = 5000
    ps = PorterStemmer()
    corpus = []
    for i in range(0,len(message)):
        review = re.sub('[^a-zA-Z]', ' ', message[i])
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        corpus.append(review)
    # print(corpus)

    onehot_repr = [one_hot(words,voc_size) for words in corpus]
    # print(onehot_repr)

    sent_length = 20
    embedded_docs = pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
    # print(embedded_docs)

    result = __model.predict(embedded_docs)

    return result
    # print(result)
    # threshold = 0.5
    # y_pred_class = np.where(result >threshold,1,0)
    # print(y_pred_class)

    #///////////////
    # sent_length = 20
    # tokenizer = Tokenizer()
    # tokenizer.fit_on_texts(message)
    # sequences = tokenizer.texts_to_sequences(message)
    # max_sequence_length = sent_length
    # max_sequence_length = sent_length  
    # padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
    # result = __model.predict(padded_sequences)
    # threshold = 0.5
    # y_pred_class = np.where(result >threshold,1,0)

    # print(y_pred_class)




if __name__ == '__main__':
    load_saved_artificats()
    Fake_news_detecation(message=['Russian Researchers Discover Secret Nazi Military Base â€˜Treasure Hunterâ€™ in the Arctic [Photos]'])
