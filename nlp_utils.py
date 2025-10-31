import os
import re
from typing import Tuple

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")
MODEL_PATH = os.path.join(MODEL_DIR, "emotion_model.pkl")
SAMPLE_DATASET_PATH = os.path.join(MODEL_DIR, "emotion_dataset_sample.csv")


def _basic_clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _load_training_data() -> pd.DataFrame:
    if os.path.exists(SAMPLE_DATASET_PATH):
        df = pd.read_csv(SAMPLE_DATASET_PATH)
        if {"text", "emotion"}.issubset(df.columns):
            return df
    # Fallback tiny inline dataset
    data = [
        ("I love this!", "happy"),
        ("This is amazing and wonderful", "happy"),
        ("I feel great today", "happy"),
        ("I am so sad", "sad"),
        ("This makes me cry", "sad"),
        ("I feel lonely and unhappy", "sad"),
        ("I am furious about this", "angry"),
        ("This pisses me off", "angry"),
        ("I am angry and frustrated", "angry"),
        ("I am scared", "fear"),
        ("This is terrifying", "fear"),
        ("I feel anxious and afraid", "fear"),
        ("No way! that's shocking", "surprise"),
        ("I did not expect this", "surprise"),
        ("Wow, unbelievable", "surprise"),
        ("I adore you", "love"),
        ("Sending you lots of love", "love"),
        ("I care about you", "love"),
        ("Okay", "neutral"),
        ("I see", "neutral"),
        ("That is fine", "neutral"),
    ]
    return pd.DataFrame(data, columns=["text", "emotion"])


def train_emotion_model() -> Tuple[Pipeline, dict]:
    os.makedirs(MODEL_DIR, exist_ok=True)
    df = _load_training_data()
    df = df.dropna(subset=["text", "emotion"])  # safety
    df["text"] = df["text"].astype(str).map(_basic_clean)

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["emotion"], test_size=0.2, random_state=42, stratify=df["emotion"]
    )

    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(stop_words="english", max_features=10000)),
            ("clf", LogisticRegression(max_iter=1000, n_jobs=None)),
        ]
    )

    pipeline.fit(X_train, y_train)

    # Optional quick report (printed once during training)
    try:
        y_pred = pipeline.predict(X_test)
        print(classification_report(y_test, y_pred))
    except Exception:
        pass

    joblib.dump(pipeline, MODEL_PATH)
    return pipeline, {"classes": sorted(df["emotion"].unique())}


def ensure_model() -> None:
    if os.path.exists(MODEL_PATH):
        return
    train_emotion_model()


def _load_model() -> Pipeline:
    if not os.path.exists(MODEL_PATH):
        ensure_model()
    return joblib.load(MODEL_PATH)


def predict_emotion(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return "neutral"
    model = _load_model()
    cleaned = _basic_clean(text)
    try:
        return str(model.predict([cleaned])[0])
    except Exception:
        return "neutral"


