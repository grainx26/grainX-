import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="GrainX — Grain size analysis",
    page_icon="🔬",
    layout="wide",
)

# GrainX is a fully self-contained HTML/CSS/JS app (no server needed),
# so we embed it directly in the page via an iframe-backed component.
html_path = Path(__file__).parent / "GrainX-Fixed.html"
html_content = html_path.read_text(encoding="utf-8")

# Remove Streamlit's default padding so the app fills the viewport nicely
st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header {visibility: hidden;}
        iframe {min-height: 100vh;}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html_content, height=1000, scrolling=True)
