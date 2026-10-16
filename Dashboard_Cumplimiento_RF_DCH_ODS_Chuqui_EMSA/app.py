from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dashboard Cumplimiento RF DCH | EMSA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
HTML_FILE = ROOT / "dashboard.html"

st.markdown(
    """
    <style>
      .block-container {padding-top: 0.5rem; padding-bottom: 0.5rem; max-width: 100%;}
      header[data-testid="stHeader"] {height: 0rem;}
      footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.exists():
    st.error("No se encontró dashboard.html en el repositorio.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")
# El HTML contiene su propia cabecera, estilos y lógica interactiva.
# La planilla se selecciona desde el botón "Actualizar información" del dashboard
# y se procesa en el navegador, sin guardar los datos cargados en el servidor.
components.html(html, height=1800, scrolling=True)
