from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# --- 1. SESSION STATE INITIALIZATION ---
# Using the exact hex codes from your starting screenshots
if "bg_val" not in st.session_state:
    st.session_state.bg_val = "#0E1117"
if "side_val" not in st.session_state:
    st.session_state.side_val = "#262730"
if "text_val" not in st.session_state:
    st.session_state.text_val = "#FAFAFA"
if "accent_val" not in st.session_state:
    st.session_state.accent_val = "#FF4B4B"

# --- 2. SIDEBAR CUSTOMIZATION ---
st.sidebar.title("Theme Customization 🎨")

bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", st.session_state.bg_val, key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", st.session_state.side_val, key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", st.session_state.text_val, key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", st.session_state.accent_val, key="accent_p")

# --- 3. RESET LOGIC ---
if st.sidebar.button("Reset App"):
    # Force colors back to your requested original hex codes
    st.session_state.bg_val = "#0E1117"
    st.session_state.side_val = "#262730"
    st.session_state.text_val = "#FAFAFA"
    st.session_state.accent_val = "#FF4B4B"
    
    # Clear text input keys
    for i in range(1, 7):
        key = f"text{i}"
        if key in st.session_state:
            st.session_state[key] = ""
    
    # Rerun so the pickers pick up the reset session state values
    st.rerun()

# --- 4. APPLY THE COLORS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bgcolorpick};
    }}
    section[data-testid="stSidebar"] {{
        background-color: {sidebgcolorpick} !important;
    }}
    .stApp, p, h1, h2, h3, label, span {{
        color: {textcolorpick} !important;
    }}
    button, [data-baseweb="button"] {{
        background-color: {primarycolorpick} !important;
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. APP CONTENT ---
st.title("📖 Mood Journal Analyzer!")

text = st.text_input("Please enter a sentence about your mood in Sunday: ", placeholder="How was your day?", key="text0")
text1 = st.text_input("Please enter a sentence about your mood in Monday: ", placeholder="How was your day?", key="text1")
text2 = st.text_input("Please enter a sentence about your mood in Tuesday: ", placeholder="How was your day?", key="text2")
text3 = st.text_input("Please enter a sentence about your mood in Wednesday: ", placeholder="How was your day?", key="text3")
text4 = st.text_input("Please enter a sentence about your mood in Thursday: ", placeholder="How was your day?", key="text4")
text5 = st.text_input("Please enter a sentence about your mood in Friday: ", placeholder="How was your day?", key="text5")
text6 = st.text_input("Please enter a sentence about your mood in Saturday: ", placeholder="How was your day?", key="text6")

# Analysis Logic
all_inputs = [text, text1, text2, text3, text4, text5, text6]
polarities = []

for t in all_inputs:
    b = TextBlob(t)
    day = b.sentiment.polarity
    polarities.append(day)
    if day > 0.1:
        st.write(f"Your day is {day * 100:.1f}% Positive")
    elif day < -0.1:
        st.write(f"Your day is {day * -100:.1f}% Negative")
    else:
        st.write("Your day is Neutral")

# Weekly Analysis
sentimentaverage = sum(polarities) / 7

st.title("Your week is")

if sentimentaverage > 0.1:
    st.write(f"Positive: {sentimentaverage * 100:.1f}%")
elif sentimentaverage < -0.1:
    st.write(f"Negative: {sentimentaverage * -100:.1f}%")
else:
    st.write("Neutral")
