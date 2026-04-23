from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# --- 1. INITIALIZE SESSION STATE ---
if "bg_p" not in st.session_state:
    st.session_state.bg_p = "#0E1117"
if "side_p" not in st.session_state:
    st.session_state.side_p = "#262730"
if "text_p" not in st.session_state:
    st.session_state.text_p = "#FAFAFA"
if "accent_p" not in st.session_state:
    st.session_state.accent_p = "#FF4B4B"

# --- 2. RESET LOGIC ---
if st.sidebar.button("Reset App"):
    # Directly update the widget keys to force the UI to change
    st.session_state.bg_p = "#0E1117"
    st.session_state.side_p = "#262730"
    st.session_state.text_p = "#FAFAFA"
    st.session_state.accent_p = "#FF4B4B"
    
    # Clear text inputs
    for i in range(0, 7):
        key = f"text{i}"
        if key in st.session_state:
            st.session_state[key] = ""
    
    st.rerun()

# --- 3. SIDEBAR PICKERS ---
# Note: value is omitted because it is handled by the 'key' automatically
bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", key="accent_p")

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

t0 = st.text_input("Sunday:", placeholder="How was your day?", key="text0")
t1 = st.text_input("Monday:", placeholder="How was your day?", key="text1")
t2 = st.text_input("Tuesday:", placeholder="How was your day?", key="text2")
t3 = st.text_input("Wednesday:", placeholder="How was your day?", key="text3")
t4 = st.text_input("Thursday:", placeholder="How was your day?", key="text4")
t5 = st.text_input("Friday:", placeholder="How was your day?", key="text5")
t6 = st.text_input("Saturday:", placeholder="How was your day?", key="text6")

# Analysis
all_inputs = [t0, t1, t2, t3, t4, t5, t6]
polarities = []

for t in all_inputs:
    b = TextBlob(t)
    pol = b.sentiment.polarity
    polarities.append(pol)
    if t: # Only write if there is text
        if pol > 0.1:
            st.write(f"Your day is {pol * 100:.1f}% Positive")
        elif pol < -0.1:
            st.write(f"Your day is {pol * -100:.1f}% Negative")
        else:
            st.write("Your day is Neutral")

# Weekly Analysis
if any(all_inputs):
    avg = sum(polarities) / 7
    st.title("Your week is")
    if avg > 0.1:
        st.write(f"Positive: {avg * 100:.1f}%")
    elif avg < -0.1:
        st.write(f"Negative: {avg * -100:.1f}%")
    else:
        st.write("Neutral")
