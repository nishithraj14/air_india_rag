const chatBox = document.getElementById("chat-box");
const input = document.getElementById("question-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.className = `message ${sender}`;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const question = input.value.trim();
    if (!question) return;

    addMessage(question, "user");
    input.value = "";

    const thinkingMsg = document.createElement("div");
    thinkingMsg.className = "message bot";
    thinkingMsg.innerText = "Thinking...";
    chatBox.appendChild(thinkingMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        chatBox.removeChild(thinkingMsg);
        addMessage(data.answer, "bot");

    } catch (error) {
        chatBox.removeChild(thinkingMsg);
        addMessage("An error occurred. Please try again.", "bot");
    }
}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});
