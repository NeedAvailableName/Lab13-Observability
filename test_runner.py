import json
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGFUSE_DEBUG"] = "true"
print("LANGFUSE_HOST:", os.getenv("LANGFUSE_HOST"))

from fastapi.testclient import TestClient
from app.main import app
from langfuse.decorators import langfuse_context
from langfuse import Langfuse

def run_tests():
    client = TestClient(app)
    queries_path = os.path.join("data", "sample_queries.jsonl")
    with open(queries_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            payload = json.loads(line)
            response = client.post("/chat", json=payload)
            print(f"[{response.status_code}] {response.json().get('correlation_id')}")
            
    # Force flush before exit
    try:
        langfuse_context.flush()
        print("Langfuse explicit flush completed.")
    except Exception as e:
        print(f"Langfuse flush error: {e}")

if __name__ == "__main__":
    run_tests()
