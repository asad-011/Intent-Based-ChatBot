from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from datetime import datetime
import re
import random

app = Flask(__name__)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


training_sentences = [

    "hello", "hi", "hey",
    "hello there", "hi there",
    "good morning", "good evening", "good afternoon",
    "hii", "heyy",

    "bye", "goodbye", "see you",
    "see you later", "talk to you later",
    "exit", "quit",

    "how are you", "how r u",
    "how are you doing", "how is it going",
    "are you fine",

    "what is your name", "who are you",
    "tell me your name", "what should i call you",

    "tell me a joke", "joke",
    "make me laugh", "say something funny",

    "time", "current time",
    "what is the time", "time now",
    "tell me the time",

    "date", "today date",
    "what is the date", "today's date",
    "tell me today's date",

    "help", "what can you do",
    "how can you help me",
    "what are your features",

    "thanks", "thank you",
    "thx", "thanks a lot",

    "ok", "okay", "cool",
    "nice", "great"
]

training_labels = [

    "greeting","greeting","greeting",
    "greeting","greeting",
    "greeting","greeting","greeting",
    "greeting","greeting",

    "bye","bye","bye",
    "bye","bye",
    "bye","bye",

    "status","status",
    "status","status",
    "status",

    "name","name",
    "name","name",

    "joke","joke",
    "joke","joke",

    "time","time",
    "time","time",
    "time",

    "date","date",
    "date","date",
    "date",

    "help","help",
    "help","help",

    "thanks","thanks",
    "thanks","thanks",

    "confirmation","confirmation","confirmation",
    "confirmation","confirmation"
]



vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)

model = LogisticRegression(max_iter=1000)
model.fit(X, training_labels)


responses = {
    "greeting": [
        "Hello! How can I help you? 😊",
        "Hi there! 👋",
        "Hey! Nice to see you.",
        "Greetings! What can I do for you?",
        "Hello! I'm here to assist you."
    ],

    "status": [
        "I'm doing great! Thanks for asking 😊",
        "All good here! How about you?",
        "I'm fine and ready to help!",
        "Doing well 👍"
    ],

    "name": [
        "I am an NLP chatbot built using Flask and Python 🤖",
        "You can call me your virtual assistant!",
        "I'm a simple AI chatbot here to help you.",
        "I don't have a name, but I'm always available for you."
    ],

    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs 😂",
        "Why did the computer go to the doctor? It caught a virus 😄",
        "Why was the math book sad? Too many problems 😆",
        "I told my computer I needed a break… it froze 😜"
    ],

    "help": [
        "I can chat with you, tell the time/date, and crack jokes!",
        "I can answer basic questions and keep you entertained 😊",
        "Try asking me about time, date, jokes, or greetings.",
        "I'm here to assist you however I can!"
    ],

    "bye": [
        "Goodbye! Have a great day 👋",
        "See you later!",
        "Bye! Take care 😊",
        "Hope to chat again soon!",
        "Farewell! 👋"
    ],

    "thanks": [
        "You're welcome! 😊",
        "No problem at all!",
        "Happy to help 👍",
        "Anytime!"
    ],

    "confirmation": [
        "Okay 👍",
        "Got it ✅",
        "Sure!",
        "Alright!",
        "Confirmed!"
    ]
}



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = clean_text(request.json.get("message", ""))

        if not user_input:
            return jsonify({"reply": "Please type something "})

        X_test = vectorizer.transform([user_input])
        intent = model.predict(X_test)[0]
        confidence = model.predict_proba(X_test).max()

        if confidence < 0.15:
            return jsonify({"reply": "Sorry, I didn't understand that. Can you rephrase?"})
        
        if intent == "time":
            reply = datetime.now().strftime("%H:%M:%S")
        elif intent == "date":
            reply = datetime.now().strftime("%d-%m-%Y")
        else:
            reply = random.choice(responses.get(intent, ["I'm not sure how to answer that."]))

        return jsonify({"reply": reply})

    except Exception:
        return jsonify({"reply": "Something went wrong. Please try again."})

if __name__ == "__main__":
    app.run()

