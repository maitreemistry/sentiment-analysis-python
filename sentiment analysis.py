import nltk
from textblob import TextBlob
import pyautogui as pg
n=pg.prompt(text="Enter the number of Entries", title='Sentiment Analysis', default='')
inputtext=[]
for i in range(0,int(n)):
     x=pg.prompt(text='Enter your Text', title='Sentiment Analysis', default='')
     inputtext.append(x)
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
for words in inputtext:
  scores = sia.polarity_scores(words)
  print(words,":")
  print("Positive =",scores['pos']*100, "%","Neutral =",scores['neu']*100, "%","Negative =",scores['neg']*100, "%","Compound =",scores['compound'])
  print(" ")
 

