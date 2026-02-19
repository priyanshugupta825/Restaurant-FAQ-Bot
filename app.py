from flask import Flask, request, jsonify, render_template, session
from groq import Groq
import os
import uuid

app = Flask(__name__)
app.secret_key = "mysecretkey123"

# ── API key from environment variable ──────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
# ──────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a helpful FAQ assistant for "Hotel New Guru Deo Basera".
Only answer questions related to the restaurant.

MENU (prices in Indian Rupees ₹):

STARTERS:
- Tomato Soup (V, GF) - ₹120
- Garlic Bread (V) - ₹80
- Chicken Wings (GF) - ₹220
- Bruschetta (V) - ₹150

MAINS:
- Grilled Salmon (GF, DF) - ₹480
- Margherita Pizza (V) - ₹300
- Mushroom Risotto (V, GF) - ₹320
- Grilled Chicken (GF, DF) - ₹380
- Vegan Pasta (VG, DF) - ₹280

DESSERTS:
- Chocolate Lava Cake (V) - ₹180
- Fruit Sorbet (VG, GF, DF) - ₹130
- Cheesecake (V) - ₹160

DRINKS:
- Fresh Juices - ₹80
- Soft Drinks - ₹60
- Coffee/Tea - ₹60

DIETARY CODES: V=Vegetarian | VG=Vegan | GF=Gluten-Free | DF=Dairy-Free

RESTAURANT INFO:
- Hours: Mon-Thu 11am-10pm | Fri-Sat 11am-11pm | Sun 12pm-9pm
- Reservations: Call (555) 123-4567
- Location: 123 Main Street, Downtown
- Parking: Free parking behind restaurant
- Payment: Cash, Card, UPI accepted

ALLERGY POLICY:
- Inform staff of allergies before ordering
- Kitchen handles nuts, dairy and gluten

Always mention prices in ₹. Be short and helpful."""


@app.route("/")
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    history = data.get("history", [])

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if not GROQ_API_KEY:
        return jsonify({"error": "API key not set. Please set GROQ_API_KEY environment variable."}), 500

    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for turn in history:
            if turn.get("role") in ("user", "assistant"):
                messages.append({"role": turn["role"], "content": turn["content"]})
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


if __name__ == "__main__":
    print("🚀 Hotel New Guru Deo Basera FAQ Bot running at http://localhost:5000")
    app.run(debug=True, port=5000)