import streamlit as st

with st.expander("📌 Projelerle Alakalı Bilgiler"):

    # Kullanıcının ilgilendiği proje türlerini seçebileceği alan
    project_types = ["Makine Öğrenmesi", "Web Geliştirme", "Mobil Uygulama", 
                     "Oyun Geliştirme", "Veri Bilimi", "Yapay Zeka"]
    selected_projects = st.multiselect("İlgilendiğin Proje Türleri", project_types)

    # Liste öğelerini tanımlayın
    my_list = ["Elma", "Armut", "Muz", "Kiraz", "Çilek", "Portakal", "Kavun", "Limon", "Nar", "Şeftali"]

    # Başlık
    st.header("Daha önce katılınan projeler")

    # CSS kodu
    css_code = """
        <style>
            .scrollable-container {
                height: 300px;
                overflow-y: scroll;
                border: 2px solid #000000;  /* Kaydırılabilir alanın kenarlık rengi */
                padding: 10px;
                background-color: #3b2121;  /* Arka plan rengi */
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
    for item in my_list:
        html_content += f'<div class="item">{item}</div>'
    html_content += '</div>'

    # HTML ve CSS içeriğini Streamlit'te göster
    st.markdown(css_code + html_content, unsafe_allow_html=True)
