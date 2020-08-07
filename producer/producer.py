import json
import os
import redis
from flask import Flask, request

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD =os.getenv("REDIS_PASSWORD")
REDIS_DB = os.getenv("REDIS_DB")
REDIS_QUEUE = os.getenv("REDIS_QUEUE")

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        json_message = request.json

        redis_connection = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            db=REDIS_DB
        )
        try:
            redis_connection.rpush(REDIS_QUEUE, json.dumps(json_message))
        except Exception as error:
            return {"error": str(error)}, 500

        return {"status": "ok"}, 200
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run()
