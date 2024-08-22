import io

import requests
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

from fastapi.responses import StreamingResponse
from starlette.websockets import WebSocketDisconnect

import constants
from nsfw_gen import createPrompts

app = FastAPI()

# Define the templates folder
templates = Jinja2Templates(directory="templates")

# Store active WebSocket connections
websocket_connections = []

# API endpoints
GENERATE_API_ENDPOINT = "https://api.prodia.com/generate"
IMAGE_API_ENDPOINT = "https://images.prodia.xyz"
PROMPT_EXPAND_ENDPOINT = 'https://www.feedough.com/wp-admin/admin-ajax.php'


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
            print("image created successfully, now plotting to front end")
            return image_response.content
        else:
            # If not successful, wait for 0.5 seconds before retrying
            await asyncio.sleep(0.5)


@app.get("/fetch_everything/")
async def fetch_everything(prompt, tags, model):
    print(f"received prompt: {prompt}, tags: {tags}, model: {model}")
    createPrompts(1)
    with open('prompts.txt', 'r') as file:
        content = file.read()
    if not model:
        model = "absolutereality_v181.safetensors [3d9d4d2b]"
    prompt += ", 8k image, highly detailed, detailed eyes, detailed skin textures, detailed lips"

    if "woman, women, man, men, people" in prompt:
        prompt += "full body image, wide angele shot"

    if "nsfw" in prompt:
        prompt += content
    for tag in tags:
        prompt += ", image style " + tag

    prompt += ", image style of " + constants.model_tag_map[model]

    # headers = {
    #     'authority': 'www.feedough.com',
    #     'accept': '*/*',
    #     'accept-language': 'en-US,en;q=0.7',
    #     'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    #     'cookie': 'ext_name=ojplmecpdpgccookcobabopnaifgidhf; _ga=GA1.1.2086675295.1708885051; aixg_user_id=aixg_65db843e334939.18757862; tve_leads_unique=1; tl_3314_3315_43=a%3A1%3A%7Bs%3A6%3A%22log_id%22%3BN%3B%7D; tl_3314_30184_75=a%3A1%3A%7Bs%3A6%3A%22log_id%22%3BN%3B%7D; _ga_722BX5RSV3=GS1.1.1708885050.1.1.1708885065.45.0.0; aixg_user_id=aixg_65db86a98b03d1.46449765',
    #     'origin': 'https://www.feedough.com',
    #     'referer': 'https://www.feedough.com/stable-diffusion-prompt-generator/',
    #     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-gpc': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    # }
    #
    # data = {
    #     'action': 'aixg_generate',
    #     'prompt': constants.DEFAULT_PROMPT + " - " + prompt + " - " + constants.DEFAULT_PROMPT_2,
    #     '_ts': '1708885412291',
    #     'form_id': 'ai_x_generator_65db28276d07f',
    # }
    # # Make the request with cookies and payload
    # response = requests.post(PROMPT_EXPAND_ENDPOINT, headers=headers, data=data)
    #
    # # Check the response status code
    # if response.status_code == 200:
    #     # API request was successful
    #     prompt = response.json()["data"]["message"]
    #     print(f"this is expanded prompt: {prompt}")
    # else:
    #     # API request failed
    #     print('API request failed with status code:', response.status_code)

    params = {
        "new": "true",
        "steps": 100,
        "cfg": 7,
        "prompt": prompt,
        "model": model,
        "negative_prompt": constants.DEFAULT_NEGATIVE_PROMPT,
        "sampler": "DPM++ 2M Karras",
        "seed": -1,
        "aspect_ratio": "square"
    }
    print("generating image...")
    response = requests.get(GENERATE_API_ENDPOINT, params=params)

    if response.status_code == 200:
        # Extract the job ID from the response
        response_json = response.json()
        job_id = response_json.get("job")
        print("image generated, now converting it to jpg...")
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
