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

## Setup 
1. Navigate to the project directory:
   ```powershell
   cd "$HOME\Desktop\newos\emotion-chatbot"
   ```
2. Create and activate a virtual environment:
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





