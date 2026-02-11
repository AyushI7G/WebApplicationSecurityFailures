from flask import request, jsonify
from flask_login import login_required, current_user
from auth import authenticate

def register_routes(app):

    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        if authenticate(data.get("username")):
            return jsonify({"status": "logged_in"})
        return jsonify({"status": "failed"}), 401

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return jsonify({"role": current_user.role})

    @app.route("/admin")
    @login_required
    def admin():
        if current_user.role != "admin":
            return jsonify({"error": "forbidden"}), 403
        return jsonify({"secret": "admin_data"})
