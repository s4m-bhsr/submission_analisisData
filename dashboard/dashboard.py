import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  
import seaborn as sns

# Load dataset hasil cleaning
day_df = pd.read_csv("dashboard/cleaned_bike_data.csv")  
day_df["dteday"] = pd.to_datetime(day_df["dteday"])  

# Mapping nilai season ke label musim
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_name"] = day_df["season"].map(season_labels)

# Mapping cuaca
weather_labels = {
    1: "Cerah / Sedikit Awan",
    2: "Berawan / Kabut",
    3: "Hujan / Salju Ringan",
    4: "Hujan Lebat / Salju Lebat / Kabut + Angin Kencang"
}
day_df["weather_desc"] = day_df["weathersit"].map(weather_labels)

# Judul Dashboard
st.title("📊 Bike Sharing Data Dashboard")

# Sidebar: Pilih rentang tanggal untuk filtering interaktif
st.sidebar.header("📆 Pilih Rentang Tanggal")

# Mendapatkan rentang tanggal dataset
min_date = day_df["dteday"].min().date()
max_date = day_df["dteday"].max().date()

# Input rentang tanggal
start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Waktu", 
    [min_date, max_date], 
    min_value=min_date, 
    max_value=max_date
)

# Konversi ke datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataset berdasarkan rentang tanggal yang dipilih
filtered_df = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]

# Pilihan Analisis
st.sidebar.header("🔍 Pilih Analisis")
option = st.sidebar.selectbox(
    "Pilih kategori:", 
    ["Tren Penyewaan", "Pengaruh Cuaca", "Perbandingan Hari Kerja vs Akhir Pekan"]
)

# 📌 **1. Tren Penyewaan Sepeda**
if option == "Tren Penyewaan":
    st.subheader("📈 Tren Penyewaan Sepeda Harian dalam Setahun")

    # 📌 **Tren Penyewaan Sepeda Harian**
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(x=filtered_df["dteday"], y=filtered_df["cnt"], ax=ax, color="blue")

    # **Atur Format sumbu X**
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Tren Penyewaan Sepeda dalam Setahun")

    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)

    st.pyplot(fig)

    # 📌 **Rata-rata Penyewaan Sepeda Berdasarkan Musim**
    st.subheader("📊 Rata-rata Penyewaan Sepeda Berdasarkan Musim")

    season_avg = filtered_df.groupby("season_name")["cnt"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="season_name", y="cnt", data=season_avg, ax=ax, palette="viridis")

    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    ax.set_title("Penyewaan Sepeda Berdasarkan Musim")

    st.pyplot(fig)

# 📌 **2. Pengaruh Cuaca terhadap Penyewaan**
elif option == "Pengaruh Cuaca":
    st.subheader("🌤️ Pengaruh Cuaca terhadap Penyewaan Sepeda")

    weather_avg_rentals = filtered_df.groupby("weather_desc")["cnt"].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    weather_avg_rentals.plot(kind="bar", color=["blue", "gray", "orange", "red"], ax=ax)

    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_title("Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    st.pyplot(fig)

# 📌 **3. Perbandingan Hari Kerja vs Akhir Pekan berdasarkan Tipe Pengguna**
elif option == "Perbandingan Hari Kerja vs Akhir Pekan":
    st.subheader("📆 Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")

    # Mapping weekday ke kategori hari kerja atau akhir pekan
    filtered_df["day_type"] = filtered_df["weekday"].apply(lambda x: "Akhir Pekan" if x in [0, 6] else "Hari Kerja")

    # Hitung rata-rata penyewaan berdasarkan tipe hari dan tipe pelanggan
    rental_by_day_type = filtered_df.groupby(["day_type"])[["casual", "registered"]].mean().reset_index()

    # Plot perbandingan dengan seaborn
    fig, ax = plt.subplots(figsize=(8, 5))
    rental_by_day_type.set_index("day_type").plot(kind="bar", ax=ax, color=["skyblue", "salmon"])

    ax.set_xlabel("Tipe Hari")
    ax.set_ylabel("Rata-rata Jumlah Penyewaan")
    ax.set_title("Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
    ax.legend(["Pelanggan Biasa", "Pelanggan Terdaftar"])

    plt.xticks(rotation=0)  # Label tetap horizontal

    st.pyplot(fig)
