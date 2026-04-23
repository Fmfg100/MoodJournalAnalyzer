from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# --- 1. INITIALIZE SESSION STATE WITH WHITE/GREY THEME ---
if "bg_p" not in st.session_state:
    st.session_state.bg_p = "#FFFFFF"
if "side_p" not in st.session_state:
    st.session_state.side_p = "#F0F2F6"
if "text_p" not in st.session_state:
    st.session_state.text_p = "#31333F"
if "accent_p" not in st.session_state:
    st.session_state.accent_p = "#FF4B4B"

# --- 2. RESET LOGIC ---
if st.sidebar.button("Reset App"):
    # Updated these to reset to the White/Grey colors you wanted
    st.session_state.bg_p = "#FFFFFF"
    st.session_state.side_p = "#F0F2F6"
    st.session_state.text_p = "#31333F"
    st.session_state.accent_p = "#FF4B4B"
    
    # Reset all text inputs (0 through 6)
    for i in range(0, 7):
        key = f"text{i}"
        if key in st.session_state:
            st.session_state[key] = ""
    st.rerun()

# --- 3. SIDEBAR PICKERS ---
bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", key="accent_p")

# --- 4. APPLY COLORS ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: {bgcolorpick}; }}
    section[data-testid="stSidebar"] {{ background-color: {sidebgcolorpick} !important; }}
    .stApp, p, h1, h2, h3, label, span {{ color: {textcolorpick} !important; }}
    button, [data-baseweb="button"] {{ background-color: {primarycolorpick} !important; color: white !important; }}
    /* Input field styling */
    .stTextInput>div>div>input {{
        background-color: #F0F2F6;
        color: #31333F;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. APP CONTENT ---
st.title(" Mood Journal Analyzer!")

text = st.text_input("Please enter a sentence about your mood in Sunday: ", placeholder="How was your day?", key="text0")
text1 = st.text_input("Please enter a sentence about your mood in Monday: ", placeholder="How was your day?", key="text1")
text2 = st.text_input("Please enter a sentence about your mood in Tuesday: ", placeholder="How was your day?", key="text2")
text3 = st.text_input("Please enter a sentence about your mood in Wednesday: ", placeholder="How was your day?", key="text3")
text4 = st.text_input("Please enter a sentence about your mood in Thursday: ", placeholder="How was your day?", key="text4")
text5 = st.text_input("Please enter a sentence about your mood in Friday: ", placeholder="How was your day?", key="text5")
text6 = st.text_input("Please enter a sentence about your mood in Saturday: ", placeholder="How was your day?", key="text6")

# Analysis Logic
all_inputs = [text, text1, text2, text3, text4, text5, text6]
all_blobs = [TextBlob(t) for t in all_inputs]

for i, b in enumerate(all_blobs):
    if all_inputs[i]: # Only analyze if user typed something
        day = b.sentiment.polarity
        if day > 0.1:
            st.write(f"Your day is {day * 100:.1f}% Positive")
        elif day < -0.1:
            st.write(f"Your day is {day * -100:.1f}% Negative")
        else:
            st.write("Your day is Neutral")

# Weekly Analysis
if any(all_inputs):
    sentimentaverage = sum([b.sentiment.polarity for b in all_blobs]) / 7
    st.title("Your week is")
    if sentimentaverage > 0.1:
        st.write(f"Positive: {sentimentaverage * 100:.1f}%")
    elif sentimentaverage < -0.1:
        st.write(f"Negative: {sentimentaverage * -100:.1f}%")
    else:
        st.write("Neutral")
