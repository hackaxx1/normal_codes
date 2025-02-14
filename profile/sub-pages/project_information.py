import streamlit as st

indb_interested_projects = ["Makine Öğrenmesi", "Web Geliştirme"]
indb_attended_projects_list = ["teknofest 2021 makine öğrenmesi", "tübitak 4000B yapay zeka"]

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