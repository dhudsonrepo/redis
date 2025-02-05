# Real-Time Chat Application & Leaderboard System with Redis

This project implements a **Real-Time Chat Application** using Redis Pub/Sub and a **Leaderboard System** using Redis sorted sets.

## Features

- **Real-Time Chat**: A basic chat system where messages are broadcast to all users in real-time using Redis Pub/Sub.
- **Leaderboard**: A system to track user scores and display the top scorers using Redis sorted sets.

## Requirements

- Python 3.x
- Redis server (local or remote)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/dhudsonrepo/chat-leaderboard-redis.git
    cd chat-leaderboard-redis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start Redis server on `localhost:6379` or configure the `config/settings.py` for a remote Redis server.


4. Run the application:
    ```bash
    python main.py
    ```

## Testing

You can run tests for both the chat and leaderboard systems:
```bash
  python -m unittest discover tests/
```

