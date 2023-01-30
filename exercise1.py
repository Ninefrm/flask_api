from imports_exercise import *

@app.route("/ping")
def ping():
    return jsonify({"response": "ping"}), 200
