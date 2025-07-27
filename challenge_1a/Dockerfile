FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# Copy source code
COPY process_pdfs.py .
COPY pdf_parser.py .

# Install dependencies
RUN pip install --no-cache-dir pdfminer.six

# Run script on container start
CMD ["python", "process_pdfs.py"]
