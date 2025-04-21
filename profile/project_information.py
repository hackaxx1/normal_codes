import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projeler", page_icon="🛠️", layout="centered")

# Örnek veriler
indb_interested_projects = ["Makine Öğrenmesi", "Web Geliştirme"]
if "attended_projects" not in st.session_state:
    st.session_state.attended_projects = [
        {"ad": "Proje 1", "tarih": "2023-01-01", "alan": "Makine Öğrenmesi"},
        {"ad": "Proje 2", "tarih": "2023-02-01", "alan": "Web Geliştirme"},
    ]

# İlgilenilen proje türleri
project_types = ["Makine Öğrenmesi", "Web Geliştirme", "Mobil Uygulama", 
                 "Oyun Geliştirme", "Veri Bilimi", "Yapay Zeka"]
selected_projects = st.multiselect("İlgilendiğin Proje Türleri", project_types, default=indb_interested_projects)

if st.button("Güncelle"):
    st.success("✅ Başarıyla güncellendi!")

# Katılınan Projeler Başlığı
st.markdown("---")
st.subheader("📌 Daha Önce Katılınan Projeler")

# Proje Tablosu
df_projects = pd.DataFrame(st.session_state.attended_projects)
st.dataframe(df_projects, use_container_width=True)

# --- Proje Ekleme Alanı ---
with st.expander("Yeni Proje Ekle ✔"):
    col1, col2, col3 = st.columns(3)
    with col1:
        new_project_name = st.text_input("Proje Adı")
    with col2:
        new_project_date = st.date_input("Tarih")
    with col3:
        new_project_field = st.selectbox("Alan", project_types)

    if st.button("Projeyi Ekle"):
        if new_project_name:
            new_project = {
                "ad": new_project_name,
                "tarih": new_project_date.strftime("%Y-%m-%d"),
                "alan": new_project_field
            }
            st.session_state.attended_projects.append(new_project)
            st.success("✅ Yeni proje eklendi!")
            st.experimental_rerun()
        else:
            st.warning("⚠️ Lütfen proje adını girin.")

# --- Proje Silme Alanı ---
with st.expander("Projeyi Kaldır ❌"):

    # Proje adlarını listeden seçtirme
    project_names = [proj["ad"] for proj in st.session_state.attended_projects]
    selected_to_remove = st.selectbox("Kaldırmak istediğin projeyi seç", [""] + project_names)

    if st.button("Projeyi Kaldır") and selected_to_remove:
        st.session_state.attended_projects = [p for p in st.session_state.attended_projects if p["ad"] != selected_to_remove]
        st.success(f"❌ '{selected_to_remove}' başarıyla kaldırıldı.")
        st.experimental_rerun()
