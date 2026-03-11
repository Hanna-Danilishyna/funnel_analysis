import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data/raw/events.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data/processed/cleaned_events.csv"

print("Loading raw data...")

df = pd.read_csv(RAW_DATA_PATH)

print("Initial shape:", df.shape)

# удаляем строки без user_id
df = df.dropna(subset=["user_id"])

# заполняем пропуски brand
df["brand"] = df["brand"].fillna("unknown")

# преобразуем время
df["event_time"] = pd.to_datetime(df["event_time"])

df["date"] = df["event_time"].dt.date
df["hour"] = df["event_time"].dt.hour
df["weekday"] = df["event_time"].dt.day_name()

print("Cleaned shape:", df.shape)

df.to_csv(PROCESSED_DATA_PATH, index=False)

print("Cleaned data saved:", PROCESSED_DATA_PATH)