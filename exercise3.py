from imports_exercise import *
from exercise2 import check_auth
from flask_caching import Cache
import sqlite3
import json
# Configure the cache
cache = Cache(app, config={'CACHE_TYPE': 'memcached', 'CACHE_MEMCACHED_SERVERS': ['localhost:11211']})

# Connect to the database
conn = sqlite3.connect("data.db", check_same_thread=False)

cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL
)
""")
conn.commit()

@app.route("/save", methods=["POST"])
def save_data():
    authorized = check_auth(request)
    if not authorized:
        return jsonify({"error": "Unauthorized"}), 401

    # Get the data from the request body
    data_id, data_data = request.json.get("id"), request.json.get("data")
    # Check if the id exist
    cursor.execute("""
    SELECT id FROM data WHERE id = ?
    """, (data_id,))
    result = cursor.fetchone()
    # Return an error response if the id doesn't exist
    if result:
        return jsonify({"error": "Data exist"}), 400
    # Add the data to the database
    cursor.execute("""
    INSERT INTO data (id, data)
    VALUES (?,?)
    """, (data_id,data_data,))
    conn.commit()

    # Delete the cache
    cache.delete("data")

    return jsonify({"response": "Data saved"})

@app.route("/get", methods=["GET"])
def get_data():
    authorized = check_auth(request)
    if not authorized:
        return jsonify({"error": "Unauthorized"}), 401
    
    # Check if the data is in cache
    data = cache.get("data")
    if data:
        return jsonify({"response": data})

    # If the data is not in cache, fetch it from the database
    cursor.execute("""
    SELECT data FROM data
    """)
    data = [row[0] for row in cursor.fetchall()]
    cache.set("data", data)
    return jsonify({"response": data})

@app.route("/delete", methods=["DELETE"])
def delete_data():
    authorized = check_auth(request)
    if not authorized:
        return jsonify({"error": "Unauthorized"}), 401

    # Get the id of the data to be deleted
    data_id = request.json.get("id")
    
    # Check if the id exists in the database
    # Get the data from the request body
    cursor.execute("""
    SELECT id FROM data WHERE id = ?
    """, (data_id,))
    result = cursor.fetchone()
    # Return an error response if the id doesn't exist
    if not result:
        return jsonify({"error": "Invalid id"}), 400

    # Remove the data from the database
    cursor.execute("""
    DELETE FROM data
    WHERE id = ?
    """, (data_id,))
    conn.commit()

    # Delete the cache
    cache.delete("data")

    return jsonify({"response": "Data deleted"})

# extra, to perfomance E2E
@app.route("/setup", methods=["GET"])
def setup():
    authorized = check_auth(request)
    if not authorized:
        return jsonify({"error": "Unauthorized"}), 401
    # Delete all data from the database
    cursor.execute("DELETE FROM data")
    conn.commit()

    # Delete the cache
    cache.delete("data")

    return jsonify({"response": "Database cleared"})