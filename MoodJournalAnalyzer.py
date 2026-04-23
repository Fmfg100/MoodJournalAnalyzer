from textblob import TextBlob
import streamlit as st

st.set_page_config(
    page_title="Mood Journal Analyzer!",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

# --- 1. INITIALIZE SESSION STATE WITH NEW THEME ---
# These match the white/grey theme in your latest image
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
    # Force state back to the White/Grey theme
    st.session_state.bg_p = "#FFFFFF"
    st.session_state.side_p = "#F0F2F6"
    st.session_state.text_p = "#31333F"
    st.session_state.accent_p = "#FF4B4B"
    
    # Clear all text inputs
    for i in range(0, 7):
        st.session_state[f"text{i}"] = ""
    
    st.rerun()

# --- 3. SIDEBAR PICKERS ---
bgcolorpick = st.sidebar.color_picker("• Background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Sidebar", key="side_p")
textcolorpick = st.sidebar.color_picker("• Text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Accent", key="accent_p")

# --- 4. APPLY THE COLORS ---
st.markdown(f"""
    <style>
    /* Main App Background */
    .stApp {{
        background-color: {bgcolorpick};
    }}
    /* Sidebar Background */
    section[data-testid="stSidebar"] {{
        background-color: {sidebgcolorpick} !important;
    }}
    /* Text Colors */
    .stApp, p, h1, h2, h3, label, span {{
        color: {textcolorpick} !important;
    }}
    /* Button Colors */
    button, [data-baseweb="button"] {{
        background-color: {primarycolorpick} !important;
        color: white !important;
    }}
    /* Input field styling to match your screenshot */
    .stTextInput>div>div>input {{
        background-color: #F0F2F6;
        color: #31333F;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. APP CONTENT ---
st.title("📖 Mood Journal Analyzer!")

# Inputs with keys so the reset button can clear them
t0 = st.text_input("Please enter a sentence about your mood in Sunday:", placeholder="How was your day?", key="text0")
t1 = st.text_input("Please enter a sentence about your mood in Monday:", placeholder="How was your day?", key="text1")
t2 = st.text_input("Please enter a sentence about your mood in Tuesday:", placeholder="How was your day?", key="text2")
t3 = st.text_input("Please enter a sentence about your mood in Wednesday:", placeholder="How was your day?", key="text3")
t4 = st.text_input("Please enter a sentence about your mood in Thursday:", placeholder="How was your day?", key="text4")
t5 = st.text_input("Please enter a sentence about your mood in Friday:", placeholder="How was your day?", key="text5")
t6 = st.text_input("Please enter a sentence about your mood in Saturday:", placeholder="How was your day?", key="text6")

# Analysis Logic
all_inputs = [t0, t1, t2, t3, t4, t5, t6]
polarities = []

for t in all_inputs:
    if t:
        b = TextBlob(t)
        pol = b.sentiment.polarity
        polarities.append(pol)
        if pol > 0.1:
            st.write(f"Your day is {pol * 100:.1f}% Positive")
        elif pol < -0.1:
            st.write(f"Your day is {pol * -100:.1f}% Negative")
        else:
            st.write("Your day is Neutral")

# Weekly Summary
if any(all_inputs):
    avg = sum(polarities) / len(polarities) if polarities else 0
    st.title("Your week is")
    if avg > 0.1:
        st.write(f"Positive: {avg * 100:.1f}%")
    elif avg < -0.1:
        st.write(f"Negative: {avg * -100:.1f}%")
    else:
        st.write("Neutral")
