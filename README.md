# redis-playground

[Redis](https://redis.io) is short for _Remote Dictionary Server_. It is a very fast, in-memory database commonly used as a cache. 
In this project, I demonstrate how it works with caching API responses. 

## Simple App
I created a super simple Flask app written in Python that has one endpoint. When that endpoint is called, it checks Redis for a message, and if the message is there, it sends that message back. Otherwise, it sends a default message instead and saves it into the cache for retrievel later.

The Time To Live (TTL) is set to a short 5 seconds. TTL is the duration of the message in the cache before it gets automatically
deleted.

### Set Up
Before starting the app, you must have a Redis server running. Start the Redis server by using the `docker-compose.yml` 
file. I have another repo about Docker [here](https://github.com/mai-thao/docker-playground) if you want to learn more.

Executing `$ docker compose up -d` on the terminal spins up a Docker container that runs a basic Redis server on port 6379
    
* `-d` option is for detached mode, which runs the container in the background

### Run the App
Now, the Flask app can be started. Make sure you're in the same directory as the `simple-app.py` script, and execute the command
`$ python simple-app.py`. The app should start up and be ready to accept HTTP requests.

* This implies that you have Python installed ready. If you don't, then install it at: https://docs.python.org/3/using/mac.html#using-python-for-macos-from-python-org

Open your browser of choice and navigate to the "/data" endpoint by going to: http://localhost:5000/data

Pay attention the `source` field. It indicates whether it grabbed the message from the cache or not. If you count for 5 
seconds, the `source` should change since 5 seconds is the TTL of the cache.

## Redis CLI
The "redis-cli" is the command-line client that lets you connect to and interact with the Redis server. You can access, create, update, or delete cached data. 

Since you already have the Redis server running in Docker, you don't need to manually start one with the command `$ redis-server`.  You can jump straight to using the client.

1) Install the redis-cli tool from [Homebrew](https://brew.sh/): `$ brew install redis`
2) Locally connect to the Redis standalone instance with: `$ redis-cli -h localhost -p 6379`

Alternatively, you can run the CLI tool directly inside the container:
1) Find the Redis container ID by executing: `$ docker ps -a`
2) Execute: `$ docker exec -it <CONTAINER_ID> redis-cli`
3) If successfully connected, you'll see the output: `127.0.0.1:6379> `
4) Interact and play around with Redis
5) When you're done, log out with `$ exit`

### redis-cli Commands
```
$ ping
Should get PONG as response to indicate the client successfully connected to the server

$ ping hello
Should get "hello" output back

$ set 1 "hello" nx
Create a key of int type 1 associated with the value of string type "hello"
-nx option ONLY creates a new key if Not eXisting
-xx is the oposite. Only creates a new key if new key EXists aka an override

$ set name "mai"
Create a new key called name associated with the value "mai"

$ keys *
Show all the keys matching ANY pattern and its count

$ get 1
Returns the value associated with the key, which should be "hello" (set from earlier)

$ del 1 name
Deletes the (key,value) of (1,name), will also output # of deleted keys

$ exists 1 name
Return if these keys exist. Returns 0 if not

$ set abc “hello” ex 10
Create a new key and set the TTL of it to expire in 10 seconds (the EX is in seconds)

$ ttl abc
Get the TTL in seconds remaining until expired
- Returns -1 if it didn't have a TTL set in the first place
- Returns -2 if it had a TTL that has expired
```
