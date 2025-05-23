async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  addToChat("user", message);
  input.value = "";

  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, user_id: "user1" })
  });
  const data = await res.json();
  addToChat("bot", data.response);
}

function addToChat(role, message) {
  const box = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = role;
  div.textContent = message;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}
