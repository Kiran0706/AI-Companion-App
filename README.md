# AI-Companion-App
Personalized AI Companion built using LLM-based architecture with context-aware conversations, emotion handling, and fallback mechanisms.
#  AI Companion App

A friendly AI chat application that feels more like talking to a real person than a bot.  
It uses modern LLM-based architecture to understand context, emotions, and respond naturally.

---

**API key(for safty)**
key = AIzaSyB69I9zU3VjwIrGY-c-_CN3apAjsCIVYKI

**What it does..**

-  Keeps track of conversation (context-aware)
-  Understands simple emotions like happy, sad, confused
-  Responds in a human-like, friendly way
-  Handles API limits gracefully using fallback responses
-  Clean and simple chat interface

---

**Technologies used**

- Python (Flask) — backend
- HTML, CSS, JavaScript — frontend
- Gemini API — AI responses

---

**Working**

User message → Context memory → AI model → Response → Fallback (if needed)

---



**How to run the project**

**Start backend**
cd backend
py app.py

**Start Frontend**
cd frontend
py -m http.server 5500

**To open the interface **
http://localhost:5500
