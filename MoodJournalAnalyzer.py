from textblob import TextBlob
import streamlit as st
# Draw a title and some text to the app:
title = st.title("Mood Journal Analyzer!")
counter = 0
def changed():
    global counter 
    counter += 1
    print("changed!")
    if counter == 7:
        if sentiment > 0.1:
            st.write("Positive")
        elif sentiment >= -0.1:
            st.write("Neutral")
        else:
            st.write("Negative")
        if sentiment > 0.1:
            st.write(f"Your week is {sentimentaverage * 100:.1f}%" + " Positive")
        if sentiment < -0.1:
            score = sentiment * -100
        st.write(f"Your week is {score:.1f}% Negative")
        counter = 0
def day(blob, daynumber)
    if blob > 0.1:
        st.write(f"Your " + daynumber + " day is {blob * 100:.1f}%" + " Positive")
    if blob < -0.1:
        score = blob * -100
        st.write(f"Your " + daynumber + " day is {score:.1f}% Negative")
text = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", on_change=changed, args=day)
blob = TextBlob(text)
text1 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text1", on_change=changed)
blob1 = TextBlob(text1)
text2 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text2", on_change=changed)
blob2 = TextBlob(text2)
text3 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text3", on_change=changed)
blob3 = TextBlob(text3)
text4 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text4", on_change=changed)
blob4 = TextBlob(text4)
text5 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text5", on_change=changed)
blob5 = TextBlob(text5)
text6 = st.text_input("Please enter a sentence about your day: ", placeholder="How was your day?", key="text6", on_change=changed)
blob6 = TextBlob(text6)
sentimentaverage = (blob.sentiment.polarity + blob1.sentiment.polarity + blob2.sentiment.polarity + blob3.sentiment.polarity + blob4.sentiment.polarity + blob5.sentiment.polarity + blob6.sentiment.polarity) / 7
sentiment = sentimentaverage
if sentiment > 0.1:
    st.write("Positive")
elif sentiment >= -0.1:
    st.write("Neutral")
else:
    st.write("Negative")
if sentiment > 0.1:
    st.write(f"Your week so far is {sentimentaverage * 100:.1f}%" + " Positive")
if sentiment < -0.1:
    score = sentiment * -100
    st.write(f"Your week so far is {score:.1f}% Negative")
sentiment = sentimentaverage
title = st.title("Your week is ")
sentiment = sentimentaverage

