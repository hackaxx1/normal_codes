import streamlit as st

indb_username = "Eymen Taha"
indb_school = "İTÜ"
indb_class = "9. sınıf"
indb_skills = ["Python", "NLP", "Veri Bilimi"]
indb_experience = "1 Kere teknofeste katıldım"
indb_password = "1234"

new_name = st.text_input("Ad-Soyad", value=indb_username)

# Okul Seçimi
schools = ["ODTÜ", "Boğaziçi", "İTÜ", "Bilkent", "Hacettepe", "Yıldız Teknik"]
new_school = st.selectbox("Okulunu Seç", schools, index=schools.index(indb_school) if indb_school in schools else 0)

# Sınıf seçimi (Radio Button - Tek seçim)
class_options = ["9. sınıf", "10. sınıf", "11. sınıf", "12. sınıf", "Mezun"]
new_class = st.selectbox("Sınıfını Seç", class_options, index=class_options.index(indb_class) if indb_class in class_options else 0)

# Yetenekler
skills_list = ["Python", "Django", "Streamlit", "Makine Öğrenmesi", "NLP", "Veri Bilimi", "Flutter", "React"]
new_skills = st.multiselect("Yetenekler", skills_list, default=indb_skills)

# Deneyimler
new_experience = st.text_area("Deneyimlerini Yaz", value=indb_experience)

# **Güncelle Butonu**
if st.button("Profili Güncelle"):
    st.success("✅ Profil başarıyla güncellendi!")  # Gerçek bir güncelleme için burada veri kaydetme işlemi yapılabilir.