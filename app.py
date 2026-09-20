import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="GrainX", page_icon="🔬", layout="wide")

# Remove Streamlit's default padding so the embedded app can use the full page
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { background: transparent; }
        #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "GrainX-Final-2.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1200, scrolling=True)
