from flask import Flask, jsonify, request

app = Flask(__name__)

PROGRAMS = [
    {
        "id": 1,
        "name": "Weight Loss",
        "duration_weeks": 8,
        "sessions_per_week": 4
    },
    {
        "id": 2,
        "name": "Muscle Gain",
        "duration_weeks": 12,
        "sessions_per_week": 5
    },
    {
        "id": 3,
        "name": "General Fitness",
        "duration_weeks": 6,
        "sessions_per_week": 3
    }
]

clients = []


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "application": "ACEest Fitness & Gym",
            "status": "running",
            "message": "Welcome to the ACEest Fitness & Gym API"
        }
    ), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/programs", methods=["GET"])
def get_programs():
    return jsonify(PROGRAMS), 200


@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients), 200


@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    name = data.get("name")
    email = data.get("email")
    program_id = data.get("program_id")

    if not name or not email or program_id is None:
        return jsonify(
            {"error": "name, email and program_id are required"}
        ), 400

    selected_program = next(
        (program for program in PROGRAMS if program["id"] == program_id),
        None
    )

    if selected_program is None:
        return jsonify({"error": "Invalid program_id"}), 400

    client = {
        "id": len(clients) + 1,
        "name": name,
        "email": email,
        "program": selected_program["name"]
    }
    clients.append(client)

    return jsonify(client), 201


@app.route("/calories", methods=["POST"])
def calculate_calories():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must contain JSON data"}), 400

    try:
        weight_kg = float(data["weight_kg"])
        duration_minutes = float(data["duration_minutes"])
        intensity = data.get("intensity", "moderate").lower()
    except (KeyError, TypeError, ValueError):
        return jsonify(
            {"error": "weight_kg and duration_minutes must be valid numbers"}
        ), 400

    intensity_factors = {
        "low": 0.05,
        "moderate": 0.08,
        "high": 0.11
    }

    if intensity not in intensity_factors:
        return jsonify(
            {"error": "intensity must be low, moderate or high"}
        ), 400

    estimated_calories = round(
        weight_kg * duration_minutes * intensity_factors[intensity],
        2
    )

    return jsonify(
        {
            "weight_kg": weight_kg,
            "duration_minutes": duration_minutes,
            "intensity": intensity,
            "estimated_calories": estimated_calories
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
