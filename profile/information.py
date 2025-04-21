import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_modal import Modal

# BU KOMUT EN BAŞTA OLMALI
st.set_page_config(page_title="Profil Kartı", page_icon="👤", layout="centered")

indb_username = "Eymen Taha"
indb_school = "İTÜ"
indb_class = "9. sınıf"
indb_skills = ["Python", "NLP", "Veri Bilimi"]
indb_experience = "1 Kere teknofeste katıldım"

def main():
    profile_image_url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"

    st.markdown(f"""
    <style>
        body {{
            background-color: #0A192F;
        }}
        .profile-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }}
        .profile-card {{
            width: 250px;
            background-color: #112D4E;
            border-radius: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            text-align: center;
        }}
        .profile-image {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #3F72AF;
        }}
        .profile-name {{
            font-size: 18px;
            font-weight: bold;
            color: #DBE2EF;
            margin-top: 20px;
        }}
    </style>
    <div class="profile-container">
        <div class="profile-card">
            <img src="{profile_image_url}" class="profile-image">
            <p class="profile-name">{indb_username}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    colored_header(" ", description="Kullanıcı bilgilerini görüntüleyin", color_name="blue-70")

    new_name = st.text_input("Ad-Soyad", value=indb_username)

    schools = ["ODTÜ", "Boğaziçi", "İTÜ", "Bilkent", "Hacettepe", "Yıldız Teknik"]
    new_school = st.selectbox("Okulunu Seç", schools, index=schools.index(indb_school) if indb_school in schools else 0)

    class_options = ["9. sınıf", "10. sınıf", "11. sınıf", "12. sınıf", "Mezun"]
    new_class = st.selectbox("Sınıfını Seç", class_options, index=class_options.index(indb_class) if indb_class in class_options else 0)

    skills_list = ["Python", "Django", "Streamlit", "Makine Öğrenmesi", "NLP", "Veri Bilimi", "Flutter", "React"]
    new_skills = st.multiselect("Yetenekler", skills_list, default=indb_skills)

    new_experience = st.text_area("Deneyimlerini Yaz", value=indb_experience)

    if st.button("Profili Güncelle"):
        st.success("✅ Profil başarıyla güncellendi!")

if __name__ == "__main__":
    main()
