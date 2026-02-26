"""Application lifespan management for FastAPI."""

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown."""
    try:
        yield
    finally:
        print("Shutting down application...")
