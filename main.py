from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from broadcaster import Broadcast
import asyncio
import json

# 1. Define the Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs ON STARTUP
    await broadcast.connect()
    yield  # The app runs while it "yields" here
    # This code runs ON SHUTDOWN
    await broadcast.disconnect()

# 2. Pass the lifespan to the FastAPI app
app = FastAPI(lifespan=lifespan)

broadcast = Broadcast("memory://")
templates = Jinja2Templates(directory="templates")

poll_data = {"Python": 0, "JavaScript": 0, "C++": 0}

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "votes": poll_data})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async with broadcast.subscribe(channel="poll_channel") as subscriber:
        
        # TASK 1: Listen for when the server shouts a new vote count
        async def send_updates():
            async for event in subscriber:
                await websocket.send_text(event.message)

        # TASK 2: Listen for when THIS specific user clicks a button
        async def receive_votes():
            try:
                while True:
                    data = await websocket.receive_text()
                    if data in poll_data:
                        poll_data[data] += 1
                        # Shout the update to the Broadcaster
                        await broadcast.publish(
                            channel="poll_channel", 
                            message=json.dumps({"language": data, "votes": poll_data[data]})
                        )
            except WebSocketDisconnect:
                pass

        # This "gathers" both tasks and runs them concurrently
        await asyncio.gather(send_updates(), receive_votes())