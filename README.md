# Simple Redis Queue with Containers

This is an implementation of a Redis Queue using a **trigger** that sends the message to a **producer** which stores the message in the **redis queue** and then a **consumer** checks for new messages on it.

If a new message is in the queue, the **consumer** process it and sends it to the **ending API**.

## Requirements

- Python >= 3
- pip >= 19.2.3
- Docker >= 19.03.12
- Docker Compose >= 1.24.0

## Ports used

- Redis: 6379
- Producer: 11000
- Ending API: 12000

## Micro-services

1. Producer
1. Redis
1. Consumer
1. Ending API

## How to run

```bash
# Build the containers
docker-compose build

# Run the containers
docker-compose up

# Install trigger.py dependencies
pip install -r requirements.txt

# Send the message
python trigger.py
```

## Integrate this queue with your own container/micro-service/service

Inside the **docker-compose.yml**:

1. Change the **environment variable**: ENDING_API (Ex: name-of-your-container:port)

1. Change the **depends_on** with the name of your container (Ex: name-of-your-container)
