import json
import os
import redis
import requests
import time

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD =os.getenv("REDIS_PASSWORD")
REDIS_DB = os.getenv("REDIS_DB")
REDIS_QUEUE = os.getenv("REDIS_QUEUE")

ENDING_API = os.getenv("ENDING_API")

def consume_queue(redis_connection: redis.Redis, redis_queue: str) -> None:
    while True:
        try:
            packed = redis_connection.blpop([redis_queue], timeout=30)
        except Exception as error:
            print("Consumer failed to connect to Redis")
            # time.sleep(5000)
            packed = None

        if not packed:
            continue

        message = json.loads(packed[1])

        try:
            send_message(message)
        except Exception as error:
            print(f"Error: {error}. Failed to send message: {message}")
        else:
            print(f"Sent message: {message}")

def send_message(message: dict) -> None:
    requests.post(
        url=ENDING_API,
        json=message
    )

def main() -> None:
    redis_connection = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        db=REDIS_DB
    )
    consume_queue(redis_connection, REDIS_QUEUE)

if __name__ == "__main__":
    main()