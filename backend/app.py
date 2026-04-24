from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import generate_reply

app = Flask(__name__)
CORS(app)

# 🧠 conversation memory
memory = []

@app.route("/chat", methods=["POST"])
def chat():
    global memory

    message = request.json["message"]

    # store last 6 messages
    memory.append(message)
    memory = memory[-6:]

    reply = generate_reply(message, memory)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)