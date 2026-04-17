from textblob import TextBlob
import streamlit as st

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

text = st.text_input("Please enter a sentance about your day: ", placeholder="How was your day?")
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0.1:
    print("Positive")
elif sentiment >= -0.1:
    print("Neutral")
else:
    print("Negative")
if sentiment > 0.1:
    print(f"your day is {blob.sentiment.polarity * 100:.1f}%" + " Positive")
if sentiment < -0.1:
    score = sentiment * -100
    print(f"your day is {score:.1f}% Negative")
