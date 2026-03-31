from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data import TABLE_REGISTRY

app = FastAPI(title="INTERRA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tables/{table_key}")
def get_table(table_key: str):
    """Return sample rows for a given table key (T1–T6)."""
    key = table_key.upper()
    if key not in TABLE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Table '{table_key}' not found")
    fn, name = TABLE_REGISTRY[key]
    return {"table_key": key, "name": name, "rows": fn()}


@app.get("/tables")
def list_tables():
    """List all available tables."""
    return {
        k: {"name": v[1], "row_count": len(v[0]())}
        for k, v in TABLE_REGISTRY.items()
    }
