# 📊 Submission Dicoding — Belajar Analisis Data dengan Python

![Dicoding Badge](https://img.shields.io/badge/Dicoding-Belajar%20Analisis%20Data%20dengan%20Python-blue?style=for-the-badge&logo=python)
![Streamlit Badge](https://img.shields.io/badge/Built%20with-Streamlit-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen?style=for-the-badge)

> Proyek akhir ini disusun untuk memenuhi submission pada course **Belajar Analisis Data dengan Python** oleh [Dicoding Indonesia](https://dicoding.com).  
> Dataset yang digunakan adalah **Bike Sharing Dataset**, dengan tujuan menghasilkan **insight dan visualisasi interaktif** yang dapat membantu pengambilan keputusan berbasis data.

---

## 📝 Deskripsi Proyek

🎯 **Tujuan**:  
Menganalisis perilaku penyewaan sepeda berdasarkan faktor-faktor seperti cuaca, musim, hari kerja, dan waktu.

🧩 **Output Proyek**:
- Proses analisis data secara lengkap (EDA, visualisasi, dan interpretasi).
- Dashboard interaktif menggunakan **Streamlit**.
- Insight berbasis data untuk menjawab pertanyaan bisnis yang relevan.

---

## 📁 Struktur Direktori

```
📦 submission_analisisData
┣ 📁 data
┃ ┗ 📄 day.csv, hour.csv
┣ 📁 dashboard
┃ ┗ 📄 dashboard.py
┣ 📄 Proyek_Analisis_Data_Samuel.ipynb
┣ 📄 requirements.txt
┗ 📄 README.md
```

- **/data/**: Berisi dataset yang digunakan (`day.csv` dan `hour.csv`).
- **/dashboard/**: Berisi aplikasi dashboard berbasis Streamlit.
- **Proyek_Analisis_Data_Samuel.ipynb**: Notebook utama untuk proses analisis data.

---

## ⚙️ Instalasi dan Setup

1. **Clone repository** ke komputer lokal Anda:
   ```bash
   git clone https://github.com/s4m-bhsr/submission_analisisData.git
   cd submission_analisisData
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Atau jika hanya ingin menjalankan dashboard:
   ```bash
   pip install streamlit
   ```

---

## 🚀 Menjalankan Dashboard

1. Masuk ke direktori `dashboard`:
   ```bash
   cd dashboard
   ```

2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard.py
   ```

✅ Atau cukup kunjungi secara online melalui:  
🌐 [🔗 Project Submission Analisis Data (Streamlit App)](https://bike-sharing-samuel974.streamlit.app/)

---

## 📊 Insight yang Dihasilkan

Beberapa insight utama dari proyek ini:

- 📅 **Tren musiman** menunjukkan peningkatan penyewaan di musim panas.
- 👥 **Hari kerja vs akhir pekan** memengaruhi tipe pengguna (registered vs casual).
- 🌦️ **Cuaca** menjadi salah satu faktor yang cukup signifikan terhadap total penyewaan.
- ⏰ **Jam sibuk** menunjukkan lonjakan pengguna registered di pagi dan sore hari.

---

## 🛠 Tools & Libraries

| Library           | Fungsi Utama                     |
|-------------------|----------------------------------|
| `pandas`          | Manipulasi dan analisis data     |
| `numpy`           | Operasi numerik dasar            |
| `matplotlib`      | Visualisasi statis               |
| `seaborn`         | Visualisasi statistik interaktif |
| `streamlit`       | Membuat dashboard interaktif     |
| `datetime`        | Konversi waktu dan tanggal       |

---
