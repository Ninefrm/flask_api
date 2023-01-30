from imports_exercise import *
from secrets_env import SECRET_KEY

def check_auth(request):
    api_key = request.headers.get("Authorization")
    return api_key == SECRET_KEY

@app.route("/authorize", methods=["GET"])
def authorize():
    authorized = check_auth(request)
    if authorized:
        return jsonify({"response": "Authorized"})
    return jsonify({"error": "Unauthorized"}), 401
