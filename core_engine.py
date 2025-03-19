from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

def get_mistral_reply(prompt):
    """Generate AI response using Mistral via Ollama."""
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def home():
    return render_template("neural_link.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    ai_response = get_mistral_reply(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
