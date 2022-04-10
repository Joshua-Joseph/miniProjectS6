from flask import Flask, request, jsonify
from flask_cors import CORS

from core.sports.sportsTextPre import sportsUrlProcessor
from core.textPre import bullyUrlProcessor

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
    url = request_data["url"]
    print(url)
    # result = sportsUrlProcessor(url)
    result = bullyUrlProcessor(url)
    return jsonify({"success": True, "result": result})
