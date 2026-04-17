from textblob import TextBlob
import streamlit as st

# Draw a title and some text to the app:
title = st.title("Mood Journal Analyzer!")

text = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?")
blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0.1:
    st.write("Positive")
elif sentiment >= -0.1:
    st.write("Neutral")
else:
    st.write("Negative")
if sentiment > 0.1:
    st.write(f"Your day is {blob.sentiment.polarity * 100:.1f}%" + " Positive")
if sentiment < -0.1:
    score = sentiment * -100
    st.write(f"Your day is {score:.1f}% Negative")
