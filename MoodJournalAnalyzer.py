from textblob import TextBlob
import streamlit as st

# Draw a title and some text to the app:


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
