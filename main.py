from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import re, random

app = FastAPI(title="GymBuddy Chatbot")
@app.get("/")
def read_root():
    return {"message": "Welcome to GymBuddy API"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change this to ["http://localhost:5500"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default_user"

class ChatResponse(BaseModel):
    response: str
    conversation_history: List[Message]

conversations: Dict[str, List[Message]] = {}

def gymbuddy_response(msg: str) -> str:
    msg = msg.lower()

    if re.search(r"^hi|hello|hey$", msg):
        return "Welcome to GymBuddy! How may I help you?\n\nChoose an option:\n1. Exercises\n2. Cardio\n3. Diet\n4. Supplements\n5. Muscle Soreness"

    elif "1" in msg or "exercise" in msg:
        return (
            "Here's your weekly exercise plan:\n"
            "🟩 Monday - Back: Lat Pulldown, Dumbbell Row, T-Bar Row\n"
            "🟨 Tuesday - Chest: Bench Press, Incline Dumbbell Press, Cable Fly\n"
            "🟦 Wednesday - Legs: Squats, Leg Press, Lunges\n"
            "🟪 Thursday - Shoulders: Overhead Press, Lateral Raise, Rear Delt Fly\n"
            "🟥 Friday - Arms: Bicep Curls, Tricep Dips, Hammer Curl\n"
            "🟧 Saturday - Core: Planks, Russian Twists, Leg Raises\n"
            "🟫 Sunday - Rest or Light Stretching"
        )

    elif "2" in msg or "cardio" in msg:
        return ("Try these cardio exercises:\n"
        "-Brisk Walking\n"
        "-Jumping Jacks\n"
        "-Burpees\n" 
        "-Jump Squats\n"
        "-High Knees\n"
        )

    elif "3" in msg or "diet" in msg:
        return "Please enter your weight in kg (e.g., 'weight 70')"

    elif "weight" in msg:
        match = re.search(r"weight\s*(\d+)", msg)
        if match:
            weight = int(match.group(1))
            protein = weight * 2
            return f"Your daily protein requirement is ~{protein}g.\nAre you vegetarian or non-vegetarian?"
        else:
            return "Please provide your weight like: weight 70"

    elif "non-vegetarian" in msg:
        return (
        "🍗 *Non-Vegetarian Protein Sources:*\n"
        "- Eggs\n"
        "- Chicken Breast\n"
        "- Fish\n"
        "- Milk\n"
        "- Whey Protein"
    )

    elif "vegetarian" in msg:
        return (
        "🥦 *Vegetarian Protein Sources:*\n"
        "- Paneer\n"
        "- Tofu\n"
        "- Soya Chunks\n"
        "- Lentils & Chickpeas\n"
        "- Greek Yogurt"
    )


    elif "4" in msg or "supplement" in msg:
        return "Recommended Supplements:\n- Whey Protein\n- Creatine Monohydrate\n- Fish Oil\n- Multivitamins"

    elif "5" in msg or "sore" in msg:
        return "For muscle soreness:\n- Cold Showers\n- Hot Water Bag\n- Foam Rolling\n- Active Recovery\nSoreness reduces over time. Keep going!"

    return "Please choose an option (1-5) or type 'hello' to restart."

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user_message = Message(role="user", content=req.message)
    bot_message = Message(role="bot", content=gymbuddy_response(req.message))

    if req.user_id not in conversations:
        conversations[req.user_id] = []
    conversations[req.user_id].extend([user_message, bot_message])

    return ChatResponse(
        response=bot_message.content,
        conversation_history=conversations[req.user_id]
    )

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.delete("/reset/{user_id}")
def reset_conversation(user_id: str):
    conversations[user_id] = []
    return {"message": "Conversation reset."}
