# 🏡 House Price Prediction - Bandung

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk membangun model prediksi harga rumah di Bandung berdasarkan beberapa fitur seperti jumlah kamar tidur, kamar mandi, luas tanah, luas bangunan, lokasi, dan lain-lain. Model yang digunakan adalah **XGBoost sebagai model utama**.

## 📂 Struktur Proyek

```
prediksi-harga-rumah-kota-bandung/
│── app/
|   ├── app.py
│── data/
|   ├── processed/
|   |   ├── house_prices_label_encoded.csv
|   |   ├── house_prices_test.csv
|   |   ├── house_prices_train.csv
|   |   ├── house_prices_val.csv
|   |   ├── noEncoded_data_harga_rumah_kota_bandung.csv
|   ├── raw/
|   |   ├── data_harga_rumah_kota_bandung.csv
│── models/
|   ├── xgboost_house_price_model.pkl
|── notebooks/
|   ├── 01_EDA.ipynb
|   ├── 02_Preprocessing.ipynb
|   ├── 03_Analisis_Data.ipynb
|   ├── 04_Encoded_Data.ipynb
|   ├── 05_Modeling.ipynb
|── src/
|   ├── _pycache_.py
│   ├── api.py           # API FastAPI untuk prediksi harga rumah
|── .gitignore
|── analytics-03-00003-v2.pdf
│── requirements.txt      # Dependensi proyek
│── README.md             # Dokumentasi proyek
|── screencapture-localhost-8501-2025-02-21-15_31_50.png
```

## 🚀 Cara Menjalankan Proyek

### 1️⃣ **Setup Virtual Environment** (Opsional tapi disarankan)

```bash
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
venv\Scripts\activate     # Untuk Windows
```

### 2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3️⃣ **Menjalankan API dengan FastAPI**

```bash
uvicorn src.api:app --reload
```

API akan berjalan di: **http://127.0.0.1:8000**

### 4️⃣ **Menjalankan Dashboard Streamlit**

```bash
streamlit run app/app.py
```

Dashboard akan tersedia di **http://localhost:8501**

## 🔑 Input Data untuk Prediksi

| Fitur            | Deskripsi                         |
| ---------------- | --------------------------------- |
| installment      | Cicilan rumah                     |
| bedroom_count    | Jumlah kamar tidur                |
| bathroom_count   | Jumlah kamar mandi                |
| carport_count    | Jumlah carport                    |
| land_area        | Luas tanah (m²)                   |
| building_area    | Luas bangunan (m²)                |
| location_encoded | Kode lokasi berdasarkan kecamatan |

### 📍 **Mapping Kode Lokasi**

| Lokasi                    | Kode |
|---------------------------|------|
| Andir, Bandung            | 0    |
| Antapani, Bandung         | 1    |
| Arcamanik, Bandung        | 2    |
| Astanaanyar, Bandung      | 3    |
| Babakanciparay, Bandung   | 4    |
| Bandung Kidul, Bandung    | 5    |
| Bandung Kulon, Bandung    | 6    |
| Bandung Wetan, Bandung    | 7    |
| Batununggal, Bandung      | 8    |
| Bojongloa Kidul, Bandung  | 9    |
| Buah Batu, Bandung        | 10   |
| Cibeunying Kidul, Bandung | 11   |
| Cibiru, Bandung           | 12   |
| Cicendo, Bandung          | 13   |
| Cidadap, Bandung          | 14   |
| Coblong, Bandung          | 15   |
| Gede Bage, Bandung        | 16   |
| Kiaracondong, Bandung     | 17   |
| Lengkong, Bandung         | 18   |
| Mandalajati, Bandung      | 19   |
| Panyileukan, Bandung      | 20   |
| Rancasari, Bandung        | 21   |
| Regol, Bandung            | 22   |
| Sukajadi, Bandung         | 23   |
| Sukasari, Bandung         | 24   |
| Sumurbandung, Bandung     | 25   |
| Ujungberung, Bandung      | 26   |

## 📊 Teknologi yang Digunakan

✅ **Python** _(pandas, numpy, scikit-learn, XGBoost)_  
✅ **FastAPI** _(untuk API backend)_  
✅ **Streamlit** _(untuk dashboard UI)_  
✅ **Uvicorn** _(untuk menjalankan server FastAPI)_  
✅ **Requests** _(untuk komunikasi API)_

## 📌 Kontributor

👨‍💻 **Arya Setia Pratama** - Teknik Informatika Universitas Lampung

---

🚀 _Project ini dibuat untuk mempermudah prediksi harga rumah di Bandung!_

### Sumber dataset : 
https://www.kaggle.com/datasets/khaleeel347/harga-rumah-seluruh-kecamatan-di-kota-bandung
