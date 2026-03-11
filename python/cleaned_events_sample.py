import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA = BASE_DIR / "data/raw/events.csv"
SAMPLE_DATA = BASE_DIR / "data/processed/cleaned_events_sample.csv"

df = pd.read_csv(RAW_DATA)

df_sample = df.sample(n=50000, random_state=42)
df_sample.to_csv(SAMPLE_DATA, index=False)