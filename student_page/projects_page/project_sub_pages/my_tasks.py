import streamlit as st
import streamlit_modal as modal
from datetime import datetime, timedelta

# SON TESLİM TARİHİ GEÇEN GÖREVLERİ SALLADIM GERÇEK DEĞİLLER

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


# Örnek olması için 12 görev oluşturmak ister misin? İstersen ben otomatik olarak kalanları da üretebilirim.


def handle_task_operations(task):
    # Butona basıldığında yapılacak işlemler (şimdilik boş)
    pass

def load_more():
    st.session_state.visible_count += 6

def render():
    # Session state başlat
    if "visible_count" not in st.session_state: 
        st.session_state.visible_count = 6
    if "show_past" not in st.session_state:
        st.session_state.show_past = False

    st.subheader("Görevlerim")
    st.write("Bu sayfada görevler görüntülenir.")

    # Filtre kontrolü
    st.checkbox("Son teslim tarihi geçmiş görevleri göster", key="show_past")

    # Görevleri filtrele
    filtered_data = []
    for task in data:
        teslim_durumu = task.get("teslim durumu", "Edilmedi")  # default değeri Geçmedi

        if st.session_state.show_past or teslim_durumu != "Edildi":
            filtered_data.append(task)

    # Gösterilecek sayıyı kontrol et
    tasks_to_display = filtered_data[:st.session_state.visible_count]

    # 3 sütunlu görünüm
    cols = st.columns(3)
    for idx, task in enumerate(tasks_to_display):
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"##### {task['ad']}", unsafe_allow_html=True)

                with st.expander("Detayları Görüntüle"):
                    for key, value in task.items():
                        if key not in ["ad", "atayan id"]:
                            st.markdown(f"**{key.capitalize()}:** {value}")

                # Teslim durumu "Geçti" ise buton pasif
                btn_disabled = task.get("teslim durumu", "Edilmedi") == "Edildi"
                st.button("İşlemler", key=f"ops_{idx}", disabled=btn_disabled, on_click=handle_task_operations, args=(task,))

    # Daha fazla göster
    if st.session_state.visible_count < len(filtered_data):
        st.button("Daha fazla göster", on_click=load_more)
