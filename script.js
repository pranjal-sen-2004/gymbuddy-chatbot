const API_URL = "https://gymbuddy-api.onrender.com/chat";

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addToChat("user", message);
  input.value = "";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, user_id: "user1" })
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);

    const data = await res.json();
    addToChat("bot", data.response);
  } catch (err) {
    console.error("Fetch error:", err);
    addToChat("bot", "Oops! Something went wrong. Please try again.");
  }
}

function addToChat(role, message) {
  const box = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = role;
  div.textContent = message;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}

// Optional: Send message on Enter key
document.getElementById("user-input").addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    e.preventDefault();
    sendMessage();
  }
});
