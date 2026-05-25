# Layer 1 — Base image
FROM python:3.11-slim

# Layer 2 — Set working directory inside container
WORKDIR /app

# Layer 3 — Copy ONLY requirements first (cache optimization)
COPY requirements.txt .

# Layer 4 — Install dependencies (cached unless requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# Layer 5 — Copy application code (changes frequently)
COPY . .

# Expose port for documentation purposes
EXPOSE 8000

# Layer 6 — Command to run when container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]