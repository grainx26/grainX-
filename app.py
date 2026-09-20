"""
GrainX — Streamlit wrapper
--------------------------
GrainX is a fully client-side app (HTML + CSS + JS). All image processing
happens in the visitor's browser, so this wrapper only needs to serve the
HTML file inside Streamlit. No uploaded micrograph ever reaches the server.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# --- Page config must be the first Streamlit call -------------------------
st.set_page_config(
    page_title="GrainX — Grain size analysis",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Strip Streamlit chrome so the app fills the page ---------------------
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] { display: none !important; }

      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      section.main > div { padding: 0 !important; }

      /* Make the iframe fill the viewport */
      iframe[title="streamlit.components.v1.html"] {
        width: 100%;
        height: 100vh;
        border: 0;
        display: block;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Load and serve the HTML ----------------------------------------------
HTML_PATH = Path(__file__).parent / "GrainX-Fixed.html"


@st.cache_data(show_spinner=False)
def load_html(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


html = load_html(str(HTML_PATH))

# Height is a fixed pixel value because components.html can't read the
# parent viewport. 950 suits most laptop/desktop screens; the app itself
# scrolls internally if the window is shorter.
components.html(html, height=950, scrolling=True)
