import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# açan kişi ve kimin profili olduğu bilgisi BURASI TESTİNGDE DEĞİŞEBİLİR !!!!
opening_person_user_id = 1
whos_profile_user_id = 2

# 📌 Varsayılan (DB'den çekilmiş gibi davranan) değişkenler - İlk değerler
indb_username = "Eymen Taha"
indb_school = "İTÜ"
indb_class = "9. sınıf"
indb_skills = ["Python", "NLP", "Veri Bilimi"]
indb_experience = "1 Kere teknofeste katıldım"
indb_password = "1234"
indb_interested_projects = ["Makine Öğrenmesi", "Web Geliştirme"]
indb_attended_projects_list = ["teknofest 2021 makine öğrenmesi", "tübitak 4000B yapay zeka"]

# 📌 Sayfa Başlığı
st.title("🔹 Kişisel Profil Sayfası")

if opening_person_user_id == whos_profile_user_id:
    # Eğer giriş yapan kişi, profil sahibiyle aynıysa (kendi profiline giriş yapıyorsa)
    
    with st.expander("📌 Projelerle Alakalı Bilgiler"):

        # Kullanıcının ilgilendiği proje türlerini seçebileceği alan
        project_types = ["Makine Öğrenmesi", "Web Geliştirme", "Mobil Uygulama", 
                         "Oyun Geliştirme", "Veri Bilimi", "Yapay Zeka"]
        selected_projects = st.multiselect("İlgilendiğin Proje Türleri", project_types, default=indb_interested_projects)

        # **Güncelle Butonu**
        if st.button("Güncelle"):
            st.success("✅ başarıyla güncellendi!")  # Gerçek bir güncelleme için burada veri kaydetme işlemi yapılabilir.

        # Başlık
        st.write("Daha önce katılınan projeler")

        # CSS kodu
        css_code = """
            <style>
                .scrollable-container {
                    height: 300px;
                    overflow-y: scroll;
                    border: 2px solid #000000;  /* Kaydırılabilir alanın kenarlık rengi */
                    padding: 10px;
                    background-color: #3b2121;  /* Arka plan rengi */
                    border-radius: 15px;  /* Kenarları bombeli yapmak için */
                }
                .item {
                    padding: 10px;
                    margin: 5px;
                    border: 2px solid #000000;  /* Her öğenin kenarlık rengi */
                    border-radius: 5px;
                    background-color: #181616;  /* Kutuların arka plan rengi */
                    color: #acacac;  /* Yazı rengi */
                    font-size: 16px;  /* Yazı boyutu */
                    font-family: 'Arial', sans-serif;  /* Yazı fontu */
                }
                .item:hover {
                    background-color: #3a303080;  /* Üzerine gelince kutu rengi değişir */
                }
            </style>
        """

        # HTML içeriği dinamik olarak oluşturuluyor
        html_content = '<div class="scrollable-container">'
        for item in indb_attended_projects_list:
            html_content += f'<div class="item">{item}</div>'
        html_content += '</div>'

        # HTML ve CSS içeriğini Streamlit'te göster
        st.markdown(css_code + html_content, unsafe_allow_html=True)

        st.write("")

    # 📌 Kullanıcı Bilgileri
    with st.expander("📌 Kişisel Bilgiler ve İlgi Alanları"):
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

    # 📌 Şifre Değiştirme Alanı
    with st.expander("🔑 Şifre Değiştir"):
        old_password = st.text_input("Eski Şifre", type="password")
        new_password = st.text_input("Yeni Şifre", type="password")
        if st.button("Şifreyi Güncelle"):
            if old_password == indb_password:
                st.success("✅ Şifre başarıyla değiştirildi!")  # Gerçek bir değişiklik için burada veri kaydedilmeli.
            else:
                st.error("❌ Eski şifre yanlış!")

else:
    # Eğer giriş yapan kişi, profil sahibiyle aynıysa (kendi profiline giriş yapıyorsa)
    
    with st.expander("📌 Projelerle Alakalı Bilgiler"):

        # Kullanıcının ilgilendiği proje türlerini seçebileceği alan
        project_types = ["Makine Öğrenmesi", "Web Geliştirme", "Mobil Uygulama", 
                         "Oyun Geliştirme", "Veri Bilimi", "Yapay Zeka"]
        selected_projects = st.multiselect("İlgilendiği Proje Türleri:", project_types, default=indb_interested_projects, disabled=True)

        # Başlık
        st.write("Daha önce katılınan projeler:")

        # CSS kodu
        css_code = """
            <style>
                .scrollable-container {
                    height: 300px;
                    overflow-y: scroll;
                    border: 2px solid #000000;  /* Kaydırılabilir alanın kenarlık rengi */
                    padding: 10px;
                    background-color: #3b2121;  /* Arka plan rengi */
                    border-radius: 15px;  /* Kenarları bombeli yapmak için */
                }
                .item {
                    padding: 10px;
                    margin: 5px;
                    border: 2px solid #000000;  /* Her öğenin kenarlık rengi */
                    border-radius: 5px;
                    background-color: #181616;  /* Kutuların arka plan rengi */
                    color: #acacac;  /* Yazı rengi */
                    font-size: 16px;  /* Yazı boyutu */
                    font-family: 'Arial', sans-serif;  /* Yazı fontu */
                }
                .item:hover {
                    background-color: #3a303080;  /* Üzerine gelince kutu rengi değişir */
                }
            </style>
        """

        # HTML içeriği dinamik olarak oluşturuluyor
        html_content = '<div class="scrollable-container">'
        for item in indb_attended_projects_list:
            html_content += f'<div class="item">{item}</div>'
        html_content += '</div>'

        # HTML ve CSS içeriğini Streamlit'te göster
        st.markdown(css_code + html_content, unsafe_allow_html=True)

        st.write("")

    # 📌 Kullanıcı Bilgileri
    with st.expander("📌 Kişisel Bilgiler ve İlgi Alanları"):
        new_name = st.text_input("Ad-Soyad:", value=indb_username, disabled=True)

        # Okul Seçimi
        schools = ["ODTÜ", "Boğaziçi", "İTÜ", "Bilkent", "Hacettepe", "Yıldız Teknik"]
        new_school = st.selectbox("Okul:", schools, index=schools.index(indb_school) if indb_school in schools else 0, disabled=True)

        # Sınıf seçimi (Radio Button - Tek seçim)
        class_options = ["9. sınıf", "10. sınıf", "11. sınıf", "12. sınıf", "Mezun"]
        new_class = st.selectbox("Sınıf:", class_options, index=class_options.index(indb_class) if indb_class in class_options else 0, disabled=True)

        # Yetenekler
        skills_list = ["Python", "Django", "Streamlit", "Makine Öğrenmesi", "NLP", "Veri Bilimi", "Flutter", "React"]
        new_skills = st.multiselect("Yetenekler:", skills_list, default=indb_skills, disabled=True)

        # Deneyimler
        new_experience = st.text_area("Deneyimler:", value=indb_experience, disabled=True)