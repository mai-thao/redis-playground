from flask import Flask, jsonify
import redis, logging

# Init a Flask app with the current script name "simple-app"
app = Flask(__name__)

# Set logger to highest INFO level so can see all log messages
logging.basicConfig(level=logging.INFO)

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
        app.logger.info('Data was served from the cache')
        return jsonify({"source": "cache", "data": cached_data.decode('utf-8')})
    else:
        app.logger.info('Data was not cached, caching it now')
        # If not found, return default response and cache it
        cache.setex(CACHE_KEY, CACHE_TTL, DEFAULT_RESPONSE["message"])
        return jsonify({"source": "default", "data": DEFAULT_RESPONSE["message"]})

if __name__ == "__main__":
    app.run() # Flask apps run on port 5000 by default
