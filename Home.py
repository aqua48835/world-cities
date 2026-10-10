import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main-title {
        font-size: 3em;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 20px;
    }
    .welcome-text {
        font-size: 1.2em;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-title">🌍 World Cities Explorer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="welcome-text">Welcome to the World Cities Application! '
    'Explore cities from around the globe.</div>',
    unsafe_allow_html=True
)

# Divider
st.divider()

# Description section
st.markdown("### About This App")
st.write(
    "This application provides an interactive way to explore and analyze information "
    "about cities worldwide. Use the navigation menu on the left to access different features."
)

# Features section
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### 🗺️ Explore")
    st.write("Browse and discover cities around the world")

with col2:
    st.markdown("#### 📊 Analyze")
    st.write("View detailed statistics and data about cities")

with col3:
    st.markdown("#### 🔍 Search")
    st.write("Find specific cities and their information")

# Divider
st.divider()

# Call to action
st.markdown("### Get Started")
col1, col2 = st.columns([2, 1])

with col1:
    st.write("Click the button below to navigate to the main application:")

with col2:
    if st.button("📱 Go to App", use_container_width=True, key="go_to_app"):
        st.switch_page("pages/app.py")

# Footer
st.divider()
st.markdown(
    "<p style='text-align: center; color: #999; font-size: 0.9em;'>"
    "World Cities App © 2026 | Powered by Streamlit</p>",
    unsafe_allow_html=True
)
