import json
import logging
import redis
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RedisDocumentIngestor:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.getenv('REDIS_HOST', 'localhost'),
            port=os.getenv('REDIS_PORT', 6379),
            db=os.getenv('REDIS_DB', 0),
            password=os.getenv('REDIS_PASSWORD', None),
            decode_responses=True
        )
        self.logger = logging.getLogger(__name__)

    def load_documents(self, file_path: str):
        """Load JSON documents from file"""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            self.logger.error(f"Error loading documents: {str(e)}")
            raise

    def ingest_to_redis(self, documents: list, key_prefix: str = "doc:"):
        """Ingest documents into Redis"""
        try:
            for idx, doc in enumerate(documents):
                # Create Redis key
                doc_id = doc.get('id', f"{key_prefix}{idx}")
                redis_key = f"{key_prefix}{doc_id}"

                # Store document as Redis hash
                self.redis_client.hset(redis_key, mapping=doc)
                self.logger.info(f"Inserted document: {redis_key}")

            self.logger.info(f"Successfully ingested {len(documents)} documents")
            return True
        except Exception as e:
            self.logger.error(f"Ingestion error: {str(e)}")
            return False

if __name__ == "__main__":
    ingestor = RedisDocumentIngestor()

    # Load sample data
    documents = ingestor.load_documents('src/sample_data.json')

    # Ingest into Redis
    if documents:
        success = ingestor.ingest_to_redis(documents, key_prefix="document:")
        if success:
            print("Data ingestion completed successfully!")
        else:
            print("Data ingestion failed. Check logs for details.")