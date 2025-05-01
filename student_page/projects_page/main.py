import streamlit as st
import os
import importlib.util

st.set_page_config(page_title="Sayfa ve Menü Sistemi", layout="wide")
st.title("Proje Yönetim Sistemi")

# Varsayılan aktif sayfa
if "active_page" not in st.session_state:
    st.session_state.active_page = "my_tasks"

col1, col2 = st.columns([6, 1])

with col1:
    with st.container(border=True):
        # Butonlar güncellendikten sonra aktif sayfayı yükle
        current_page = st.session_state.active_page
        page_path = f"project_sub_pages/{current_page}.py"

        if os.path.exists(page_path):
            spec = importlib.util.spec_from_file_location(current_page, page_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.render()

with col2:
    with st.container(border=True):
        if st.button("     Görevlerim      ", key="tasks"):
            st.session_state.active_page = "my_tasks"
            st.rerun()  # Sayfayı yeniden yükle
        if st.button("İş yapım aşaması", key="work_in_progress"):
            st.session_state.active_page = "work_in_progress"
            st.rerun()
        if st.button("  Görev   işlemleri ", key="task_operations"):
            st.session_state.active_page = "task_operations"
            st.rerun()
        if st.button("Görev tamamla", key="complete_task"):
            st.session_state.active_page = "complete_task"
            st.rerun()
        if st.button("          Ayarlar           ", key="settings"):
            st.session_state.active_page = "settings"
            st.rerun()