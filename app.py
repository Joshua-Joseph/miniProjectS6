from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify(
        {
            "success": True,
            "message": "We verify urls! But this isn't the place where you should be verifying...",
        }
    )


@app.route("/verify", methods=["POST"])
def verify():
    request_data = request.get_json(force=True)
    tab_url = request_data["tab_url"]
    print(tab_url)
    return jsonify({"success": True, "results": ["safe", "safe", "unsafe", "safe"]})
