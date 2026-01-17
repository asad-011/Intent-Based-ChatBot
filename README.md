# Flask NLP Chatbot 🤖

A simple **NLP-based chatbot** built using **Flask** and **Scikit-learn**. The chatbot can handle greetings, jokes, time/date queries, basic help requests, and more using a machine learning intent classification approach.

---

## 🚀 Features

* Intent classification using **TF-IDF + Logistic Regression**
* Built with **Flask** (Python web framework)
* Handles common conversations like:

  * Greetings
  * Asking name
  * Asking time & date
  * Jokes
  * Help queries
  * Thanks & confirmations
* JSON-based API endpoint for chat
* Simple and beginner-friendly project structure

---

## 🧠 How It Works

1. User sends a message from the UI or API
2. Text is cleaned and vectorized using **TF-IDF**
3. A **Logistic Regression** model predicts the intent
4. The chatbot responds based on the predicted intent
5. Time and date are generated dynamically

---

## 🛠️ Tech Stack

* **Python 3**
* **Flask**
* **Scikit-learn**
* **HTML / CSS / JavaScript** (Frontend)

---

## 📁 Project Structure

```
project-folder/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── (optional css/js files)
```

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/flask-nlp-chatbot.git
cd flask-nlp-chatbot
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

The app will run on:

```
http://127.0.0.1:5000/
```

---

## 🔗 API Endpoint

### POST `/chat`

**Request Body (JSON):**

```json
{
  "message": "hello"
}
```

**Response (JSON):**

```json
{
  "reply": "Hello! How can I help you? 😊"
}
```

---

## 📌 Notes

* The ML model is trained **at application startup**
* Designed for learning and demonstration purposes
* Not optimized for large-scale production usage

---

## 🌱 Future Improvements

* Improve training data
* Add more intents
* Optimize model loading
* Add database support
* Deploy using Docker or cloud platforms

---

## 👨‍💻 Live Deployment

(https://intent-based-chatbot-poof.onrender.com)

---

## 👨‍💻 Author

Developed as a beginner-friendly **Flask + Machine Learning project**.

---

## 📜 License

This project is open-source and free to use for learning and experimentation.
