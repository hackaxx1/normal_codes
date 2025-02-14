import streamlit as st
import importlib.util
import os

class app:
    def get_app(dosyaadi):
        if os.path.exists(dosyaadi):
            spec = importlib.util.spec_from_file_location("module.name", dosyaadi)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'main'):
                module.main()
        else:
            st.error(f"Hata: {dosyaadi} dosyası bulunamadı.")

    def del_app():
        if 'show_app' in st.session_state:
            st.session_state.show_app = False