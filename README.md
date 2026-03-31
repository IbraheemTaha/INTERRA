# INTERRA

Proof-of-concept implementation for research experiments. Built with FastAPI (backend) and Streamlit (frontend), fully dockerized for reproducible runs.

## Requirements

- [Docker](https://docs.docker.com/get-docker/) + [Docker Compose](https://docs.docker.com/compose/)
- `make`

## Setup

```bash
cp .env.example .env
# edit .env as needed
```

## Usage

| Command | Description |
|---|---|
| `make build` | Build all Docker images |
| `make start` | Alias for `up` |
| `make up` | Start all services (detached) |
| `make up-build` | Rebuild images and start |
| `make down` | Stop all services |
| `make restart` | Restart all services |
| `make logs` | Tail logs for all services |
| `make logs-backend` | Tail backend logs only |
| `make logs-frontend` | Tail frontend logs only |
| `make shell-backend` | Shell into the backend container |
| `make shell-frontend` | Shell into the frontend container |
| `make clean` | Stop and remove containers, networks, and volumes |

## Services

| Service | URL |
|---|---|
| Streamlit UI | http://localhost:8501 |
| FastAPI backend | http://localhost:8000 |
| API docs (Swagger) | http://localhost:8000/docs |

## Project Structure

```
INTERRA/
├── docker-compose.yml
├── Makefile
├── .env.example
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
└── frontend/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

Both services mount their source directory as a volume, so code changes apply immediately without rebuilding.
