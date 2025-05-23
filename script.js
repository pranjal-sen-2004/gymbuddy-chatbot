async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addToChat("user", message);
  input.value = "";

  try {
    const res = await fetch("https://gymbuddy-api.onrender.com/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, user_id: "user1" })
    });

    if (!res.ok) {
      // If response status not 2xx, throw error to catch block
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();
    addToChat("bot", data.response);

  } catch (error) {
    console.error("Error in sending message:", error);
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

// Event listener for Send button click
document.getElementById("send-btn").addEventListener("click", sendMessage);

// Event listener for Enter key in input box
document.getElementById("user-input").addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    e.preventDefault();
    sendMessage();
  }
});
