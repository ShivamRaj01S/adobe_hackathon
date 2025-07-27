import os
from difflib import SequenceMatcher
from datetime import datetime
from modules.pdf_parser import extract_text_from_pdfs
from modules.utils import load_json

def most_similar(question, lines):
    best_ratio = 0
    best_match = "Not Found"
    for line in lines:
        ratio = SequenceMatcher(None, question.lower(), line.lower()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = line
    return best_match

def analyze_collection(collection_path):
    # Load input
    input_path = os.path.join(collection_path, "input.json")
    input_data = load_json(input_path)

    # Get PDFs and extract text
    pdf_folder = os.path.join(collection_path, "PDFs")
    pdf_filenames = sorted(os.listdir(pdf_folder))
    full_text = extract_text_from_pdfs(pdf_folder)
    lines = full_text.splitlines()

    # Simulated ranking logic (replace with real logic if needed)
    extracted_sections = []
    for idx, filename in enumerate(pdf_filenames[:5]):  # take top 5 for now
        extracted_sections.append({
            "document": filename,
            "section_title": f"Auto Section Title {idx+1}",
            "importance_rank": idx + 1,
            "page_number": idx + 1  # dummy values
        })

    # Simulated refined section content
    subsection_analysis = []
    for i, sec in enumerate(extracted_sections):
        subsection_analysis.append({
            "document": sec["document"],
            "refined_text": f"Extracted insights from {sec['section_title']}",
            "page_number": sec["page_number"]
        })

    return {
        "metadata": {
            "input_documents": pdf_filenames,
            "persona": input_data.get("persona", {}).get("role", "N/A"),
            "job_to_be_done": input_data.get("job_to_be_done", {}).get("task", "N/A"),
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
