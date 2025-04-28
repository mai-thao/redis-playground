from flask import Flask, jsonify
import redis

# Init a Flask app with the current script name "simple-app"
app = Flask(__name__)

# Connect to Redis on port 6379
cache = redis.Redis(host='localhost', port=6379)

# Cache constants
CACHE_KEY = "my_key"
DEFAULT_RESPONSE = {"message": "Hello World!"}
CACHE_TTL = 5 # seconds

# Create the "/data" endpoint
@app.route('/data', methods=['GET'])
def get_data():
    # Try to get the data from Redis
    cached_data = cache.get(CACHE_KEY)

    if cached_data:
        return jsonify({"source": "cache", "data": cached_data.decode('utf-8')})
    else:
        # If not found, return default response and cache it
        cache.setex(CACHE_KEY, CACHE_TTL, DEFAULT_RESPONSE["message"])
        return jsonify({"source": "default", "data": DEFAULT_RESPONSE["message"]})

if __name__ == "__main__":
    app.run() # Flask apps run on port 5000 by default
