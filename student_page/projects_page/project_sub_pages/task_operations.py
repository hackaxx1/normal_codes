import streamlit as st
import time
from datetime import datetime, timedelta

data = [
    {
        "ad": "Proje yönetim sayfasının kodlanması",
        "başlangıç tarihi": "2024-03-01",
        "bitiş tarihi": "2024-03-05",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Streamlit üzerinde proje yönetim arayüzü geliştir.",
        "urun": "main.py",
        "teslim durumu": "Edildi",
    },
    {
        "ad": "Veritabanı bağlantısının yapılması",
        "başlangıç tarihi": "2024-04-01",
        "bitiş tarihi": "2024-04-10",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "SQLite veritabanı bağlantısını oluştur.",
        "urun": "db.py",
        "teslim durumu": "Geçti"
    },
    {
        "ad": "Arayüz tasarımının tamamlanması",
        "başlangıç tarihi": "2024-04-11",
        "bitiş tarihi": "2024-04-15",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Streamlit UI bileşenlerini oluştur ve hizala.",
        "urun": "ui.py",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "Kullanıcı giriş sisteminin kurulması",
        "başlangıç tarihi": "2024-03-10",
        "bitiş tarihi": "2024-03-15",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Kullanıcıların giriş yapabileceği auth sistemi kur.",
        "urun": "auth.py",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "E-posta bildirim sisteminin eklenmesi",
        "başlangıç tarihi": "2024-04-05",
        "bitiş tarihi": "2024-04-08",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Görev atandığında kullanıcıya mail gönder.",
        "urun": "email_notifier.py",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "Yedekleme sisteminin kurulması",
        "başlangıç tarihi": "2024-04-10",
        "bitiş tarihi": "2024-04-20",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Görev verilerini belirli aralıklarla yedekle.",
        "urun": "backup.py",
        "teslim durumu": "Geçti"
    },
    {
        "ad": "Performans optimizasyonu",
        "başlangıç tarihi": "2024-03-20",
        "bitiş tarihi": "2024-03-25",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Yavaş sayfaları optimize et.",
        "urun": "optimize.py",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "Mobil uyumluluğun sağlanması",
        "başlangıç tarihi": "2024-04-02",
        "bitiş tarihi": "2024-04-07",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Arayüzün mobil cihazlarda da düzgün çalışmasını sağla.",
        "urun": "responsive.css",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "Görev takibi için filtreleme sistemi",
        "başlangıç tarihi": "2024-04-12",
        "bitiş tarihi": "2024-04-18",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Görevleri tarih ve durum bazlı filtrele.",
        "urun": "filters.py",
        "teslim durumu": "Geçti"
    },
    {
        "ad": "PDF rapor çıktısı alma",
        "başlangıç tarihi": "2024-03-15",
        "bitiş tarihi": "2024-03-20",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Görev özetlerini PDF olarak dışa aktar.",
        "urun": "report.py",
        "teslim durumu": "Edildi"
    },
    {
        "ad": "Görev silme özelliğinin eklenmesi",
        "başlangıç tarihi": "2024-04-01",
        "bitiş tarihi": "2024-04-03",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Kullanıcılar görevleri silebilsin.",
        "urun": "delete_task.py",
        "teslim durumu": "Geçti"
    },
    {
        "ad": "Kullanıcı profili sayfası",
        "başlangıç tarihi": "2024-04-10",
        "bitiş tarihi": "2024-04-22",
        "atayan": "Eymen Taha Midilli",
        "atayan id": "000001",
        "görev": "Kullanıcının bilgilerini ve görev geçmişini göster.",
        "urun": "profile.py",
        "teslim durumu": "Edildi"
    },
]

porcesses = ["Soru, netleştirme iste", "Görevi yeniden tanımlandırma, revize", "Süre uzatma", "Görev yükü azaltması veya bölme", "Görevi reddetme", "Eksik, engel, hata bildir"]

class TaskOperations:
    def soru():
        secilen_proje = st.session_state.secilen_proje
        if st.session_state.clicked_button_task is not None:
            with st.container():
                st.write("Soru, netleştirme iste işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=secilen_proje, disabled=True)
                st.text_area("Açıklama", placeholder="Açıklama girin...")
                if st.button("Gönder"):
                    st.success("Soru gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
            st.session_state.clicked_button_task = None
        else:
            with st.container():
                st.write("Soru, netleştirme iste işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=secilen_proje["ad"], disabled=True)
                st.text_area("Açıklama", placeholder="Açıklama girin...")
                if st.button("Gönder"):
                    st.success("Soru gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
    def yenidenTanimlama():
        if st.session_state.clicked_button_task is not None:
            with st.container():
                st.write("Görevi yeniden tanımlandırma, revize işlemi için detayları girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje, disabled=True)
                if st.button("Gönder"):
                    st.success("Görevi yeniden tanımlama isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
            st.session_state.clicked_button_task = None
        else:
            with st.container():
                st.write("Görevi yeniden tanımlandırma, revize işlemi için detayları girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje["ad"], disabled=True)
                if st.button("Gönder"):
                    st.success("Görevi yeniden tanımlama isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
    def sureUzatma():
        with st.container():
            if st.session_state.clicked_button_task is not None:
                st.write("Süre uzatma işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje, disabled=True)
                st.write("Mevcut bitiş tarihi: ", str(st.session_state.clicked_button_task["bitiş tarihi"]))
                st.date_input("Yeni bitiş tarihi", min_value=st.session_state.clicked_button_task["bitiş tarihi"])
                if st.button("Gönder"):
                    st.success("Süre uzatma isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
                st.session_state.clicked_button_task = None
            else:
                st.write("Süre uzatma işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje["ad"], disabled=True)
                st.write("Mevcut bitiş tarihi: ", str(st.session_state.secilen_proje["bitiş tarihi"]))
                st.date_input("Yeni bitiş tarihi", min_value=st.session_state.secilen_proje["bitiş tarihi"])
                if st.button("Gönder"):
                    st.success("Süre uzatma isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
    def gorevYukuAzaltma():
            if st.session_state.clicked_button_task is not None:
                with st.container():
                    st.write("Görev yükü azaltması veya bölme işlemi için detayları ve isteklerinizi girin.")
                    st.text_input("Proje adı", value=st.session_state.secilen_proje, disabled=True)
                    st.text_area("Açıklama", placeholder="Açıklama girin...")
                    if st.button("Gönder"):
                        st.success("Görev yükü azaltma isteği gönderildi!")
                        # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
                st.session_state.clicked_button_task = None
            else:
                st.write("Görev yükü azaltması veya bölme işlemi için detayları ve isteklerinizi girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje["ad"], disabled=True)
                st.text_area("Açıklama", placeholder="Açıklama girin...")
                if st.button("Gönder"):
                    st.success("Görev yükü azaltma isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
    def gorevRed():
        if st.session_state.clicked_button_task is not None:
            with st.container():
                st.write("Görevi reddetme sebebinizi girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje, disabled=True)
                if st.button("Gönder"):
                    st.success("Görev reddetme isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
            st.session_state.clicked_button_task = None
        else:
            with st.container():
                st.write("Görevi reddetme sebebinizi girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje["ad"], disabled=True)
                if st.button("Gönder"):
                    st.success("Görev reddetme isteği gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
    def eksikEngelHata():
        if st.session_state.clicked_button_task is not None:
            with st.container():
                st.write("Eksik, engel, hata bildirme işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje, disabled=True)
                if st.button("Gönder"):
                    st.success("Eksik, engel, hata bildirimi gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK
            st.session_state.clicked_button_task = None
        else:
            with st.container():
                st.write("Eksik, engel, hata bildirme işlemi için gerekli bilgileri girin.")
                st.text_input("Proje adı", value=st.session_state.secilen_proje["ad"], disabled=True)
                if st.button("Gönder"):
                    st.success("Eksik, engel, hata bildirimi gönderildi!")
                    # BU NOKTA BACKENDE KALIYOR DATAYA YAZILACAK

def render():
    if "secilen_islem" not in st.session_state:
        st.session_state.secilen_islem = "Soru, netleştirme iste"
    if "secilen_proje" not in st.session_state:
        st.session_state.secilen_proje = data[0]["ad"]

    st.subheader("Görev İşlemleri paneli")
    col1, col2 = st.columns([3, 3])
    with col1:
        proje_adlari = [item["ad"] for item in data if item["teslim durumu"] != "Edildi"]
        if st.session_state.clicked_button_task != None:
            st.session_state.secilen_proje = st.selectbox("Bir proje seçin:", proje_adlari, index = proje_adlari.index(st.session_state.clicked_button_task["ad"]))
        else:
            st.session_state.secilen_proje = st.selectbox("Bir proje seçin:", proje_adlari)
            st.session_state.secilen_proje = next((item for item in data if item["ad"] == st.session_state.secilen_proje), None)
    with col2:
        islem_adları = porcesses
        st.session_state.secilen_islem = st.selectbox("Bir işlem seçin:", islem_adları)
    
    if st.button("İşleme geç"):
        islemf()


def islemf():
    secilen_islem = st.session_state["secilen_islem"]
    if secilen_islem == "Soru, netleştirme iste":
        TaskOperations.soru()
    if secilen_islem == "Görevi yeniden tanımlandırma, revize":
        TaskOperations.yenidenTanimlama()
    if secilen_islem == "Süre uzatma":
        TaskOperations.sureUzatma()
    if secilen_islem == "Görev yükü azaltması veya bölme":
        TaskOperations.gorevYukuAzaltma()
    if secilen_islem == "Görevi reddetme":
        TaskOperations.gorevRed()
    if secilen_islem == "Eksik, engel, hata bildir":
        TaskOperations.eksikEngelHata()
