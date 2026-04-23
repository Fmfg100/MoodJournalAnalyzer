from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# 1. Setup Session State for the values
if "bg" not in st.session_state:
    st.session_state.bg = "#0E1117"
if "side" not in st.session_state:
    st.session_state.side = "#262730"
if "text" not in st.session_state:
    st.session_state.text = "#FAFAFA"
if "accent" not in st.session_state:
    st.session_state.accent = "#FF4B4B"

# 2. Reset Button Logic
if st.sidebar.button("Reset App"):
    st.session_state.bg = "#0E1117"
    st.session_state.side = "#262730"
    st.session_state.text = "#FAFAFA"
    st.session_state.accent = "#FF4B4B"
    # Clear text inputs
    for i in range(1, 7):
        st.session_state[f"text{i}"] = ""
    st.rerun()

# 3. Sidebar Pickers - Linked to session_state
bgcolorpick = st.sidebar.color_picker("• Background", st.session_state.bg, key="bg_picker")
sidebgcolorpick = st.sidebar.color_picker("• Sidebar", st.session_state.side, key="side_picker")
textcolorpick = st.sidebar.color_picker("• Text", st.session_state.text, key="text_picker")
primarycolorpick = st.sidebar.color_picker("• Accent", st.session_state.accent, key="accent_picker")

# 4. Apply CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: {bgcolorpick}; }}
    section[data-testid="stSidebar"] {{ background-color: {sidebgcolorpick} !important; }}
    .stApp, p, h1, h2, h3, label, span {{ color: {textcolorpick} !important; }}
    button, [data-baseweb="button"] {{ background-color: {primarycolorpick} !important; }}
    </style>
    """, unsafe_allow_html=True)

# 5. App Content
st.title("📖 Mood Journal Analyzer!")

# Use keys for ALL text inputs so they can be reset
text0 = st.text_input("Sunday:", placeholder="How was your day?", key="text0")
text1 = st.text_input("Monday:", placeholder="How was your day?", key="text1")
text2 = st.text_input("Tuesday:", placeholder="How was your day?", key="text2")
text3 = st.text_input("Wednesday:", placeholder="How was your day?", key="text3")
text4 = st.text_input("Thursday:", placeholder="How was your day?", key="text4")
text5 = st.text_input("Friday:", placeholder="How was your day?", key="text5")
text6 = st.text_input("Saturday:", placeholder="How was your day?", key="text6")

# Analysis Logic
all_texts = [text0, text1, text2, text3, text4, text5, text6]
polarities = []

for t in all_texts:
    b = TextBlob(t)
    p = b.sentiment.polarity
    polarities.append(p)
    if p > 0.1: st.write(f"Positive ({p*100:.1f}%)")
    elif p < -0.1: st.write(f"Negative ({p*-100:.1f}%)")
    else: st.write("Neutral")

avg = sum(polarities) / 7
st.title("Your week is")
if avg > 0.1: st.write(f"Positive: {avg*100:.1f}%")
elif avg < -0.1: st.write(f"Negative: {avg*-100:.1f}%")
else: st.write("Neutral")
