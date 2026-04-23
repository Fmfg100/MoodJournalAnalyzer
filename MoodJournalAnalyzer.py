from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# --- 1. THE RESET FUNCTION ---
def reset_everything():
    # These are the dark theme hex codes from your original screenshots
    st.session_state.bg_p = "#0E1117"
    st.session_state.side_p = "#262730"
    st.session_state.text_p = "#FAFAFA"
    st.session_state.accent_p = "#FF4B4B"
    # Clear all text inputs
    for i in range(0, 7):
        k = "text" if i == 0 else f"text{i}"
        st.session_state[k] = ""

# --- 2. INITIALIZE SESSION STATE ---
if "bg_p" not in st.session_state:
    st.session_state.bg_p = "#0E1117"
if "side_p" not in st.session_state:
    st.session_state.side_p = "#262730"
if "text_p" not in st.session_state:
    st.session_state.text_p = "#FAFAFA"
if "accent_p" not in st.session_state:
    st.session_state.accent_p = "#FF4B4B"

# --- 3. SIDEBAR ---
st.sidebar.title("Theme Customization 🎨")
bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", key="accent_p")

# Reset Button using the callback to prevent the crash
st.sidebar.button("Reset App", on_click=reset_everything)

# --- 4. APPLY THE COLORS (Includes Input Styling) ---
st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{ background-color: {bgcolorpick}; }}
    
    /* Sidebar */
    section[data-testid="stSidebar"] {{ background-color: {sidebgcolorpick} !important; }}
    
    /* Global Text */
    .stApp, p, h1, h2, h3, label, span {{ color: {textcolorpick} !important; }}
    
    /* Buttons */
    button, [data-baseweb="button"] {{ 
        background-color: {primarycolorpick} !important; 
        color: white !important; 
    }}
    
    /* Fix for Text Inputs to match the dark theme */
    .stTextInput>div>div>input {{
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border: 1px solid #4B4B4B !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. YOUR ORIGINAL CONTENT ---
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
elif sentimentaverage < -0.1:
    st.write(f"Negative: {sentimentaverage * -100:.1f}%")
else:
    st.write("Neutral")
