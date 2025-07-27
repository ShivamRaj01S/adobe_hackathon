import os
import json
from modules.qa_engine import analyze_collection
from modules.utils import get_collections, save_json

def main():
    base_data_dir = "./data"
    collections = get_collections(base_data_dir)

    for collection_path in collections:
        print(f"⚙️ Processing {collection_path}...")
        result = analyze_collection(collection_path)
        output_path = os.path.join(collection_path, "output.json")
        save_json(result, output_path)
        print(f"✅ Done: {collection_path}")

if __name__ == "__main__":
    main()
