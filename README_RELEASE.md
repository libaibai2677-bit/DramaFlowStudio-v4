# 🎬 DramaFlow Studio v4 — Release Edition

## 🟣 Production Status
This is the **release-packaged version** of DramaFlow Studio v4.

---

## 🚀 What’s Included

### 🧠 AI System
- Unified Engine (Intent + Query Enhancement)
- Result Normalizer (contract enforcement)
- DTO architecture (strict typing layer)

### 🧱 System Design
- ProductController (single entry point)
- Service Layer (history / recommend / explain)
- Error-safe fallback system

### 🎨 Product UI
- Streamlit final UI (card-based rendering)
- Sidebar history & recommendations
- Explainable AI output panel

### 🐳 Deployment
- Docker support
- CI pipeline (GitHub Actions)
- One-command run support

---

## 🏗 Architecture (Final)
```
UI (Streamlit)
   ↓
ProductController
   ↓
UnifiedEngine
   ↓
Normalizer
   ↓
DTO Layer
   ↓
Services
```

---

## ⚡ Run Locally
```bash
streamlit run app/main_final.py
```

---

## 🐳 Run with Docker
```bash
docker build -t dramaflow .
docker run -p 8501:8501 dramaflow
```

---

## 🧪 CI
GitHub Actions included:
- Install dependencies
- Import validation
- System sanity check

---

## 🧠 Positioning
This project is designed as:

> A **portfolio-grade AI system architecture showcase**

Not a toy project — but a structured AI product system.

---

## 🏁 Result
✔ Fully wired AI pipeline
✔ Production-ready structure
✔ Deployable container system
✔ Portfolio-level documentation