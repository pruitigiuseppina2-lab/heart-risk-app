import streamlit as st

st.title("📄 Report")
st.write(
    """
    Qui verrà generato un **riepilogo** scaricabile dei risultati:
    - input inseriti,
    - percentuale ed esito,
    - data/ora e versione del modello.

    
    """
)

from ui import render_footer
render_footer("Giuseppina Pruiti", None, "https://github.com/pruitigiuseppina2-lab/heart-risk-app")