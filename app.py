
import streamlit as st
from analyse_prompt import analyse_match, team1, team2

st.title("Analyse automatique des matchs")
st.write("Résultat de l'analyse selon ton prompt final :")
st.text(analyse_match(team1, team2))
