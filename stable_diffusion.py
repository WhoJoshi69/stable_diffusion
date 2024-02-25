import io

import requests
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

from fastapi.responses import StreamingResponse
from starlette.websockets import WebSocketDisconnect

app = FastAPI()

# Define the templates folder
templates = Jinja2Templates(directory="templates")

# Store active WebSocket connections
websocket_connections = []

# API endpoints
GENERATE_API_ENDPOINT = "https://api.prodia.com/generate"
IMAGE_API_ENDPOINT = "https://images.prodia.xyz"
PROMPT_EXPAND_ENDPOINT = 'https://playground.com/api/expand-prompt'


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
async def send_message(message):
    for connection in websocket_connections:
        await connection.send_text(message)


# Modify your print statements to send messages to the frontend
def print_to_frontend(message):
    print(message)  # Print to console as well
    asyncio.run(send_message(message))


async def fetch_image(image_url):
    while True:
        # Fetch the image using the provided URL
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            # If successful, return the image content
            return image_response.content
        else:
            # If not successful, wait for 0.5 seconds before retrying
            await asyncio.sleep(0.5)


@app.get("/fetch_everything/")
async def fetch_everything(prompt, tags):
    prompt += "8k image"
    for tag in tags:
        prompt += ", " + tag

    # Define your headers
    headers = {
        'Content-Type': 'application/json',
        'Cookie': '__Host-next-auth.csrf-token=090a5ee7b3f9c3ee6ffa48166cf2a1fdd1d628712832811b9cc13df7ead7c820%7C45faa8af4e7e7b052c676809c0cad63bc2e3d4a05039e06d184aa89bbe78d3e2; __Secure-next-auth.callback-url=https%3A%2F%2Fplaygroundai.com; __Secure-next-auth.session-token=782b67b3-807f-4191-9543-7939d161b612'
    }

    # Define the payload
    data = {
        'prompt': prompt
    }

    # Make the request with cookies and payload
    response = requests.post(PROMPT_EXPAND_ENDPOINT, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        # API request was successful
        prompt = response.json()["expandedPrompt"]
    else:
        # API request failed
        print('API request failed with status code:', response.status_code)

    params = {
        "new": "true",
        "steps": 100,
        "cfg": 7,
        "prompt": prompt,
        "model": "absolutereality_v181.safetensors [3d9d4d2b]",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, out of focus, bad anatomy, extra limbs, poorly drawn face, poorly drawn hands, missing fingers",
        "sampler": "DPM++ 2M Karras",
        "seed": -1,
        "aspect_ratio": "square"
    }

    response = requests.get(GENERATE_API_ENDPOINT, params=params)

    if response.status_code == 200:
        # Extract the job ID from the response
        response_json = response.json()
        job_id = response_json.get("job")

        # Use the job ID to construct the URL for the image API
        image_url = f"{IMAGE_API_ENDPOINT}/{job_id}.png?download=1"

        # Fetch the image using the constructed URL
        image_content = await fetch_image(image_url)

        # Return StreamingResponse with image content and appropriate content type
        x = StreamingResponse(io.BytesIO(image_content), media_type="image/png")
        return x
    else:
        # Return an error message if the request to generate the image fails
        return {"error": "Failed to generate the image"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
