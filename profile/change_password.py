import streamlit as st

indb_password = "1234"

old_password = st.text_input("Eski Şifre", type="password")
new_password = st.text_input("Yeni Şifre", type="password")
if st.button("Şifreyi Güncelle"):
    if old_password == indb_password:
        st.success("✅ Şifre başarıyla değiştirildi!")  # Gerçek bir değişiklik için burada veri kaydedilmeli.
    else:
        st.error("❌ Eski şifre yanlış!")