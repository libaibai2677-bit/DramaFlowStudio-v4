#!/usr/bin/env bash

# 🌍 DramaFlow AI - One Click Startup Script
# This script boots the full stack: API + UI + DB + Worker

set -e

echo "🚀 Starting DramaFlow AI (Production Stack)..."

# -----------------------------
# Check Docker
# -----------------------------
if ! command -v docker &> /dev/null
then
    echo "❌ Docker not found. Please install Docker Desktop first."
    exit 1
fi

# -----------------------------
# Start Services
# -----------------------------
cd deploy

docker compose up -d --build

# -----------------------------
# Wait for services
# -----------------------------

sleep 5

echo "🌐 UI: http://localhost:3000"
echo "⚙ API: http://localhost:8000"
echo "🧠 System: Running"

echo "✅ DramaFlow AI started successfully"
