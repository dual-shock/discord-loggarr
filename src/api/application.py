from fastapi import FastAPI
from .webhooks import Router

def start() -> FastAPI:
    print("INFO: Starting API server")
    app = FastAPI(title="Discord loggarr", summary="logging events from *arr webhooks")
    app.include_router(Router)
    print("INFO: API server started")
    return app

