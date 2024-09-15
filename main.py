import base64
import io
import aiohttp
import asyncio

import requests
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocketDisconnect
from starlette.responses import JSONResponse

import constants
from nsfw_gen import createPrompts

app = FastAPI()

# Define the templates folder
templates = Jinja2Templates(directory="templates")

# Store active WebSocket connections
websocket_connections = []

# API endpoints
GENERATE_API_ENDPOINT = "https://api.prodia.com/v1/sd/generate"
IMAGE_API_ENDPOINT = "https://images.prodia.xyz"


async def fetch_image(image_url: str) -> bytes:
    while True:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(image_url) as response:
                    if response.status == 200:
                        print("Image fetched successfully")
                        return await response.read()
                    else:
                        await asyncio.sleep(0.5)
            except Exception as e:
                print(f"An error occurred: {e}")
                await asyncio.sleep(0.5)


async def fetch_all_images(urls: list) -> list:
    tasks = [fetch_image(url) for url in urls]
    image_contents = await asyncio.gather(*tasks)
    return image_contents


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.append(websocket)

    try:
        while True:
            await asyncio.sleep(1)  # Keep the connection alive
    except WebSocketDisconnect:
        websocket_connections.remove(websocket)


# Function to send messages to all connected clients
async def send_message(message: str):
    for connection in websocket_connections:
        await connection.send_text(message)


def print_to_frontend(message: str):
    print(message)  # Print to console as well
    asyncio.create_task(send_message(message))


@app.get("/fetch_everything/")
async def fetch_everything(prompt: str, tags: str, model: str, aspect_ratio: str):
    print(f"Received prompt: {prompt}, tags: {tags}, model: {model}, aspect_ratio: {aspect_ratio}")
    for tag in tags.split(','):
        prompt += ", image style " + tag
    prompt1 = createPrompts(prompt)
    prompt2 = createPrompts(prompt)
    if not model:
        model = "absolutereality_v181.safetensors [3d9d4d2b]"
    prompt1 += ", 8k image, highly detailed"
    prompt2 += ", 8k image, highly detailed"

    print(f"PROMPT 1: {prompt1}")
    print(f"PROMPT 2: {prompt2}")

    # Set width and height based on aspect ratio
    if aspect_ratio == "portrait":
        width, height = 768, 1024
    elif aspect_ratio == "landscape":
        width, height = 1024, 768
    else:  # square
        width, height = 1024, 1024

    params1 = {
        "model": model,
        "prompt": prompt1,
        "negative_prompt": constants.DEFAULT_NEGATIVE_PROMPT,
        "steps": 30,
        "cfg_scale": 10,
        "seed": -1,
        "sampler": "DPM++ 2M Karras",
        "width": width,
        "height": height
    }
    params2 = {
        "model": model,
        "prompt": prompt2,
        "negative_prompt": constants.DEFAULT_NEGATIVE_PROMPT,
        "steps": 30,
        "cfg_scale": 10,
        "seed": -1,
        "sampler": "DPM++ 2M Karras",
        "width": width,
        "height": height
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-Prodia-Key": "438d9f98-6b89-45e2-b3c9-8c8d93f8bdf0"
    }
    print("Generating image...")
    image_urls = []
    responses = []
    async with aiohttp.ClientSession() as session:
        responses = [
            await session.post(GENERATE_API_ENDPOINT, json=params1, headers=headers) for _ in range(2)
        ]
        responses += [
            await session.post(GENERATE_API_ENDPOINT, json=params2, headers=headers) for _ in range(2)
        ]
        for response in responses:
            if response.status == 200:
                response_json = await response.json()
                job_id = response_json.get("job")
                print("Image generated, now fetching...")
                image_urls.append(f"{IMAGE_API_ENDPOINT}/{job_id}.png?download=1")
            else:
                return {"error": "Failed to generate the image"}

    base64_images = []
    image_contents = await fetch_all_images(image_urls)
    for image_content in image_contents:
        base64_images.append(base64.b64encode(image_content).decode('utf-8'))

    return JSONResponse(content=base64_images)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
