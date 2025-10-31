# Emotion-Based Chatbot (Flask + scikit-learn)

An end-to-end web chatbot that detects user emotion from messages and replies empathetically.

## Features
- Emotion detection using TF-IDF + Logistic Regression
- Auto-trains on first run if no saved model is present
- Minimal web UI (HTML/CSS) for chatting

## Project Structure
```
emotion-chatbot/
  app.py
  nlp_utils.py
  requirements.txt
  templates/
    index.html
  static/
    style.css
  model/
    emotion_dataset_sample.csv
    emotion_model.pkl  # created on first run
```

## Setup (Windows PowerShell)
1. Navigate to the project directory:
   ```powershell
   cd "$HOME\Desktop\newos\emotion-chatbot"
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the app:
   ```powershell
   python app.py
   ```
5. Open `http://localhost:5000` in your browser.

## Notes
- On the first run, if `model/emotion_model.pkl` is missing, the app will train a quick baseline model using `model/emotion_dataset_sample.csv` and save it.
- For better accuracy, replace `emotion_dataset_sample.csv` with a larger dataset (same columns: `text,emotion`) and delete `emotion_model.pkl` to trigger retraining.

## Resume Bullet
- Built an end-to-end emotion-aware chatbot using Python Flask and scikit-learn. Implemented NLP preprocessing, TF-IDF features, and Logistic Regression for emotion classification; integrated a responsive web UI and automated model training pipeline.

