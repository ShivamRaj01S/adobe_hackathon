# 📄 Challenge 1A: PDF Outline Extractor — Adobe Hackathon 2025

### 🔍 Theme: Connecting the Dots Through Docs

This solution extracts a **structured outline** from PDF files, including:
- **Title**
- **Headings**: H1, H2, H3
- **Page number** for each heading

The extracted data is saved in a clean **JSON** format, enabling smarter document understanding for downstream applications.

---

## 📁 Project Structure

```
Challenge_1a/
├── process_pdfs.py        # Main entry point
├── pdf_parser.py          # Logic to parse PDFs and determine heading levels
├── Dockerfile             # Container config to ensure platform compatibility
└── README.md              # You’re reading it!
```

---

## 🧠 Approach Summary

- Uses `pdfminer.six` to extract font sizes and layout metadata.
- Clusters text boxes by font size and style to infer heading levels (H1 > H2 > H3).
- Uses the **largest text block from page 1** as the document **title**.
- Cleans short or irrelevant text based on heuristics.
- Outputs structured JSON including:
  ```json
  {
    "title": "Document Title",
    "outline": [
      { "level": "H1", "text": "Main Heading", "page": 1 },
      { "level": "H2", "text": "Subsection", "page": 2 }
    ]
  }
  ```

---

## 🐳 How to Build the Docker Image

Run this command from inside the `Challenge_1a/` folder:

```bash
docker build --platform linux/amd64 -t pdf-extractor:v1 .
```

> 🔧 Note: Ensure you're using a Linux-compatible Docker environment (e.g., WSL or Docker Desktop).

---

## ▶️ How to Run the Container

Assuming this folder structure:

```
Challenge_1a/
├── sample_dataset/
│   ├── pdfs/         # Input PDFs (e.g., file01.pdf, file02.pdf...)
│   └── outputs/      # Output JSONs (e.g., file01.json...)
```

Use:

```bash
docker run --rm   -v $(pwd)/sample_dataset/pdfs:/app/input:ro   -v $(pwd)/sample_dataset/outputs:/app/output   --network none   pdf-extractor:v1
```

> 📝 All `.pdf` files in `/input` will be converted to `.json` outlines in `/output`.

---

## ✅ Output Format

Conforms to the schema:
```json
{
  "title": "Extracted title",
  "outline": [
    { "level": "H1", "text": "Section name", "page": 1 },
    { "level": "H2", "text": "Subsection", "page": 2 }
  ]
}
```

---

## 📦 Dependencies

- Python 3.10
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)

All dependencies are installed inside Docker.

---

## 📌 Notes

- **No network access is required.**
- Works on **CPU-only** systems.
- Supports PDFs up to **50 pages**.
- Processing time ≤ 10 seconds per file.

---

## 🏁 Final Tips

- Test with both simple and complex PDFs.
- Don't hardcode headings — detection is dynamic.
- Validate JSON output with `output_schema.json` (if required).