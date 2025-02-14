import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_modal import Modal
from lib.lib_for_page import app

def change_password():
    cp_modal = Modal(key="change_passw",title="Şifre Değiştir")
    open_modal = True
    if open_modal:
        with cp_modal.container():
            app.get_app("C:\\Users\\eymen\\Desktop\\projeyonetim-main\\apps\\profile\\sub-pages\\change_password.py")
            
def personal_inf():
    pi_modal = Modal(key="personal_inf",title="Kişisel Bilgiler")
    open_modal = True
    if open_modal:
        with pi_modal.container():
            app.get_app("C:\\Users\\eymen\\Desktop\\projeyonetim-main\\apps\\profile\\sub-pages\\personal_information.py")

def project_inf():
    pri_modal = Modal(key="project_inf",title="Proje Bilgileri")
    open_modal = True
    if open_modal:
        with pri_modal.container():
            app.get_app("C:\\Users\\eymen\\Desktop\\projeyonetim-main\\apps\\profile\\sub-pages\\project_information.py")


def main():
    st.set_page_config(page_title="Profil Kartı", page_icon="👤", layout="centered")

    profile_image_url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"

    st.markdown(f"""
    <style>
        body {{
            background-color: #0A192F; /* Koyu mavi arka plan */
        }}
        .profile-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }}
        .profile-card {{
            width: 250px;
            background-color: #112D4E; /* Koyu mavi tonunda kart */
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
            border: 3px solid #3F72AF; /* Orta koyu mavi çerçeve */
        }}
        .profile-name {{
            font-size: 18px;
            font-weight: bold;
            color: #DBE2EF; /* Açık mavi/metalik gri */
            margin-top: 20px; /* Kullanıcı adı ile resim arasına boşluk eklendi */
        }}
        .button-container {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }}
        .stButton > button {{
            width: 100%;
            height: 50px;
            background-color: #112D4E; /* Koyu mavi */
            color: white;
            border-radius: 15px; /* Bombeli kenarlar */
            font-size: 16px;
            border: none;
            transition: 0.3s;
        }}
        .stButton > button:hover {{
            background-color: #3F72AF; /* Açık mavi hover efekti */
        }}
    </style>
    <div class="profile-container">
        <div class="profile-card">
            <img src="{profile_image_url}" class="profile-image">
            <p class="profile-name">Kullanıcı Adı</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    colored_header(" ", description="Kullanıcı bilgilerini görüntüleyin", color_name="blue-70")


    buttons = [
        ("🔑", "Şifre Değiştir", change_password), ("👤", "Kişisel Bilgiler", personal_inf), 
        ("🗃", "Proje Bilgileri", project_inf)
    ]

    # Butonları 2 Satırda 4’erli olarak yerleştirme
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    for icon, label, func in buttons:
        if st.button(f"{icon} {label}"):
            func()  # Her butona özel fonksiyon çalıştırılıyor
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
