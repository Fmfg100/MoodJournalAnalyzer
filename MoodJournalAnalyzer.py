from textblob import TextBlob
import streamlit as st
# Draw a title and some text to the app:
title = st.title("Mood Journal Analyzer!")

text = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?")
text1 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text1")
text2 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text2")
text3 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text3")
text4 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text4")
text5 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text5")
text6 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text6")
blob = TextBlob(text)
blob1 = TextBlob(text1)
blob2 = TextBlob(text2)
blob3 = TextBlob(text3)
blob4 = TextBlob(text4)
blob5 = TextBlob(text5)
blob6 = TextBlob(text6)
sentimentaverage = (blob.sentiment.polarity + blob1.sentiment.polarity + blob2.sentiment.polarity + blob3.sentiment.polarity + blob4.sentiment.polarity + blob5.sentiment.polarity + blob6.sentiment.polarity)
sentiment = sentimentaverage
if sentiment > 0.1:
    st.write("Positive")
elif sentiment >= -0.1:
    st.write("Neutral")
else:
    st.write("Negative")
if sentiment > 0.1:
    st.write(f"Your day is {sentimentaverage * 100:.1f}%" + " Positive")
if sentiment < -0.1:
    score = sentiment * -100
    st.write(f"Your day is {score:.1f}% Negative")
