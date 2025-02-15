import streamlit as st
from datetime import datetime

data = [
    {"ad": "Proje 1", "arama_baslangic_tarihi": "2024-03-01", "alan": "Yapay Zeka", "yarışma": "Teknofest", "aranan_elemanlar": ["Yazılımcı", "Veri Bilimci"], "image": "https://placehold.co/400x400"},
    {"ad": "Proje 2", "arama_baslangic_tarihi": "2024-02-15", "alan": "Havacılık", "yarışma": "TÜBİTAK", "aranan_elemanlar": ["Mekatronik Mühendisi"], "image": "https://placehold.co/400x400"},
    {"ad": "Proje 3", "arama_baslangic_tarihi": "2024-01-10", "alan": "Robotik", "yarışma": "Teknofest", "aranan_elemanlar": ["Tasarımcı", "Elektrik Mühendisi"], "image": "https://placehold.co/400x400"},
    {"ad": "Proje 4", "arama_baslangic_tarihi": "2024-03-05", "alan": "Biyoteknoloji", "yarışma": "TÜBİTAK", "aranan_elemanlar": ["Biyolog", "Kimyager"], "image": "https://placehold.co/400x400"},
    {"ad": "Proje 5", "arama_baslangic_tarihi": "2024-02-20", "alan": "Otonom Sistemler", "yarışma": "Teknofest", "aranan_elemanlar": ["Gömülü Sistem Mühendisi"], "image": "https://placehold.co/400x400"},
]

st.title("Proje Arama ve Filtreleme")

# Filtreleme seçenekleri
alanlar = list(set(item["alan"] for item in data))
yarismalar = list(set(item["yarışma"] for item in data))
aranan_elemanlar = list(set(eleman for item in data for eleman in item["aranan_elemanlar"]))

# Filtreleme için yatay düzen
col1, col2, col3 = st.columns(3)
with col1:
    secili_alan = st.multiselect("Alan Seçin", alanlar)
with col2:
    secili_yarisma = st.multiselect("Yarışma Seçin", yarismalar)
with col3:
    secili_elemanlar = st.multiselect("Aranan Elemanlar", aranan_elemanlar)

# Filtreleme işlemi
filtered_data = [
    item for item in data 
    if (not secili_alan or item["alan"] in secili_alan) and
       (not secili_yarisma or item["yarışma"] in secili_yarisma) and
       (not secili_elemanlar or any(eleman in secili_elemanlar for eleman in item["aranan_elemanlar"]))
]

# Eğer filtreleme yapılmadıysa en yeni 4 projeyi göster
if not (secili_alan or secili_yarisma or secili_elemanlar):
    filtered_data = sorted(data, key=lambda x: datetime.strptime(x["arama_baslangic_tarihi"], "%Y-%m-%d"), reverse=True)[:4]

# Kartları gösterme
if filtered_data:
    with st.container():
        for item in filtered_data:
            with st.container(border=True):
                col1, col2 = st.columns([1, 6])
                with col1:
                    st.image(item["image"], width=170)
                with col2:
                    st.write(f"**{item['ad']}**")
                    st.write(f"**Alan:** {item['alan']}")
                    st.write(f"**Yarışma:** {item['yarışma']}")
                    st.write(f"**Aranan Elemanlar:** {', '.join(item['aranan_elemanlar'])}")
                    st.write(f"**Arama Başlangıç Tarihi:** {item['arama_baslangic_tarihi']}")
                    
                    if st.button("Detayları Gör", key=f"detay_{item['ad']}"):
                        with st.expander(f"Detaylar - {item['ad']}"):
                            st.write("Buraya detaylı içerik eklenebilir.")
                    
else:
    st.warning("Filtrelere uyan proje bulunamadı.")
