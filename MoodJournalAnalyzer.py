from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    initial_sidebar_state="collapsed"
)

def reset_everything():
    st.session_state.bg_p = "#0e1117"
    st.session_state.side_p = "#262730"
    st.session_state.text_p = "#fafafa"
    st.session_state.accent_p = "#FF4B4B"
 
    for i in range(0, 7):
        k = "text" if i == 0 else f"text{i}"
        st.session_state[k] = ""

def Light_Mode():
    st.session_state.bg_p = "#FFFFFF"
    st.session_state.side_p = "#F0F2F6"
    st.session_state.text_p = "#262730"
    st.session_state.accent_p = "#FF4B4B"
 
    for i in range(0, 7):
        k = "text" if i == 0 else f"text{i}"
        st.session_state[k] = ""
        
if "bg_p" not in st.session_state:
    st.session_state.bg_p = "#0e1117"
if "side_p" not in st.session_state:
    st.session_state.side_p = "#262730"
if "text_p" not in st.session_state:
    st.session_state.text_p = "#fafafa"
if "accent_p" not in st.session_state:
    st.session_state.accent_p = "#FF4B4B"

# --- 3. SIDEBAR ---
st.sidebar.title("Theme Customization 🎨")
bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", key="accent_p")


st.sidebar.button("Dark Mode Default Theme", on_click=reset_everything)
st.sidebar.button("Light Mode Default Theme", on_click=Light_Mode)
    

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bgcolorpick}; }}
    section[data-testid="stSidebar"] {{ background-color: {sidebgcolorpick} !important; }}
    .stApp, p, h1, h2, h3, span {{ color: {textcolorpick} !important; }}
    button, [data-baseweb="button"] {{ 
        background-color: {primarycolorpick} !important; 
        color: white !important; 
    }}
    /* Keeps input fields light grey as seen in your screenshot */
    .stTextInput>div>div>input {{
        background-color: #F0F2F6 !important;
        color: #31333F !important;
    }}
    </style>
    """, unsafe_allow_html=True)


st.title(" Mood Journal Analyzer!")

text = st.text_input("Please enter a sentence about your mood in Sunday: ", placeholder="How was your day?", key="text")
text1 = st.text_input("Please enter a sentence about your mood in Monday: ", placeholder="How was your day?", key="text1")
text2 = st.text_input("Please enter a sentence about your mood in Tuesday: ", placeholder="How was your day?", key="text2")
text3 = st.text_input("Please enter a sentence about your mood in Wednesday: ", placeholder="How was your day?", key="text3")
text4 = st.text_input("Please enter a sentence about your mood in Thursday: ", placeholder="How was your day?", key="text4")
text5 = st.text_input("Please enter a sentence about your mood in Friday: ", placeholder="How was your day?", key="text5")
text6 = st.text_input("Please enter a sentence about your mood in Saturday: ", placeholder="How was your day?", key="text6")

blob = TextBlob(text)
blob1 = TextBlob(text1)
blob2 = TextBlob(text2)
blob3 = TextBlob(text3)
blob4 = TextBlob(text4)
blob5 = TextBlob(text5)
blob6 = TextBlob(text6)

all_blobs_together = [blob, blob1, blob2, blob3, blob4, blob5, blob6]

for b in all_blobs_together:
    day = b.sentiment.polarity
    if day > 0.1:
        st.write(f"Your day is {day * 100:.1f}% Positive")
    elif day < -0.1:
        st.write(f"Your day is {day * -100:.1f}% Negative")
    else:
        st.write("Your day is Neutral")

sentimentaverage = (blob.sentiment.polarity + blob1.sentiment.polarity + blob2.sentiment.polarity + blob3.sentiment.polarity + blob4.sentiment.polarity + blob5.sentiment.polarity + blob6.sentiment.polarity) / 7

st.title("Your week is")
if sentimentaverage > 0.1:
    st.write(f"Positive: {sentimentaverage * 100:.1f}%")
    st.audio("lemonmusiclab-happy-kids-516337.mp3", format="audio/mpeg")
 st.sidebar.button("audio", on_click=Light_Mode)("audio-Happy")
elif sentimentaverage < -0.1:
    st.write(f"Negative: {sentimentaverage * -100:.1f}%")
    st.write(f"Positive: {sentimentaverage * 100:.1f}%")
else:
    st.write("Neutral")
