def detect_intent(message):
    msg = message.lower()

    if any(w in msg for w in ["hi", "hello", "hey"]):
        return "greeting"

    if any(w in msg for w in ["good", "not bad", "fine"]):
        return "positive"

    if any(w in msg for w in ["sad", "alone", "lonely", "feel"]):
        return "emotional"

    if any(w in msg for w in ["no", "nothing"]):
        return "short_reply"

    if any(w in msg for w in ["confused", "double minded", "not sure"]):
        return "confused"

    if any(w in msg for w in ["eat", "ice cream", "food"]):
        return "casual"

    return "general"


def detect_sentiment(message):
    msg = message.lower()

    if any(w in msg for w in ["sad", "depressed"]):
        return "negative"

    if any(w in msg for w in ["happy", "good"]):
        return "positive"

    return "neutral"