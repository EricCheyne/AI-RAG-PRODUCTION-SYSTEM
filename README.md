# AI Document Intelligence Platform (RAG)

A production-style RAG system built with FastAPI, Celery, and pgvector.

## Project Structure

```text
.
├── apps/
│   ├── api/          # FastAPI application
│   └── worker/       # Celery worker for background processing
├── packages/
│   └── core/         # Shared modules (models, schemas, utils)
├── docker-compose.yml # Infrastructure (Postgres + Redis)
└── .env.example       # Environment variables template
```

## Stack

- **FastAPI**: Main API for document management and retrieval.
- **Celery**: Distributed task queue for document embedding and processing.
- **Postgres (pgvector)**: Vector database for storing document embeddings.
- **Redis**: Message broker for Celery.
- **OpenAI**: Default LLM and Embedding provider.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.10+

### Local Setup

1. **Clone the repository**
2. **Copy environment variables**
   ```bash
   cp .env.example .env
   ```
3. **Start infrastructure**
   ```bash
   docker-compose up -d
   ```
4. **Install dependencies (Example for API)**
   ```bash
   cd apps/api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Running Locally

- **API**: `cd apps/api && uvicorn main:app --reload`
- **Worker**: `cd apps/worker && celery -A main.celery_app worker --loglevel=info`

## License
MIT
