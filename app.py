import streamlit as st
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('punkt_tab')


def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)
      text=y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text=y[:]
  y.clear()
  ps=PorterStemmer()
  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)


tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_text=st.text_area("paste your message")
if st.button('Pridict'):
  #1 preprocess
  transformed_sms =transform_text(input_text)
  #2 vectorize
  vector_input=tfidf.transform([transformed_sms])
  #3 pridict
  result=model.predict(vector_input).tolist()
  #4 Display
  for i in result:
    if i==1:
      st.header('spam')
    else:
      st.header("Not Spam")
  #print(result)

