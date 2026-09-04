# ✅ Grammar & Fluency Checker

A simple AI-powered web app that checks English grammar and gives a fluency (readability) score — like having a personal English tutor.

## 💡 Why I built this
As a former Spoken English Instructor and Peer Tutor, I spent a lot of time helping students fix grammar mistakes and improve fluency. This project turns that experience into an AI tool that anyone can use to get instant feedback on their writing.

## 🚀 Features
- Corrects grammar mistakes using a pretrained NLP model (T5 Transformer)
- Highlights exactly what was added/removed
- Gives a fluency score (Flesch Reading Ease) with simple feedback
- Clean, simple Streamlit interface

## 🛠️ Tech Stack
- Python
- HuggingFace Transformers (`vennify/t5-base-grammar-correction`)
- Streamlit
- textstat (readability scoring)

## ▶️ Run it locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Live Demo
[Add your Streamlit Cloud link here after deployment]

## 📸 Screenshot
[Add a screenshot of the app here]

## 📚 How it works
1. User types a sentence or paragraph.
2. A pretrained AI model (T5) suggests grammar corrections.
3. The app compares original vs corrected text and shows the differences.
4. A readability score is calculated to measure how easy the text is to read.

## 🔮 Future improvements
- Support for longer paragraphs
- Add support for checking Urdu-to-English translation fluency
- Track user's grammar mistake history over time
