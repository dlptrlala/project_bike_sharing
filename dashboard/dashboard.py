import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

sns.set_style("whitegrid")

# =====================================================
# Load Data
# =====================================================
hour_df = pd.read_csv("hour.csv")
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# =====================================================
# Sidebar
# =====================================================
st.sidebar.title("🚲 Capital Bikeshare")

st.sidebar.markdown("""
### Dashboard Analisis Data

Dashboard ini menampilkan hasil analisis **Bike Sharing Dataset**
berdasarkan kondisi cuaca, waktu, dan musim pada periode **2011–2012**.
""")

st.sidebar.divider()

st.sidebar.subheader("📅 Filter Tahun")

year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=[2011, 2012],
    default=[2011, 2012]
)

hour_df["year"] = hour_df["yr"].replace({
    0: 2011,
    1: 2012
})

hour_df = hour_df[
    hour_df["year"].isin(year)
]

st.sidebar.divider()

st.sidebar.markdown("""
### 📊 Informasi Dataset

- **Dataset** : Bike Sharing
- **Lokasi** : Washington D.C.
- **Periode** : 2011–2012
""")

# =====================================================
# Header
# =====================================================
st.title("🚲 Bike Sharing Dashboard")

st.caption(
    "Analisis pola penyewaan sepeda berdasarkan kondisi cuaca, waktu, dan musim pada Capital Bikeshare (2011–2012)."
)

# =====================================================
# Metrics
# =====================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Rentals",
        f"{hour_df['cnt'].sum():,}"
    )

with col2:
    st.metric(
        "Average Rentals",
        f"{hour_df['cnt'].mean():.0f}"
    )

with col3:
    st.metric(
        "Maximum Rentals",
        f"{hour_df['cnt'].max()}"
    )

st.divider()

# =====================================================
# Weather & Season Charts
# =====================================================

left_col, right_col = st.columns(2)

# ---------------- Weather ----------------
with left_col:

    st.subheader("🌦️ Average Bike Rentals by Weather")

    weather = (
        hour_df
        .groupby("weathersit")["cnt"]
        .mean()
        .reset_index()
    )

    weather_map = {
        1: "Clear",
        2: "Mist",
        3: "Light Rain/Snow",
        4: "Heavy Rain/Snow"
    }

    weather["weathersit"] = weather["weathersit"].map(weather_map)

    fig, ax = plt.subplots(figsize=(6,4))

    sns.barplot(
        data=weather,
        x="weathersit",
        y="cnt",
        palette="Blues",
        ax=ax
    )

    ax.set_xlabel("Weather Condition")
    ax.set_ylabel("Average Rentals")

    st.pyplot(fig)


# ---------------- Season ----------------
with right_col:

    st.subheader("🍂 Average Bike Rentals by Season")

    season = (
        hour_df
        .groupby("season")["cnt"]
        .mean()
        .reset_index()
    )

    season_map = {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }

    season["season"] = season["season"].map(season_map)

    fig, ax = plt.subplots(figsize=(6,4))

    sns.barplot(
        data=season,
        x="season",
        y="cnt",
        palette="viridis",
        ax=ax
    )

    ax.set_xlabel("Season")
    ax.set_ylabel("Average Rentals")

    st.pyplot(fig)

st.divider()

# =====================================================
# Bike Rentals by Hour
# =====================================================

st.subheader("📈 Bike Rentals by Hour")

working = (
    hour_df
    .groupby(["workingday", "hr"])["cnt"]
    .mean()
    .reset_index()
)

working["workingday"] = working["workingday"].replace({
    0: "Holiday",
    1: "Working Day"
})

fig, ax = plt.subplots(figsize=(12,5))

sns.lineplot(
    data=working,
    x="hr",
    y="cnt",
    hue="workingday",
    linewidth=2.5,
    ax=ax
)

ax.set_xticks(range(24))
ax.set_xlabel("Hour")
ax.set_ylabel("Average Rentals")
ax.legend(title="Day Type")

st.pyplot(fig)

st.divider()

# =====================================================
# Dataset Preview
# =====================================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    hour_df.head(),
    use_container_width=True
)