import json
from pathlib import Path
from pdf_parser import extract_structure

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        try:
            output = extract_structure(pdf_file)
        except Exception as e:
            print(f"Failed to process {pdf_file.name}: {e}")
            continue

        output_path = output_dir / f"{pdf_file.stem}.json"
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Saved: {output_path.name}")

if __name__ == "__main__":
    print("Starting PDF processing...")
    process_pdfs()
    print("All PDFs processed.")
