# 📰 Fake News Detection using Machine Learning

A Machine Learning-based web application that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP). The application preprocesses the input text, converts it into numerical features using TF-IDF Vectorization, and predicts the result using a trained Support Vector Machine (SVM) model.

🔗 **Live Demo:** https://fake-news-detection-1-1v1r.onrender.com

---

## 📌 Features

- Detects whether a news article is **Fake** or **Real**
- Text preprocessing using NLP techniques
- TF-IDF Vectorization for feature extraction
- Trained Support Vector Machine (SVM) classifier
- Simple and user-friendly web interface
- Deployed online using Render

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning & NLP
- Scikit-learn
- Pandas
- NumPy
- NLTK
- TF-IDF Vectorizer
- Support Vector Machine (SVM)

### Web Framework
- Flask

### Deployment
- Render

---

## 📂 Project Structure

```
Fake-News-Detection/
│
├── app.py                 # Flask application
├── model.pkl              # Trained SVM model
├── vectorizer.pkl         # Saved TF-IDF vectorizer
├── templates/
│   └── index.html         # Frontend UI
├── requirements.txt
├── README.md
└── PROJECT2(FND).ipynb      # Model training notebook
```

---

## ⚙️ How It Works

1. User enters a news article or headline.
2. The text is cleaned and preprocessed.
3. The processed text is converted into TF-IDF features.
4. The trained SVM model predicts whether the news is **Fake** or **Real**.
5. The prediction is displayed on the web interface.

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/himanshu-agrwl/Fake-News-Detection.git
```

Move into the project directory

```bash
cd Fake-News-Detection
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Pipeline

```
News Article
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Support Vector Machine (SVM)
      │
      ▼
Prediction
(Fake / Real)
```

---

## 📸 Screenshots


### Prediction Result

> <img width="1140" height="187" alt="Screenshot 2026-06-22 144859" src="https://github.com/user-attachments/assets/f91f5992-9e69-4847-8587-65046e51f147" />


---

## 🔮 Future Improvements

- Add prediction confidence score
- Improve UI/UX
- Support batch predictions using CSV files
- Add explainable AI (highlight important words)
- Deploy REST API using FastAPI
- Dockerize the application

---

## 📚 Dataset

The model is trained on a labeled fake news dataset containing real and fake news articles.

---

## 👨‍💻 Author

**Himanshu Aggarwal**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
