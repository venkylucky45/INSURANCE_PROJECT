# ===========================
# 1. Base Image
# ===========================
FROM python:3.10-slim

# ===========================
# 2. Set Work Directory
# ===========================
WORKDIR /app

# ===========================
# 3. Install System Dependencies
# ===========================
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && apt-get clean

# ===========================
# 4. Copy Requirements
# ===========================
COPY requirements.txt .

# ===========================
# 5. Install Python Packages
# ===========================
RUN pip install --no-cache-dir -r requirements.txt

# ===========================
# 6. Copy Entire Project
# ===========================
COPY . .

# ===========================
# 7. Expose FastAPI Port
# ===========================
EXPOSE 8000

# ===========================
# 8. Run FastAPI with Uvicorn
# ===========================
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
