import requests

API_KEY = "AIzaSyDtcsykZwafvqQe2KVM9YNfsJoEAmlHF8c"
MODEL = "models/gemini-2.5-flash"


def generate_reply(message, memory):

    # 🧠 convert memory to context
    context = "\n".join(memory)

    prompt = f"""
    You are a friendly AI companion.

    Conversation:
    {context}

    User: {message}

    Instructions:
    - Understand user naturally (no rules)
    - Respond like a real human friend
    - Be emotionally aware
    - Answer questions clearly
    - Continue conversation smoothly
    - Keep replies short (1-2 lines)
    - Avoid repeating phrases
    """

    url = f"https://generativelanguage.googleapis.com/v1/{MODEL}:generateContent?key={API_KEY}"

    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()

        print("API:", result)

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("ERROR:", e)

    # 🛟 fallback (VERY IMPORTANT)
    return "I’m here with you 😊"