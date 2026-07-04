# DramaFlow Studio v4 — Deployment Phase
# Dockerized production build for Streamlit app

FROM python:3.11-slim

WORKDIR /app

# System dependencies (minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Streamlit config
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Expose port
EXPOSE 8501

# Run app
CMD ["streamlit", "run", "app/main_final.py", "--server.port=8501", "--server.address=0.0.0.0"]