# GymBuddy 🏋️‍♂️💬

GymBuddy is a simple, interactive chatbot for gym assistance. It helps users with:
- 🏋️ Weekly workout routines
- 💓 Cardio exercises
- 🍽️ Diet planning based on weight and diet type
- 💊 Supplement suggestions
- 🧊 Muscle soreness relief tips

---

## 🚀 Live Demo

🖥️ [Try GymBuddy Online](https://pranjal-sen-2004.github.io/gymbuddy-chatbot/)

---

## ⚙️ Backend API

Hosted on Render: [https://gymbuddy-chatbot.onrender.com](https://gymbuddy-chatbot.onrender.com)

- `/chat`: POST endpoint to get chatbot response
- `/ping`: GET for health check

---

## 📂 How to Run Locally

```bash
git clone https://github.com/pranjal-sen-2004/gymbuddy-chatbot.git
cd gymbuddy-chatbot
pip install -r requirements.txt
uvicorn main:app --reload
