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


model_map = {"absolutereality_v181 (hyper realism)": "absolutereality_v181.safetensors [3d9d4d2b]",
             "Realistic_Vision_V5.0.safetensors (hyper realism)": "Realistic_Vision_V5.0.safetensors [614d1063]",
             "amIReal_V41.safetensors (hyper realism)": "amIReal_V41.safetensors [0a8a2e61]",
             "cyberrealistic_v33.safetensors (hyper realism)": "cyberrealistic_v33.safetensors [82b0d085]",
             "edgeOfRealism_eorV20.safetensors (hyper realism)": "edgeOfRealism_eorV20.safetensors [3ed5de15]",
             "ICantBelieveItsNotPhotography_seco.safetensors (hyper realism)": "ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]",
             "epicrealism_naturalSinRC1VAE.safetensors (hyper realism)": "epicrealism_naturalSinRC1VAE.safetensors [90a4c676]",
             "juggernaut_aftermath.safetensors (hyper realism)": "juggernaut_aftermath.safetensors [5e20c455]",
             "majicmixRealistic_v4.safetensors (hyper realism)": "majicmixRealistic_v4.safetensors [29d0de58]",
             "rundiffusionFX_v10.safetensors (hyper realism)": "rundiffusionFX_v10.safetensors [cd4e694d]",
             "portraitplus_V1.0.safetensors (portrait)": "portraitplus_V1.0.safetensors [1400e684]",
             "shoninsBeautiful_v10.safetensors (portrait)": "shoninsBeautiful_v10.safetensors [25d8c546]",
             "lyriel_v16.safetensors (semi real)": "lyriel_v16.safetensors [68fceea2]",
             "analog-diffusion-1.0.ckpt (nature)": "analog-diffusion-1.0.ckpt [9ca13f02]",
             "rundiffusionFX25D_v10.safetensors (2.5d)": "rundiffusionFX25D_v10.safetensors [cd12b0ee]",
             "anythingV5_PrtRE.safetensors (anime)": "anythingV5_PrtRE.safetensors [893e49b9]",
             "AOM3A3_orangemixs.safetensors (anime)": "AOM3A3_orangemixs.safetensors [9600da17]",
             "dalcefo_v4.safetensors (anime)": "dalcefo_v4.safetensors [425952fe]",
             "mechamix_v10.safetensors (anime)": "mechamix_v10.safetensors [ee685731]",
             "cetusMix_Version35.safetensors (artistic)": "cetusMix_Version35.safetensors [de2f2560]",
             "elldreths-vivid-mix.safetensors (cartoon)": "elldreths-vivid-mix.safetensors [342d9d26]",
             "childrensStories_v13D.safetensors (cartoon)": "childrensStories_v13D.safetensors [9dfaabcb]",
             "revAnimated_v122.safetensors (cartoon)": "revAnimated_v122.safetensors [3f4fefd9]",
             "meinamix_meinaV11.safetensors (cartoon)": "meinamix_meinaV11.safetensors [b56ce717]",
             "childrensStories_v1SemiReal.safetensors (cartoon)": "childrensStories_v1SemiReal.safetensors [a1c56dbb]",
             "dreamshaper_8.safetensors (cartoon)": "dreamshaper_8.safetensors [9d40847d]",
             "toonyou_beta6.safetensors (cartoon)": "toonyou_beta6.safetensors [980f6b15]",
             "childrensStories_v1ToonAnime.safetensors (anime)": "childrensStories_v1ToonAnime.safetensors [2ec7b88b]",
             "Counterfeit_v30.safetensors (vintage cartoon)": "Counterfeit_v30.safetensors [9e2a8f19]",
             "cuteyukimixAdorable_midchapter3.safetensors (vintage cartoon)": "cuteyukimixAdorable_midchapter3.safetensors [04bdffe6]",
             "deliberate_v3.safetensors (dreamy)": "deliberate_v3.safetensors [afd9d2d4]",
             "dreamlike-diffusion-1.0.safetensors (dreamy)": "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]",
             "neverendingDream_v122.safetensors [dreamy]": "neverendingDream_v122.safetensors [f964ceeb]",
             "openjourney_V4.ckpt [2d]": "openjourney_V4.ckpt [ca2f377f]",
             "pastelMixStylizedAnime_pruned_fp16.safetensors (2d horror) ": "pastelMixStylizedAnime_pruned_fp16.safetensors [793a26e8]",
             }


@app.get("/fetch_everything/")
async def fetch_everything(prompt, tags, model):
    if not model:
        model = "absolutereality_v181.safetensors [3d9d4d2b]"
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
        "model": model,
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
