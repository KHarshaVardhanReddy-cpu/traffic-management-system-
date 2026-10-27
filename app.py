from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from traffic import TrafficManager

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

traffic = TrafficManager()

# Home - serves the dashboard directly
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# API status endpoint
@app.route("/api/status")
def status():
    return jsonify({
        "message": "Smart Traffic Management System Backend",
        "status": "Running"
    })


# Get traffic information
@app.route("/api/traffic", methods=["GET"])
def get_traffic():
    return jsonify(traffic.get_status())


# Update vehicle count
@app.route("/api/traffic", methods=["POST"])
def update_traffic():
    data = request.json or {}

    road = data.get("road")
    vehicles = data.get("vehicles")

    if road not in [1, 2, 3, 4]:
        return jsonify({"error": "Road must be between 1 and 4"}), 400

    if not isinstance(vehicles, int) or vehicles < 0:
        return jsonify({"error": "Invalid vehicle count"}), 400

    traffic.update_vehicles(road, vehicles)

    return jsonify({
        "message": "Traffic updated successfully",
        "data": traffic.get_status()
    })


# Automatic traffic control
@app.route("/api/control", methods=["POST"])
def automatic_control():
    result = traffic.select_signal()
    return jsonify(result)


# Emergency vehicle priority
@app.route("/api/emergency", methods=["POST"])
def emergency():
    data = request.json or {}
    road = data.get("road")

    if road not in [1, 2, 3, 4]:
        return jsonify({"error": "Invalid road"}), 400

    result = traffic.emergency_priority(road)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
