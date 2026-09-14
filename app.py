"""
🌀 THE CHAOS MACHINE 🌀
A completely unnecessary, database-free Flask app that exists purely
to generate chaos: roasts, fortunes, weird facts, screen-shake triggers,
and randomly-colored backgrounds. Nothing is persisted. Nothing is serious.
"""


import random
from datetime import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# In-memory "content" — no database, just Python lists living in RAM
# ---------------------------------------------------------------------------

ROASTS = [
    "You have the energy of a browser with 47 tabs open and none of them loading.",
    "You're like a software update — nobody wants you, but you appear anyway.",
    "If procrastination were a sport, you'd start training tomorrow.",
    "You bring everyone so much joy... when you leave the room.",
    "You're the human version of a CAPTCHA — mildly confusing and slightly annoying.",
    "I'd explain it again, but I already ran out of crayons.",
    "You have something on your chin... no, the 3rd one down.",
    "You're proof that evolution can, in fact, go backwards.",
]

FORTUNES = [
    "A great opportunity will disguise itself as a Monday.",
    "You will trip over nothing today, in front of someone important.",
    "Your Wi-Fi will disconnect at the most dramatic possible moment.",
    "Someone is about to reply-all to an email you shouldn't have sent.",
    "You will find exactly one sock today. Only one.",
    "A pop quiz on something you skimmed is imminent.",
    "You will say 'you too' when a waiter tells you to enjoy your meal.",
    "Your next great idea will arrive at 2am and vanish by 9am.",
]

FACTS = [
    "Bananas are berries, but strawberries aren't.",
    "A shrimp's heart is in its head.",
    "Octopuses have three hearts and blue blood.",
    "Honey never spoils. Archaeologists have eaten 3,000-year-old honey.",
    "Wombats poop in cubes.",
    "There are more possible chess games than atoms in the observable universe.",
    "Sea otters hold hands while sleeping so they don't drift apart.",
    "The inventor of the Pringles can is buried in one.",
]

CHAOS_TITLES = [
    "MAXIMUM CHAOS ACHIEVED",
    "REALITY.EXE HAS STOPPED RESPONDING",
    "CHAOS LEVEL: UNSTABLE",
    "YOU HAVE SUMMONED THE VOID",
    "ERROR 42: TOO MUCH VIBE",
]


def random_hex_color() -> str:
    return "#%06x" % random.randint(0, 0xFFFFFF)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chaos")
def api_chaos():
    """Returns a fresh bundle of nonsense every time it's called."""
    payload = {
        "title": random.choice(CHAOS_TITLES),
        "roast": random.choice(ROASTS),
        "fortune": random.choice(FORTUNES),
        "fact": random.choice(FACTS),
        "bg_color": random_hex_color(),
        "accent_color": random_hex_color(),
        "rotation": random.randint(-8, 8),
        "shake": random.choice([True, False]),
        "timestamp": datetime.now().strftime("%H:%M:%S"),
    }
    return jsonify(payload)


@app.route("/api/roast")
def api_roast():
    return jsonify({"roast": random.choice(ROASTS)})


@app.route("/api/fortune")
def api_fortune():
    return jsonify({"fortune": random.choice(FORTUNES)})


if __name__ == "__main__":
    # Debug mode on purpose — this app is chaotic, not production-grade.
    app.run(debug=True)
