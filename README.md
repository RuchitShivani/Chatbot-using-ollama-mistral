NeuroChat: Fast Local AI Chatbot using Mistral + Ollama
NeuroChat is a local AI chatbot that runs on your machine using Mistral (an advanced LLM) via Ollama. It features a Flask backend and a simple HTML+JS frontend for interaction.

✨ Features
✅ Runs completely offline – No API keys, no internet required.
✅ Uses Ollama – Efficient LLM execution locally.
✅ Fast responses – Optimized for low-latency responses.
✅ Simple Web UI – Chat via a browser.

🚀 1. Install Dependencies
🛠 Step 1: Install Ollama
Download and install Ollama from the official site:
👉 Ollama Download

After installation, open a terminal (PowerShell) and pull the Mistral model:

powershell
Copy
Edit
ollama pull mistral
🛠 Step 2: Install Python & Flask
Ensure you have Python installed. Then, install Flask:

powershell
Copy
Edit
pip install flask
📂 2. Create the Project Directory
Open a PowerShell terminal and run:

powershell
Copy
Edit
mkdir NeuroChat
cd NeuroChat
🖥 3. Create the Backend (Flask Server)
🔹 Step 1: Create neuron_server.py
Inside NeuroChat, create a Python file:

powershell
Copy
Edit
New-Item neuron_server.py
Open it in VS Code:

powershell
Copy
Edit
code neuron_server.py
✏️ Paste the following code into neuron_server.py:
python
Copy
Edit
from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Function to interact with Mistral using Ollama
def get_ai_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return render_template("synapse.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("message", "")
    if not user_text:
        return jsonify({"error": "No message provided"}), 400
    
    response = get_ai_response(user_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
🌐 4. Create the Frontend (Web Interface)
🔹 Step 1: Create templates/synapse.html
First, create a templates directory:

powershell
Copy
Edit
mkdir templates
Now, create the HTML file:

powershell
Copy
Edit
New-Item templates/synapse.html
Open it in VS Code:

powershell
Copy
Edit
code templates/synapse.html
✏️ Paste the following code into templates/synapse.html:
html
Copy
Edit
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeuroChat - AI Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f8f8f8;
        }
        #chatbox {
            width: 50%;
            height: 400px;
            border: 1px solid black;
            overflow-y: auto;
            margin: auto;
            padding: 10px;
            text-align: left;
            background-color: white;
        }
        input, button {
            margin-top: 10px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>🧠 NeuroChat - Local AI Chatbot</h2>
    <div id="chatbox"></div>
    <input type="text" id="userInput" placeholder="Type a message..." onkeypress="handleKeyPress(event)" />
    <button id="sendButton">Send</button>

    <script>
        document.getElementById("sendButton").addEventListener("click", sendMessage);

        function handleKeyPress(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        }

        function sendMessage() {
            let userInputField = document.getElementById("userInput");
            let chatbox = document.getElementById("chatbox");
            let userInput = userInputField.value.trim();

            if (!userInput) return;

            chatbox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;
            userInputField.value = "";

            fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput })
            })
            .then(response => response.json())
            .then(data => {
                chatbox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => {
                console.error("Error:", error);
                chatbox.innerHTML += `<p><b>Bot:</b> Error communicating with the server.</p>`;
            });
        }
    </script>
</body>
</html>
▶️ 5. Run the Chatbot
Step 1: Start Ollama
Ensure Ollama is running:

powershell
Copy
Edit
ollama serve
Step 2: Run the Flask Server
In another terminal, navigate to the NeuroChat folder:

powershell
Copy
Edit
cd NeuroChat
python neuron_server.py
Step 3: Open the Chatbot in Browser
Go to:
👉 http://127.0.0.1:5000

Now, chat with the bot! 🎉

🛠 6. Debugging & Fixes
✅ Issue: "Unknown flag: --system"
Fix: The --system flag doesn’t work in CLI. Instead, pass system instructions as part of the prompt.

✅ Issue: Flask App Not Running?
Ensure Python is installed (python --version).
Ensure Flask is installed (pip install flask).
✅ Issue: Ollama Not Responding?
Ensure Ollama is running (ollama serve).
If using a GPU, check compatibility.
🎯 Why Use This?
✅ No API Keys Required – Runs locally.
✅ Fast Responses – Optimized for minimal delay.
✅ Easy Web UI – No CLI knowledge needed.
✅ Fully Private – No data leaves your system.

📜 License
This project is open-source and free to use and easy to implement! 🚀

🔥 Try it & Give a Star ⭐
If you like this, consider giving it a ⭐ on GitHub!

![Screenshot 2025-03-19 084447](https://github.com/user-attachments/assets/40d71bd3-c810-4986-8173-271e8e9a5a99)
![Screenshot 2025-03-19 084515](https://github.com/user-attachments/assets/9387b7b0-9655-41e8-b956-cbb9b4cf75b1)
![Screenshot 2025-03-19 084504](https://github.com/user-attachments/assets/ade28a78-6046-4264-8726-7240f4cd75b9)

