import streamlit as st
from datetime import datetime

# Açık kapalı proje sistemi eklendi

# Sayfa durumu oluşturma
if 'offset' not in st.session_state:
    st.session_state.offset = 0
if 'displayed_projects' not in st.session_state:
    st.session_state.displayed_projects = []
if 'last_filters' not in st.session_state:
    st.session_state.last_filters = {
        "alan": [], "yarışma": [], "eleman": [], "basvuru": False
    }

st.set_page_config(page_title="Proje Vitrini", layout="wide")

data = [
    {"ad": "Proje 1",
     "arama_baslangic_tarihi": "2024-03-01",
     "alan": "Yapay Zeka",
     "yarışma": "Teknofest",
     "aranan_elemanlar": ["Yazılımcı", "Veri Bilimci"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 1 için başvuru tamamlandı!"),
     "basvuru_acik": True},

    {"ad": "Proje 2",
     "arama_baslangic_tarihi":
     "2024-02-15",
     "alan": "Havacılık",
     "yarışma": "TÜBİTAK",
     "aranan_elemanlar": ["Mekatronik Mühendisi"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 2 için başvuru tamamlandı!"),
     "basvuru_acik": False},

    {"ad": "Proje 3",
     "arama_baslangic_tarihi": "2024-01-10",
     "alan": "Robotik",
     "yarışma": "Teknofest",
     "aranan_elemanlar": ["Tasarımcı", "Elektrik Mühendisi"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 3 için başvuru tamamlandı!"),
     "basvuru_acik": True},

    {"ad": "Proje 4",
     "arama_baslangic_tarihi": "2024-03-05",
     "alan": "Biyoteknoloji",
     "yarışma": "TÜBİTAK",
     "aranan_elemanlar": ["Biyolog", "Kimyager"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 4 için başvuru tamamlandı!"),
     "basvuru_acik": False},

    {"ad": "Proje 5",
     "arama_baslangic_tarihi": "2024-02-20",
     "alan": "Otonom Sistemler",
     "yarışma": "Teknofest",
     "aranan_elemanlar": ["Gömülü Sistem Mühendisi"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 5 için başvuru tamamlandı!"),
     "basvuru_acik": True},

    {"ad": "Proje 6",
     "arama_baslangic_tarihi": "2024-03-10",
     "alan": "Sağlık Teknolojileri",
     "yarışma": "TÜBİTAK",
     "aranan_elemanlar": ["Biyomedikal Mühendisi", "Veri Analisti"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 6 için başvuru tamamlandı!"),
     "basvuru_acik": True},

    {"ad": "Proje 7",
     "arama_baslangic_tarihi": "2024-02-28",
     "alan": "Yapay Zeka",
     "yarışma": "Teknofest",
     "aranan_elemanlar": ["Makine Öğrenmesi Uzmanı", "Veri Bilimci"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 7 için başvuru tamamlandı!"),
     "basvuru_acik": False},

    {"ad": "Proje 8",
     "arama_baslangic_tarihi": "2024-03-12",
     "alan": "Siber Güvenlik",
     "yarışma": "CTF Yarışması",
     "aranan_elemanlar": ["Etik Hacker", "Güvenlik Analisti"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 8 için başvuru tamamlandı!"),
     "basvuru_acik": False},

    {"ad": "Proje 9",
     "arama_baslangic_tarihi": "2024-02-05",
     "alan": "Otonom Sistemler",
     "yarışma": "Teknofest",
     "aranan_elemanlar": ["Kontrol Sistemleri Mühendisi", "Gömülü Yazılım Geliştirici"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 9 için başvuru tamamlandı!"),
     "basvuru_acik": True},

    {"ad": "Proje 10",
     "arama_baslangic_tarihi": "2024-03-18",
     "alan": "Robotik",
     "yarışma": "Uluslararası Robot Yarışması",
     "aranan_elemanlar": ["Mekatronik Mühendisi", "Yapay Zeka Geliştiricisi"],
     "image": "https://placehold.co/400x400",
     "basvuru_fonksiyonu": lambda: st.success("Proje 10 için başvuru tamamlandı!"),
     "basvuru_acik": False}
]

st.title("Proje Vitrini")

# Filtreleme alanları
alanlar = list(set(item["alan"] for item in data))
yarismalar = list(set(item["yarışma"] for item in data))
aranan_elemanlar = list(set(eleman for item in data for eleman in item["aranan_elemanlar"]))

sol_alan, col1, col2, col3 = st.columns([3, 3, 3, 3])
with sol_alan:
    basvuru_kapali_goster = st.checkbox("Başvurusu Bitmişleri Göster", value=False)
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
       (not secili_elemanlar or any(eleman in secili_elemanlar for eleman in item["aranan_elemanlar"])) and
       (basvuru_kapali_goster or item["basvuru_acik"])
]

# Tarihe göre sırala
filtered_data = sorted(filtered_data, key=lambda x: datetime.strptime(x["arama_baslangic_tarihi"], "%Y-%m-%d"), reverse=True)

# Filtre değişimi kontrolü
if (
    st.session_state.last_filters["alan"] != secili_alan or
    st.session_state.last_filters["yarışma"] != secili_yarisma or
    st.session_state.last_filters["eleman"] != secili_elemanlar or
    st.session_state.last_filters["basvuru"] != basvuru_kapali_goster
):
    st.session_state.displayed_projects = filtered_data[:4]
    st.session_state.offset = 4
    st.session_state.last_filters = {
        "alan": secili_alan,
        "yarışma": secili_yarisma,
        "eleman": secili_elemanlar,
        "basvuru": basvuru_kapali_goster
    }

# İlk yükleme
if not st.session_state.displayed_projects and not (secili_alan or secili_yarisma or secili_elemanlar or basvuru_kapali_goster):
    st.session_state.displayed_projects = filtered_data[:4]
    st.session_state.offset = 4

# Kartları Göster
if st.session_state.displayed_projects:
    for item in st.session_state.displayed_projects:
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
                st.write(f"**Başvuru Durumu:** {'Açık' if item['basvuru_acik'] else 'Kapalı'}")
                col4, col5 = st.columns([3, 1])
                with col4:
                    with st.expander(f"Detaylar - {item['ad']}"):
                        st.write("Buraya detaylı içerik eklenebilir.")
                with col5:
                    if item["basvuru_acik"]:
                        if st.button("Başvur", key=f"basvur_{item['ad']}"):
                            item["basvuru_fonksiyonu"]()
                    else:
                        st.button("Başvur", key=f"basvur_{item['ad']}", disabled=True)

    # Daha fazla göster
    if st.session_state.offset < len(filtered_data):
        if st.button("Daha Fazla Göster"):
            next_projects = filtered_data[st.session_state.offset:st.session_state.offset + 4]
            st.session_state.displayed_projects.extend(next_projects)
            st.session_state.offset += 4
            st.rerun()
else:
    st.warning("Filtrelere uyan proje bulunamadı.")