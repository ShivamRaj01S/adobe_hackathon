
# 📄 Document AI Challenge 1B – PDF Question Answering Engine

This project automates answering questions from PDF documents. It extracts textual data from PDFs and matches each question with the most relevant answer line using fuzzy matching.

---

## 📁 Directory Structure

```
challenge_1b/
├── Dockerfile
├── main.py
├── README.md
├── data/
│   └── collection1/
│       ├── PDFs/
│       │   └── *.pdf
│       ├── input.json
│       └── output.json (will be generated)
├── module/
│   ├── __init__.py
│   ├── pdf_parser.py
│   ├── qa_engine.py
│   ├── task_handler.py
│   └── utils.py
```

---

## ⚙️ How It Works

1. **PDF Parsing** – Extracts text from PDF files using PyMuPDF.
2. **Question Answering** – Matches each input question to the most similar sentence from the PDF text.
3. **Output Generation** – Saves the best-matched answers in an `output.json` file next to the input.

---

## 📦 Requirements

> ✅ You **do not need to install anything** if you're using Docker. Everything runs inside the container.

Otherwise, for local development:

```bash
pip install PyMuPDF
```

---

## 🐳 Running with Docker

### Step 1: Build Docker Image

Run this in the root of the `challenge_1b/` directory:

```bash
docker build -t documentai:shivamv1 .
```

### Step 2: Prepare Your Input

Inside the `data/` directory, create a subfolder like `collection1/` containing:

- A folder `PDFs/` with your PDF files.
- An `input.json` file like:

```json
[
  "What is the invoice number?",
  "Who is the client?",
  "What is the total amount?"
]
```

### Step 3: Run the Container

```bash
docker run --rm -v "$(pwd)/data:/app/data" --network none documentai:shivamv1
```

📂 After running, you’ll get an `output.json` file inside the same `collection1/` folder.

---

## 🧠 Example

### 📥 Input (`input.json`)

```json
[
  "Who is the customer?",
  "What is the invoice date?",
  "What is the total billed amount?"
]
```

### 📤 Output (`output.json`)

```json
[
  "Customer: Acme Corp",
  "Invoice Date: Jan 25, 2023",
  "Total Billed: $5,234.00"
]
```

---

## 🧾 Dockerfile Reference

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir PyMuPDF

CMD ["python", "main.py"]
```

---

## 🔍 Module Overview

- `main.py` – Entry point. Iterates through `data/` folders.
- `pdf_parser.py` – Extracts raw text from PDF files.
- `qa_engine.py` – Matches questions to sentences using fuzzy logic.
- `task_handler.py` – (For future enhancements).
- `utils.py` – Helper functions for JSON operations and text processing.

---


