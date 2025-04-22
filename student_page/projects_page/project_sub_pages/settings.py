import streamlit as st

def render():
    
    st.subheader("Ayarlar")

    with st.expander("Proje Ayarları"):
        st.button("Projeden Çık", key="exit_project")