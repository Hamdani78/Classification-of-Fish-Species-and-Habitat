# Gunakan image Python resmi
FROM python:3.11-slim

# Set direktori kerja
WORKDIR /app

# Copy semua file ke container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Jalankan aplikasi
CMD ["python", "app.py"]
