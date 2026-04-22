from textblob import TextBlob
import streamlit as st
st.set_page_config(
    page_title="Mood Journal Analyzer" ,
    page_icon="📖"
)
# Draw a title and some text to the app:
title = st.title("📖 Mood Journal Analyzer!")

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

# --- DAILY ANALYSIS SECTION ---
# This part handles the "Your day is..." for every input
all_blobs_together = [blob, blob1, blob2, blob3, blob4, blob5, blob6]

for b in all_blobs_together:
    day = b.sentiment.polarity
    # Very simple if conditions
    if day > 0.1:
        st.write(f"Your day is {day * 100:.1f}% Positive")
    elif day < -0.1:
        st.write(f"Your day is {day * -100:.1f}% Negative")
    else:
        st.write("Your day is Neutral")

# --- WEEKLY ANALYSIS SECTION ---
sentimentaverage = (blob.sentiment.polarity + blob1.sentiment.polarity + blob2.sentiment.polarity + blob3.sentiment.polarity + blob4.sentiment.polarity + blob5.sentiment.polarity + blob6.sentiment.polarity) / 7

st.title("Your week is")

# Simplified Weekly Logic
if sentimentaverage > 0.1:
    st.write(f"Positive: {sentimentaverage * 100:.1f}%")
elif sentimentaverage < -0.1:
    st.write(f"Negative: {sentimentaverage * -100:.1f}%")
else:
    st.write("Neutral")
