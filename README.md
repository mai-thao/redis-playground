# redis-playground

Redis is short for _Remote Dictionary Server_. It is a very fast, in-memory database commonly used as a cache. 
In this project, I demonstrate how it works with caching API responses. 

I created a super simple Flask app written in Python that checks Redis for a message, and if the message is there, it
sends that message back. Otherwise, it sends a default message and saves it into the cache for date retrieval. 

I set the Time To Live (TTL) to 5 seconds, which is the duration of the message in the cache before it gets automatically
deleted.

### Set Up
Before starting the app, you must have a Redis server running. Start the Redis server by using the `docker-compose.yml` 
file. I have another repo about Docker [here](https://github.com/mai-thao/docker-playground) if you want to learn more.

Executing `docker-compose up -d` on the terminal spins up a Docker container that runs a basic Redis server on port 6379
    
* `-d` option is for detached mode, which runs the container in the background

### Run the App
Now, the Flask app can be started. Make sure you're in the same directory as the `simple-app.py` script, and execute the command
`python simple-app.py`. The app should start up and be ready to accept HTTP requests.

* This implies that you have Python installed ready. If you don't, then install it at: https://docs.python.org/3/using/mac.html#using-python-for-macos-from-python-org

Open your browser of choice and navigate to the "/data" endpoint by going to: http://localhost:5000/data

Pay attention the `source` field. It indicates whether it grabbed the message from the cache or not. If you count for 5 
seconds, the `source` should change since 5 seconds is the TTL of the cache.

