import streamlit as st

def render():
    
    st.title("Ayarlar")

    with st.expander("Proje Ayarları"):
        st.button("Projeden Çık", key="exit_project")