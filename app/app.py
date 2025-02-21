import streamlit as st
import requests

# Konfigurasi URL API (sesuaikan dengan API yang sedang berjalan)
API_URL = "http://127.0.0.1:8000/predict"

# Mapping lokasi ke kode label encoding
lokasi_mapping = {
    "Andir, Bandung": 0, "Antapani, Bandung": 1, "Arcamanik, Bandung": 2, "Astanaanyar, Bandung": 3,
    "Babakanciparay, Bandung": 4, "Bandung Kidul, Bandung": 5, "Bandung Kulon, Bandung": 6,
    "Bandung Wetan, Bandung": 7, "Batununggal, Bandung": 8, "Bojongloa Kidul, Bandung": 9,
    "Buah Batu, Bandung": 10, "Cibeunying Kidul, Bandung": 11, "Cibiru, Bandung": 12,
    "Cicendo, Bandung": 13, "Cidadap, Bandung": 14, "Coblong, Bandung": 15,
    "Gede Bage, Bandung": 16, "Kiaracondong, Bandung": 17, "Lengkong, Bandung": 18,
    "Mandalajati, Bandung": 19, "Panyileukan, Bandung": 20, "Rancasari, Bandung": 21,
    "Regol, Bandung": 22, "Sukajadi, Bandung": 23, "Sukasari, Bandung": 24,
    "Sumurbandung, Bandung": 25, "Ujungberung, Bandung": 26
}

# Membuat judul aplikasi
st.title("🏡 Prediksi Harga Rumah di Bandung")

# Menampilkan deskripsi singkat
st.markdown("Masukkan detail properti untuk mendapatkan perkiraan harga.")

# Membuat form input
installment = st.number_input("💰 Cicilan (Installment)", min_value=0.0, step=100000.0)
bedroom_count = st.number_input("🛏 Jumlah Kamar Tidur", min_value=0, step=1)
bathroom_count = st.number_input("🛁 Jumlah Kamar Mandi", min_value=0, step=1)
carport_count = st.number_input("🚗 Jumlah Carport", min_value=0, step=1)
land_area = st.number_input("📏 Luas Tanah (m²)", min_value=0.0, step=1.0)
building_area = st.number_input("🏢 Luas Bangunan (m²)", min_value=0.0, step=1.0)

# Dropdown untuk lokasi
selected_location = st.selectbox("📍 Pilih Lokasi", list(lokasi_mapping.keys()))
location_encoded = lokasi_mapping[selected_location]  # Konversi ke kode label

# Tombol prediksi
if st.button("🔍 Prediksi Harga"):
    input_data = {
        "installment": installment,
        "bedroom_count": bedroom_count,
        "bathroom_count": bathroom_count,
        "carport_count": carport_count,
        "land_area": land_area,
        "building_area": building_area,
        "location_encoded": location_encoded
    }
    
    # Request ke API
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            prediksi = response.json()["predicted_price"]
            st.success(f"🏠 Perkiraan Harga Rumah: **Rp {prediksi:,.2f}**")
        else:
            st.error("Terjadi kesalahan saat mendapatkan prediksi.")
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Gagal menghubungi API: {e}")

# Footer
st.markdown("---")
st.caption("🚀 Dibuat dengan ❤️ menggunakan Streamlit")
