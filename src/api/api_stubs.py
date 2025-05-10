# /src/api/api_stubs.py

"""
REST API stubs for the Eden Protocol backend.
Simulates endpoints for frontend access (mobile/web) to symbolic systems:
- Avatar identity
- Tree of Life
- Quests
- XP tracking
- DAO proposals
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data (reused from simulation)
from sim.mobile_ui_simulation import generate_user_state

# Initialize static user state for now
user_state = generate_user_state()

@app.route("/api/avatar", methods=["GET"])
def get_avatar():
    return jsonify(user_state["avatar"])

@app.route("/api/tree", methods=["GET"])
def get_tree_of_life():
    return jsonify(user_state["tree_of_life"])

@app.route("/api/quest", methods=["GET"])
def get_current_quest():
    return jsonify(user_state["edenquest"])

@app.route("/api/meritcoin", methods=["GET"])
def get_merit_status():
    return jsonify(user_state["meritcoin"])

@app.route("/api/dao", methods=["GET"])
def get_dao_proposal():
    return jsonify(user_state["dao"])

@app.route("/api/world", methods=["GET"])
def get_world_tree():
    return jsonify(user_state["world_tree"])

@app.route("/api/sync", methods=["POST"])
def sync_biometric_data():
    data = request.json
    # This is where you'd process and update symbolic traits from real biometric input
    return jsonify({"message": "Biometric sync successful", "received": data}), 200

if __name__ == "__main__":
    app.run(debug=True)
