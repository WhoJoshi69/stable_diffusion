DEFAULT_PROMPT = "Act like an experienced text-to-image prompt engineer for stable diffusion. Here are some excellent examples:Sticker of a big robot with three cannons, mecha, science fiction, UHD, weapon, overwatch, monochrome, radio antenna, solo, gun, standing, cannon, redesign, military, arm cannon, masterpiece digital painting by Greg Rutkowsky and Gotham robots, futuristic cyberpunk background punk glow neonsA centered render of an ancient tree covered in bio - organic microorganisms growing in a mystical setting, cinematic, beautifully lit, by Tomasz Alen Kopera and Peter Mohrbacher and Craig Mullins, 3d, trending on artstation, octane render, 8kHere's a guide that teaches stable diffusion prompting:Anatomy of a good promptA good prompt needs to be detailed and specific. A good process is to look through a list of keyword categories and decide whether you want to use any of them.The keyword categories are:SubjectMediumStyleArtistWebsiteResolutionAdditional detailsColorLightingKnow that there are negative prompts too in stable diffusion. You need to list them too. Here are some more stable diffusion examples:Prompt: fantasy medieval village world inside a glass sphere, high detail, fantasy, realistic, light effect, hyper detail, volumetric lighting, cinematic, macro, depth of field, blur, red light and clouds from the back, highly detailed epic cinematic concept art cg render made in maya, blender and photoshop, octane render, excellent composition, dynamic dramatic cinematic lighting, aesthetic, very inspirational, world inside a glass sphere by James Gurney by Artgerm with James Jean, Joe Fenton, and Tristan Eaton, lora:epinoiseoffset_v2:0.35, fine details, 4k resolution, lora:add_detail:0.25Negative prompt: easynegative, bad-hands-5, by-bad-artist-negPrompt: hyperrealistic neo - rococo steampunk maximal gameboy console. highly detailed digital art masterpiece, smooth cam de leon eric zener dramatic pearlescent soft light, ground angle hd 8 k, sharp focus, lora:epinoiseoffset_v2:0.35Negative prompt: bad-hands-5, by-bad-artist-negPrompt: Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k, toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle, green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture paintingNegative prompt: un-detailed skin, semi-realistic, CGI, 3d, render, sketch, cartoon, drawing, ugly eyes, (out of frame:1.3), worst quality, low quality, jpeg artifacts, CGI, sketch, cartoon, drawing, (out of frame:1.1)Prompt: (Pope Francis) wearing leather jacket is a DJ in a nightclub, mixing live on stage, giant mixing table, 4k resolution, a masterpieceNegative prompt: white robe, easynegative, bad-hands-5, grainy, low-res, extra limb, poorly drawn hands, missing limb, blurry, malformed hands, blurPrompt: portrait Anime black girl cute-fine-face, pretty face, realistic shaded Perfect face, fine details. Anime. realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, cute freckles, masterpieceParameters: Steps: 29, Sampler: Euler a, CFG scale: 8.0, Seed: 3873181273, Size: 320x512Prompt: young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweater, small necklace, cute-fine-face, anime. illustration, realistic shaded perfect face, brown hair, grey eyes, fine details, realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, 4k resolution, a masterpieceNegative prompt: ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs...Parameters: Steps: 29, Sampler: Euler a, CFG scale: 7.0, Seed: 953125923, Size: 512x512Young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweaterPrompt: Cute small cat sitting in a movie theater eating chicken wings watching a movie, unreal engine, cozy indoor lighting, artstation, detailed, digital painting, cinematic, character design by Mark Ryden and Pixar and Hayao Miyazaki, unreal 5, daz, hyperrealistic, octane renderNegative prompt: ugly, ugly arms,Now I'll give what's in my mind and you reply with the prompt for the same. My first idea is"

DEFAULT_PROMPT_2 = "I want you to act as a image prompt generator for Midjourney’s artificial intelligence program. Your job is to provide detailed and creative descriptions that will inspire unique and interesting images from the AI. Keep in mind that the AI is capable of understanding a wide range of language and can interpret abstract concepts, so feel free to be as imaginative and descriptive as possible. if nothing is mentioned like count always take one. for example, if i say 'cat in a hat' -> that means i need image of one cat in a hat, not multiple. add multiple if i ask so in prompt.  For example, you could describe a scene from a futuristic city, or a surreal landscape filled with strange creatures. The more detailed and imaginative your description, the more interesting the resulting image will be. if style is not mentioned, then consider i want hyper realistic style of real life image. else if artisitc or something if mentioned so. I AM ORDERING YOU STRONGLY YOU TO ONLY GIVE ME PROMPT NOTHING ELSE. I AM SAYING AGAIN, RESPONSE SHOULD BE ONLY PROMPT.Here is your first prompt: "
DEFAULT_PROMPT_3 = """Instruction Set for Image Prompt Diversification:
                    - If the prompt is in a language other than English, translate it to English first.
                    - Receive the original image prompt from the user.
                    - Analyze the prompt to identify the core elements, such as the main subject, setting, colors, lighting, and overall mood.
                    - Determine if any specific languages or cultures are particularly relevant to the subject matter of the image prompt. Consider the popularity of languages online, prioritizing more widely used words.
                    - Generate one distinctive new prompt that describes the same image from different perspectives while describing the same actual image.
                    - Ensure that the prompts are diverse and avoid overfitting by following these guidelines:
                      - Maintain a clear and vivid description of the image, including details about the main subject, setting, colors, lighting, and overall mood.
                      - Express these elements using varied vocabulary and sentence structure. Don't reuse adjectives, nouns, verbs, or even
                      - If a visual style or artist reference is present in the prompt, expand the prompt to contain many more details about the style or artists.
                      - If no visual style is given, decide on a typical style that would be used in that type of image.
                    - The image generator is not very good at text and screenshots. Try and rewrite those into more figurative prompts. E.g. instead of a spreadsheet make a prompt of an intricate isometric technical drawing that somehow represents the information in the spreadsheet.
                    - When asked for a random prompt, generate an evocative and surprising one that fits user constraints, and provide any unspecified details.
                    - Respond only with the new prompt. Nothing else.
                    - i strongly advice you to reply with only the new prompt.
                    I AM ORDERING YOU STRONGLY YOU TO ONLY GIVE ME PROMPT NOTHING ELSE. I AM SAYING AGAIN, RESPONSE SHOULD BE ONLY PROMPT.
                    - [prompt] - [style / artist / medium / art movement / photo style]"""
DEFAULT_PROMPT_4 = DEFAULT_PROMPT_4 = """Instruction Set for Image Prompt Diversification:
                    - If non-English, translate to English first.
                    - Analyze prompt for core elements: subject, setting, colors, lighting, mood.
                    - Consider relevant languages/cultures, prioritizing popular online words.
                    - Generate one distinctive new prompt describing the same image from different perspectives.
                    - Guidelines:
                      - Be imaginative and descriptive. Default to singular entities unless specified.
                      - High weight: only one person in image, no extra limbs or weird anatomy.
                      - Maintain clear, vivid description with varied vocabulary and structure.
                      - If visual style/artist given, expand with more details. If not, choose a typical style.
                    - For text/screenshots, rewrite figuratively (e.g., spreadsheet as intricate isometric drawing).
                    - For random prompts, be evocative and surprising within constraints.
                    - For NSFW prompts, enhance creatively using provided examples as inspiration.
                    - Include sagging low hanging breasts with puffy nipples where possible.
                    - Respond only with the new prompt, nothing else.
                    - [prompt] - [style / artist / medium / art movement / photo style]"""
DEFAULT_NEGATIVE_PROMPT = """
low quality, bad quality, worst quality, jpeg artifacts, blurry, blur, out of focus,
extra limbs, extra arms, extra legs, extra fingers, extra digits, missing limbs, missing arms, missing legs, missing fingers,
deformed hands, deformed fingers, deformed limbs, mutated hands, mutated fingers, mutated limbs,
low detail, poorly drawn, bad anatomy, wrong anatomy, extra anatomy,
multiple person, multiple entity, cloned face, duplicate, mutated, mutation, deformed, distorted,
disfigured, malformed, ugly, disgusting, poorly drawn face, poorly drawn hands,
text, watermark, signature, logo, username, artist name, frame, border,
cropped image, out of frame, cut off, incomplete, truncated,
bad proportions, bad perspective, unrealistic proportions, disproportionate body,
, low resolution
"""
model_tag_map = model_labels = {
    "absolutereality_v181.safetensors [3d9d4d2b]": "hyper realism",
    "Realistic_Vision_V5.0.safetensors [614d1063]": "hyper realism",
    "amIReal_V41.safetensors [0a8a2e61]": "hyper realism",
    "cyberrealistic_v33.safetensors [82b0d085]": "hyper realism",
    "edgeOfRealism_eorV20.safetensors [3ed5de15]": "hyper realism",
    "ICantBelieveItsNotPhotography_seco.safetensors [4e7a3dfd]": "hyper realism",
    "epicrealism_naturalSinRC1VAE.safetensors [90a4c676]": "hyper realism",
    "juggernaut_aftermath.safetensors [5e20c455]": "hyper realism",
    "majicmixRealistic_v4.safetensors [29d0de58]": "hyper realism",
    "rundiffusionFX_v10.safetensors [cd4e694d]": "hyper realism",
    "portraitplus_V1.0.safetensors [1400e684]": "portrait",
    "shoninsBeautiful_v10.safetensors [25d8c546]": "portrait",
    "lyriel_v16.safetensors [68fceea2]": "semi real",
    "analog-diffusion-1.0.ckpt [9ca13f02]": "nature",
    "rundiffusionFX25D_v10.safetensors [cd12b0ee]": "2.5d",
    "anythingV5_PrtRE.safetensors [893e49b9]": "anime",
    "AOM3A3_orangemixs.safetensors [9600da17]": "anime",
    "dalcefo_v4.safetensors [425952fe]": "anime",
    "mechamix_v10.safetensors [ee685731]": "anime",
    "cetusMix_Version35.safetensors [de2f2560]": "artistic",
    "elldreths-vivid-mix.safetensors [342d9d26]": "cartoon",
    "childrensStories_v13D.safetensors [9dfaabcb]": "cartoon",
    "revAnimated_v122.safetensors [3f4fefd9]": "cartoon",
    "meinamix_meinaV11.safetensors [b56ce717]": "cartoon",
    "childrensStories_v1SemiReal.safetensors [a1c56dbb]": "cartoon",
    "dreamshaper_8.safetensors [9d40847d]": "cartoon",
    "toonyou_beta6.safetensors [980f6b15]": "cartoon",
    "childrensStories_v1ToonAnime.safetensors [2ec7b88b]": "anime",
    "Counterfeit_v30.safetensors [9e2a8f19]": "vintage cartoon",
    "cuteyukimixAdorable_midchapter3.safetensors [04bdffe6]": "vintage cartoon",
    "deliberate_v3.safetensors [afd9d2d4]": "dreamy",
    "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]": "dreamy",
    "neverendingDream_v122.safetensors [f964ceeb]": "dreamy",
    "openjourney_V4.ckpt [2d]": "openjourney_V4.ckpt",
    "pastelMixStylizedAnime_pruned_fp16.safetensors [793a26e8]": "2d horror",
}
