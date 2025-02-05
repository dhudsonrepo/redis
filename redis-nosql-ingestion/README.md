# Redis NoSQL Document Ingestion

A Python solution for ingesting JSON documents into Redis with proper data modeling.

## Features
- Document Ingestion: Securely stores JSON documents in Redis using hash data structures
- Cloud-Ready: Configured for local development with Docker and environment variables
- Error Handling: Comprehensive logging and exception management
- Scalable Design: Modular architecture for easy extension

## System Requirements
- Python 3.8 or newer
- Docker Desktop (or equivalent container runtime)
- Git version control system
- Redis server (included via Docker)

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dhudsonrepo/redis.git
    cd redis-nosql-ingestion
    ```

2. **Create a `.env` file for environment variables**:
   Create a `.env` file in the root directory of the project with the following content:
    ```dotenv
    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_DB=0
    REDIS_PASSWORD=mysecretpassword
    ```

3. **Start the Redis container**:
   Use Docker Compose to start a Redis instance in a container:
    ```bash
    docker-compose up -d
    ```

4. **Install dependencies**:
   Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

5. **Modify the sample data**:
   Store JSON documents in `src/sample_data.json` following the format:
    ```json
    [
        {
            "id": "unique_id",
            // ... other fields
        }
    ]
    ```

6. **Run the ingestion script**:
   Run the `data_ingestor.py` script to ingest the data into Redis:
    ```bash
    python src/data_ingestor.py
    ```
   
## Data Modeling Approach
 **Documents are stored as Redis hashes using this key pattern:**
 ```
 document:<unique_id>:
  ├── field1: value
  ├── field2: value
  └── nested_field:
      ├── sub_field1: value
      └── sub_field2: value
 ```

## Troubleshooting
- Connection Issues: Verify Docker container status and .env credentials
- Data Errors: Check JSON formatting in sample_data.json
- Dependency Conflicts: Use virtual environments for package isolation