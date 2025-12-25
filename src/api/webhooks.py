from fastapi import APIRouter, Request, Header, HTTPException
from src.config import Config

Router = APIRouter()

@Router.post("/webhook")
async def handle_webhook(request: Request, x_webhook_secret: str | None = Header(None)):
    if Config.WEBHOOK_SECRET:
        print("INFO: Webhook secret set, checking it")
        if x_webhook_secret != Config.WEBHOOK_SECRET:
            print("ERROR: Invalid webhook secret")
    
    try: 
        data = await request.json()
    except Exception:
        body = await request.body()
        data = body.decode('utf-8')

    print("INFO: Received webhook data:", data)

    queue = request.app.state.queue
    await queue.put(data)

    return {"status": "success"}

@Router.get("/health")
async def health_check():
    return {"status": "ok"}