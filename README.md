# proyek_bike_sharing

## Deskripsi Proyek

Proyek ini merupakan analisis data menggunakan **Bike Sharing Dataset** dari Capital Bikeshare, Washington D.C., Amerika Serikat, periode **2011–2012**.

Analisis dilakukan untuk menjawab beberapa pertanyaan bisnis, yaitu:
1. Bagaimana kondisi cuaca memengaruhi rata-rata jumlah penyewaan sepeda?
2. Pada jam berapa permintaan penyewaan sepeda paling tinggi pada hari kerja dibandingkan hari libur?
3. Bagaimana pola penyewaan sepeda pada setiap musim?

Hasil analisis kemudian divisualisasikan dalam bentuk dashboard interaktif menggunakan **Streamlit**.

---

## Setup Environment

### Menggunakan Anaconda

```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

### Menggunakan Virtual Environment (venv)

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## Menjalankan Dashboard

Masuk ke folder dashboard

```bash
cd dashboard
```

Jalankan Streamlit

```bash
streamlit run dashboard.py
```

Dashboard akan berjalan pada browser dengan alamat:

```
http://localhost:8501
```

---

## Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset** yang berisi data penyewaan sepeda Capital Bikeshare di Washington D.C. selama periode 2011–2012.

Dataset terdiri dari:

- **day.csv** → data penyewaan harian
- **hour.csv** → data penyewaan per jam

---

## Library yang Digunakan

- pandas
- numpy
- matplotlib
- seaborn
- streamlit
