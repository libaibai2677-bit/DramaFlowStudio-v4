# 🧠 DramaFlow Studio v4 — Architecture Refactor Plan

## 🎯 Goal
Transform current SaaS prototype into a **clean, scalable, production-grade AI architecture** with strict layering and separation of concerns.

---

# ⚠️ Current Issues (Observed)

## 1. Controller Overload
- ProductController handles too many responsibilities
- AI logic + history + recommendation mixed

## 2. Missing Application Layer
- UI/API directly depend on Controller
- No orchestration boundary

## 3. Weak Domain Separation
- DTOs mixed with domain models
- Unsafe use of `__dict__`

## 4. In-memory SaaS limitations
- Usage tracking not persistent
- No tenant isolation

---

# 🏗 Target Architecture (Final Form)

```
UI (Streamlit)
   ↓
API Layer (FastAPI)
   ↓
Application Service Layer  ← NEW
   ↓
Domain Services
   ├── AI Engine Service
   ├── History Service
   ├── Recommendation Service
   └── Explanation Service
   ↓
DTO Mapping Layer
   ↓
Infrastructure Layer (DB / Cache)
```

---

# 🧩 Key Refactor Decisions

## ✔ 1. Introduce ApplicationService
Central orchestration layer for:
- UI/API requests
- workflow coordination
- dependency isolation

---

## ✔ 2. Split ProductController
Replace with:
- AIEngineService
- HistoryService
- RecommendationService
- ExplanationService

---

## ✔ 3. Introduce DTO Mapper
- Remove `__dict__` exposure
- Use explicit mapping functions

---

## ✔ 4. Persistence Upgrade Plan
- Replace in-memory usage tracking
- Introduce Redis/Postgres layer

---

# 🚀 Migration Strategy

## Phase 1 (Safe Refactor)
- Add ApplicationService
- No behavior change

## Phase 2 (Service Split)
- Break Controller into services

## Phase 3 (Data Hardening)
- DTO strict mapping
- persistence layer upgrade

---

# 🧠 Design Principles

- Single Responsibility Principle (SRP)
- Dependency Inversion (DIP)
- Clean Architecture boundaries
- API-first design

---

# 🏁 Outcome

After refactor, system becomes:

> A modular AI SaaS architecture with strict separation between UI, orchestration, domain, and infrastructure layers.