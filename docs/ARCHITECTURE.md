# DramaFlow Studio v4 — Architecture Freeze (Final)

> This document defines the **final system architecture**. Any future changes must respect this structure.

---

# 🧠 1. System Overview

DramaFlow Studio v4 is a **modular AI image search product system** composed of three stable layers:

```
UI Layer
   ↓
ProductController (Single Entry Point)
   ↓
UnifiedEngine (Core AI Pipeline)
   ↓
Service Layer (Business Capabilities)
```

---

# 🧩 2. Layer Responsibilities

## 🟢 UI Layer
- Render results
- Display history / recommendations / explanations
- No business logic

---

## 🟡 ProductController (ORCHESTRATION ONLY)

**Responsibilities:**
- Single entry point for all requests
- Call UnifiedEngine
- Call Services
- Assemble final response

**Rules:**
- ❌ No AI logic
- ❌ No ranking
- ❌ No caching logic

---

## 🔵 UnifiedEngine (AI CORE ONLY)

**Responsibilities:**
- Query enhancement (PromptEnhancer)
- Image search execution
- Result ranking
- Cache handling (low-level)

**Rules:**
- ❌ No UI logic
- ❌ No history tracking
- ❌ No recommendations

---

## 🟣 Service Layer (Business Intelligence)

### 1. HistoryService
- Stores user query history
- Provides session context

### 2. RecommendationService
- Generates next-step suggestions
- Uses history as input

### 3. ExplainabilityService
- Generates human-readable explanations
- Adds trust and transparency layer

---

# 🔁 3. Data Flow (Canonical)

```
User Query
   ↓
ProductController
   ↓
UnifiedEngine
   ↓
Results
   ↓
ExplainabilityService
   ↓
ProductController
   ↓
UI Response
   ↓
HistoryService + RecommendationService
```

---

# 📦 4. Core Design Principles

## 1. Single Responsibility
Each module has ONE clear job.

## 2. Single Entry Point
All requests go through ProductController.

## 3. AI Core Isolation
UnifiedEngine contains ALL AI logic.

## 4. Service Decoupling
Services do NOT depend on AI engine internals.

## 5. No Cross-Layer Leakage
No layer is allowed to bypass its boundary.

---

# 🚫 5. Deprecated / Forbidden Patterns

- ❌ SearchFacade usage
- ❌ AI logic inside ProductController
- ❌ Service calling other services recursively
- ❌ UI accessing UnifiedEngine directly

---

# 📈 6. Evolution Status

| Layer | Status |
|------|--------|
| UI | Stable |
| ProductController | Stable |
| UnifiedEngine | Stable |
| Service Layer | Stable |
| Architecture | **FROZEN** |

---

# 🧠 7. Final Statement

This system is now in **architecture freeze mode**.

Future changes must:

> ❗ Extend existing layers only
> ❗ NOT create parallel architectures

---

# 🟢 Result

DramaFlow Studio v4 is a production-grade modular AI system with strict architectural boundaries.