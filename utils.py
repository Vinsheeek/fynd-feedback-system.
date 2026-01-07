import json
from pathlib import Path

# Resolve path based on file location (works everywhere)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "summary.json"

def load_summary():
    if not DATA_FILE.exists():
        print("⚠ Summary file NOT FOUND at:", DATA_FILE)
        return {}
    
    print("📂 Loading summary from:", DATA_FILE)
    return json.loads(DATA_FILE.read_text())
