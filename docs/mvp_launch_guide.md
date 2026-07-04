# 🚀 MVP Launch Guide (Production-Ready Release)

This guide defines the **minimum complete launch version** of DramaFlow AI Runtime as a deployable MVP product.

---

# 🟢 1. MVP Definition

The MVP includes:

- FastAPI AI Runtime Service
- Agent Orchestrator Core
- Tool System (Web Search + internal tools)
- Memory Layer (basic)
- Observability (trace + logs)
- Docker deployment stack

> ❌ Excludes: billing, marketplace, advanced UI, enterprise scaling

---

# 🏗️ 2. System Startup Architecture

```text
User → FastAPI (/run)
     → AgentOrchestrator
     → Tools + Memory + Reflection
     → Response + Trace Logs
```

---

# ⚡ 3. One-Command Deployment

## Step 1: Build & Run

```bash
docker-compose -f deploy/docker-compose.yml up -d --build
```

---

## Step 2: Verify Services

### API Health Check
```bash
curl http://localhost:8000/health
```

Expected:
```json
{"status": "ok"}
```

---

## Step 3: Run AI Request

```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Explain how AI agents work",
    "mode": "auto"
  }'
```

---

# 🧠 4. Core Runtime Flow

Each request executes:

1. Receive goal
2. Orchestrator planning
3. Tool routing (if needed)
4. Execution
5. Reflection
6. Response formatting
7. Trace logging

---

# 📊 5. Observability (Built-in)

Each request includes:

- trace_id
- execution spans
- tool usage logs
- runtime duration

Logs available in container:

```bash
docker logs drama-flow-api
```

---

# 🧩 6. Environment Configuration

Create `.env` (optional):

```env
ENV=prod
LOG_LEVEL=INFO
WEB_SEARCH_PROVIDER=serpapi
```

---

# 🗄 7. Infrastructure Services

Started via Docker Compose:

- API (FastAPI) → port 8000
- Redis → port 6379
- PostgreSQL → port 5432

---

# 🔐 8. MVP Security Notes

Current MVP behavior:

- No authentication (open API)
- No rate limiting
- No tenant isolation

> ⚠️ Intended for internal / controlled deployment only

---

# 🚀 9. MVP Success Criteria

The system is considered successfully launched if:

- API responds at `/health`
- `/run` executes AI workflow
- Logs show trace execution
- Docker stack runs without errors

---

# 🧠 10. What You Now Have

You now have a working system that includes:

- AI reasoning engine
- Tool execution layer
- Memory integration
- Observability system
- Deployable runtime

---

# 🌍 Final Statement

This MVP is not a prototype anymore.

It is a:

> 🟣 **Deployable AI Agent Runtime Product (Minimum Commercial Launch Version)**
