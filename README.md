# ✈️ AVIATRACK: A Blockchain-Enabled Flight Duty Time Limitations (FDTL) Management System

Aviatrack is a blockchain-based web application designed to manage and monitor **Flight Duty Time Limitations (FDTL)** for pilots. It ensures transparency, accountability, and compliance with aviation regulations by securely recording pilot duty logs on an immutable ledger.

---

## 🚀 Project Overview

Flight Duty Time Limitations (FDTL) are crucial to ensure pilots get adequate rest and operate safely. Traditional FDTL systems often lack tamper-proof mechanisms and can be inefficient.

**AVIATRACK** solves this problem by:
- Providing a user-friendly interface for logging pilot duties.
- Using blockchain to store duty logs immutably.
- Checking FDTL violations in real-time.
- Supporting airlines in adhering to safety norms.

---

## 🧠 Key Features

- ✅ **Pilot Duty Logging**: Enter duty start/end times securely.
- 🔐 **Blockchain Ledger**: Tamper-proof duty log records stored in a local blockchain.
- 📊 **FDTL Checker**: Alerts if logged hours exceed allowed limits.
- 🌐 **Frontend-Backend Integration**: React + Flask architecture.
- 🛢️ **Database Support**: Uses SQLite to store structured data.
- 🧪 **Error Handling**: Simple validation and exception management.
- 📜 **Readable Codebase**: Organized folder structure for easy navigation.

---

## 🛠️ Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Frontend      | React                    |
| Backend       | Flask (Python)           |
| Blockchain    | Custom JSON-based chain  |
| Database      | SQLite                   |
| Deployment    | (Optional: Heroku, Render) |
| Others        | Axios, HTML/CSS, JS      |

---

## 📂 Project Structure

AVIATRACK/

├── aviatrack-frontend/       # React frontend

├── templates/                # HTML templates (Flask rendering)

├── static/                   # Static files (CSS, JS)

│

├── app.py                    # Flask entry point

├── blockchain.py             # Blockchain logic

├── fdtl_checker.py           # FDTL rules & logic

├── models.py                 # Data models

├── init_db.py                # DB setup script

├── blockchain_ledger.json    # Ledger data

├── *.db                      # SQLite databases

├── requirements.txt          # Python dependencies

└── README.md                 # You're reading it 😄

---

## 🧪 How to Run Locally



### 📥 Backend Setup

---

git clone [https://github.com/yourusername/aviatrack.git](https://github.com/yourusername/aviatrack.git)

cd aviatrack

pip install -r requirements.txt

python init_db.py  # Initialize the database

python app.py      # Start Flask server

---

### 🌐 Frontend Setup (React)

---

cd aviatrack-frontend

npm install

npm start

Visit: http://localhost:3000 to interact with the frontend.

---

## 🔐 Security & Blockchain
Aviatrack stores duty logs in an append-only blockchain file (blockchain_ledger.json). Each record:

Is hashed using SHA-256

Includes previous hash links

Ensures tamper-evidence

This enables transparent auditability.

---

## 💬 Future Enhancements

🔒 JWT Authentication for user login

📤 Cloud database & blockchain storage

📈 Admin dashboard with analytics

☁️ One-click deployment with CI/CD

---

## 👨‍💻 Authors

Hemanth — B.Tech Final Year (CSE)

Team Aviatrack | 2025

---

## 📃 License

This project is licensed for academic and educational purposes.

---

## ⭐ Give It a Star!

If you found this project helpful or interesting, don’t forget to ⭐ star the repo and share it with your network!