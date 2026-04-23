initial_sidebar_state="collapsed"
)

# --- 1. RESET FUNCTION (The only way to avoid the crash) ---
# --- 1. RESET FUNCTION (Sets the EXACT colors from your screenshots) ---
def reset_everything():
    st.session_state.bg_p = "#0e1117"
    st.session_state.bg_p = "#0E1117"
st.session_state.side_p = "#262730"
    st.session_state.text_p = "#fafafa"
    st.session_state.accent_p = "#ff4b4b"
    st.session_state.text_p = "#FAFAFA"
    st.session_state.accent_p = "#FF4B4B"
    # Clear all text inputs
for i in range(0, 7):
k = "text" if i == 0 else f"text{i}"
st.session_state[k] = ""

# --- 2. INITIALIZE COLORS ---
# --- 2. INITIALIZE SESSION STATE ---
if "bg_p" not in st.session_state:
    st.session_state.bg_p = "#0e1117"
    st.session_state.bg_p = "#0E1117"
if "side_p" not in st.session_state:
st.session_state.side_p = "#262730"
if "text_p" not in st.session_state:
    st.session_state.text_p = "#fafafa"
    st.session_state.text_p = "#FAFAFA"
if "accent_p" not in st.session_state:
    st.session_state.accent_p = "#ff4b4b"
    st.session_state.accent_p = "#FF4B4B"

# --- 3. SIDEBAR ---
st.sidebar.title("Theme Customization 🎨")
bgcolorpick = st.sidebar.color_picker("• Background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Sidebar", key="side_p")
textcolorpick = st.sidebar.color_picker("• Text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Accent", key="accent_p")
bgcolorpick = st.sidebar.color_picker("• Choose a color for your background", key="bg_p")
sidebgcolorpick = st.sidebar.color_picker("• Choose a color for your sidebar background", key="side_p")
textcolorpick = st.sidebar.color_picker("• Choose a color for the text", key="text_p")
primarycolorpick = st.sidebar.color_picker("• Choose an accent color", key="accent_p")

# The button calls the function above
# Reset Button using the callback to prevent the crash
st.sidebar.button("Reset App", on_click=reset_everything)

# --- 4. APPLY COLORS ---
# --- 4. APPLY THE COLORS ---
st.markdown(f"""
   <style>
   .stApp {{ background-color: {bgcolorpick}; }}
