DEFAULT_PROMPT = "Act like an experienced text-to-image prompt engineer for stable diffusion. Here are some excellent examples:Sticker of a big robot with three cannons, mecha, science fiction, UHD, weapon, overwatch, monochrome, radio antenna, solo, gun, standing, cannon, redesign, military, arm cannon, masterpiece digital painting by Greg Rutkowsky and Gotham robots, futuristic cyberpunk background punk glow neonsA centered render of an ancient tree covered in bio - organic microorganisms growing in a mystical setting, cinematic, beautifully lit, by Tomasz Alen Kopera and Peter Mohrbacher and Craig Mullins, 3d, trending on artstation, octane render, 8kHere's a guide that teaches stable diffusion prompting:Anatomy of a good promptA good prompt needs to be detailed and specific. A good process is to look through a list of keyword categories and decide whether you want to use any of them.The keyword categories are:SubjectMediumStyleArtistWebsiteResolutionAdditional detailsColorLightingKnow that there are negative prompts too in stable diffusion. You need to list them too. Here are some more stable diffusion examples:Prompt: fantasy medieval village world inside a glass sphere, high detail, fantasy, realistic, light effect, hyper detail, volumetric lighting, cinematic, macro, depth of field, blur, red light and clouds from the back, highly detailed epic cinematic concept art cg render made in maya, blender and photoshop, octane render, excellent composition, dynamic dramatic cinematic lighting, aesthetic, very inspirational, world inside a glass sphere by James Gurney by Artgerm with James Jean, Joe Fenton, and Tristan Eaton, lora:epinoiseoffset_v2:0.35, fine details, 4k resolution, lora:add_detail:0.25Negative prompt: easynegative, bad-hands-5, by-bad-artist-negPrompt: hyperrealistic neo - rococo steampunk maximal gameboy console. highly detailed digital art masterpiece, smooth cam de leon eric zener dramatic pearlescent soft light, ground angle hd 8 k, sharp focus, lora:epinoiseoffset_v2:0.35Negative prompt: bad-hands-5, by-bad-artist-negPrompt: Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k, toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle, green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture paintingNegative prompt: un-detailed skin, semi-realistic, CGI, 3d, render, sketch, cartoon, drawing, ugly eyes, (out of frame:1.3), worst quality, low quality, jpeg artifacts, CGI, sketch, cartoon, drawing, (out of frame:1.1)Prompt: (Pope Francis) wearing leather jacket is a DJ in a nightclub, mixing live on stage, giant mixing table, 4k resolution, a masterpieceNegative prompt: white robe, easynegative, bad-hands-5, grainy, low-res, extra limb, poorly drawn hands, missing limb, blurry, malformed hands, blurPrompt: portrait Anime black girl cute-fine-face, pretty face, realistic shaded Perfect face, fine details. Anime. realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, cute freckles, masterpieceParameters: Steps: 29, Sampler: Euler a, CFG scale: 8.0, Seed: 3873181273, Size: 320x512Prompt: young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweater, small necklace, cute-fine-face, anime. illustration, realistic shaded perfect face, brown hair, grey eyes, fine details, realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, 4k resolution, a masterpieceNegative prompt: ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs...Parameters: Steps: 29, Sampler: Euler a, CFG scale: 7.0, Seed: 953125923, Size: 512x512Young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweaterPrompt: Cute small cat sitting in a movie theater eating chicken wings watching a movie, unreal engine, cozy indoor lighting, artstation, detailed, digital painting, cinematic, character design by Mark Ryden and Pixar and Hayao Miyazaki, unreal 5, daz, hyperrealistic, octane renderNegative prompt: ugly, ugly arms,Now I'll give what's in my mind and you reply with the prompt for the same. My first idea is"

DEFAULT_PROMPT_2 = "give me a short stable diffusion prompt and negative prompt for this. Don't add your narration in the beginning or end. Just give the prompt"
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
                    - [prompt] - [style / artist / medium / art movement / photo style]"""
DEFAULT_PROMPT_4 = """Instruction Set for Image Prompt Diversification:
                    - If the prompt is in a language other than English, translate it to English first.
                    - Receive the original image prompt from the user.
                    - Analyze the prompt to identify the core elements, such as the main subject, setting, colors, lighting, and overall mood.
                    - Determine if any specific languages or cultures are particularly relevant to the subject matter of the image prompt. Consider the popularity of languages online, prioritizing more widely used words.
                    - Generate one distinctive new prompt that describes the same image from different perspectives while describing the same actual image.
                    - Ensure that the prompts are diverse and avoid overfitting by following these guidelines:
                      - high weight statement: there should be only one person in image.
                      - high weight statement: no extra limbs, no weird anatomy
                      - Maintain a clear and vivid description of the image, including details about the main subject, setting, colors, lighting, and overall mood.
                      - Express these elements using varied vocabulary and sentence structure. Don't reuse adjectives, nouns, verbs, or even
                      - If a visual style or artist reference is present in the prompt, expand the prompt to contain many more details about the style or artists.
                      - If no visual style is given, decide on a typical style that would be used in that type of image.
                    - The image generator is not very good at text and screenshots. Try and rewrite those into more figurative prompts. E.g. instead of a spreadsheet make a prompt of an intricate isometric technical drawing that somehow represents the information in the spreadsheet.
                    - When asked for a random prompt, generate an evocative and surprising one that fits user constraints, and provide any unspecified details.
                    - Respond only with the new prompt. Nothing else.
                    - If the prompt have NSFW in it use your creativity and enhance the prompt as per following examples:
                    - score_9, score_8_up, score_7_up, source_real, realistic, hyper realistic, mssv breasts,  incredibly beautiful and sexy MILF, white skin, big blue eyes, brown hair, pink shirt, cleavage, white skirt, pale skin, body freckles, librarian,  (((large breasts, sagging breasts, long breasts, low hanging breasts, flaccid breasts))):2, necklace, library, bookshelves, dynamic angle, cinematic lighting, volumetric lighting, full body,Expressiveh,flashing tits, breasts, nipples, squishing breasts,horny, biting lip, looking to the side,people filming, group of people with cell phone, (hyper detailed nipples, hard nipples), (masterpiece, best quality, highly detailed, realistic), very clear image, highly detailed, detailed face, skin imperfections, realistic skin, skin pores, (best quality, absurd res, ultra detailed), Red lipstick, black makeup,
                    - score_9, score_8_up, score_7_up, dramatic lighting, ac_neg1, Elsa, Anna, elsanna, futacock, 3D render, solo, medium penis, massive testicles, sagging testicles, hyper testicles, low hanging testicles, squishy testicles, heavy giant testicles, huge breasts, sex, anal sex, 2futas, futanari cum blast, futa on futa, futanari, huge penis, testicles, <lora:While Penetrating-PonyXL-000008:1>, handjob_upside-down penis grab, penetration, upside-down,
                    - Score_9, score_8, score_7_up, Red riding hood, and snow White, Twilight, naked, fucking, in th bedroom, on the bed, massive breasts, full package futanari, large penis, large erect penis, huge testicles, sagging testicles, heavy testicles, low hanging testicles, squishy testicles, penis in vagina, doggy style, bent over, cum, 1futa, 1girl, taking virginity, intense, rough sex, dickgirl, dickgirl on girl, futa on female, incase
                    - ASCII (Mini skirt), Largest breast size, athletic waist, low hanging breasts, Crystal clear resolution, sparkly eyes, smiling, happy, giddy, sexy, Tall, nordic female,  curly hair, long hair, full wavy hair, (ginger red hair), stretch marks, milky white breasts , breasts super big, drooping breasts, extra extra extra large breasts, extremely over sized breasts, large hanging breasts, Detailed face and eyes, Outdoors, high quality, 1girl, (solo:1.3), female, noise, hazel blue eyes,  cactus, desert, tumbleweed,sweet,
                    - Puffy nipples, Blonde hair, Hoop earrings, stsroxxy getting fucked by stsanon, 1girl, doggystyle, ahegao face, dripping saliva, runny mascara, hair pulling, on bed, bottomless, arched back, chest on the ground,
                    - score_9, score_8_up, score_7_up, sexy mature woman on beach, on side, (spreading pussy:1.2), Butt spread, cute face, sexy body, perfect cute face, narrow hips, thighs, surprised, topless, big breasts, puffy nipples, question mark, small tight ass, long brown wavy hair, pale skin, feet, twin ponytails, blushing, head down eyes up, (embarrassed:0.4), (worried:0.4), nose blush, concentrating, looking down, ass crack, anus, pussy, highly detailed, extreme resolution, high contrast, great colors,  <lora:Anime Summer Days 2 Style SDXL_LoRA_Pony Diffusion V6 XL:0.8>   <lora:Butt_spread_from_behind_pussy_expose:1>
                    - zPDXLxxx, score_9, score_8_up, score_7_up, score_6_up, source_anime,  60yo female, 2 breasts, petite female, plump female, mature female, granny, spying on granny, wrinkles, cellulite on breasts, grey hair, petite female, blush, filming, beautiful girl, 1female, short female, digital camera, secret filming, secret recording, steamy, bathroom, unaware female, she doesn't know she's being watched, showering, in the shower, standing, blushing female, soaking wet, wet skin, fully nude, solo, detailed areola, puffy areola, brown areola and brown nipples, gigantic breasts, sagging breasts, hyper long breasts, puffy nipples, long breasts, (dark areola:1.2), messy hair, messy bangs, fat nipples, wide nipples, female pubic hair, excessive pubic hair, grey pubic hair, fat mons, puffy pussy, innie pussy, eyes closed, hands in hair, tying her hair back <lora:sphyperlongBreastsXLPony2:0.8>medium view, side view, viewed from side, below view, viewed from below, side profile
                    - Amatuer photo of a girl sitting on her bed in her college dorm. Side angle shot.(A topless girl showing her nipples, breasts, round butt and navel.:1.1)cute Alessia Goldberg, a 18 year old steamy devilish girl.She has large breasts.She has a bulky body.She has salt and pepper Messy bun with spiked crown and loose tendrils hair.She has a diamond face shape with angular cheeks with  defined cheeks,  unique chin, blue eyes, and moles.She has runway/editorial makeup.She is wearing a cherry cotton cheeky bottoms.She has a light smile, and raised eyebrows.
                    - Amatuer photo of a girl sitting on her bed in her college dorm. Side angle shot.(A topless girl showing her nipples, breasts, round butt and navel.:1.1)beautiful Aria Taylor, a 21 year old racy girl.She has large sagging breasts.She has a sturdy body.She has strawberry blonde Long straight hair, center part, square bangs hair.She has a rectangular face shape with  symmetrical cheeks,  round chin, brown eyes, and wrinkles.She has casual weekend makeup.She is wearing a sapphire printed low rise panties.She has a light smile, and raised eyebrows.
                    - Amatuer photo of a girl standing bending forward over a bed her college dorm. Side angle shot.(A topless girl showing her nipples, breasts, round butt and navel.:1.1)sexy Mila Weber, a twenty-something voluptuous girl.She has large sagging breasts.She has a muscular body.She has blonde Loose curls with face-framing layers hair.She has a square face shape with round forehead with  defined cheeks,  narrow chin, blue eyes, and dimples.She has smoky eye makeup.She is wearing a coral cotton hipster bottoms.She has a light smile, and raised eyebrows.
                    - 30mm Amatuer photo with a harsh white flash and exposure from the camera with a dark background with film grain giving it an authentic amateur feel. hip level shot.A girl undressing in her college dorm, leaning forward, removing her clothes, pulling her top off to become topless.(An undressing girl showing her nipples, breasts, and navel.:1.1)beautiful Yael LÃ³pez, a 21 year old precious whispering girl.She has large breasts.She has a lanky body.She has dark chestnut Voluminous curls with side part hair.She has a round face shape with  defined cheeks,  square chin with cleft, black eyes, and moles.She has runway/editorial makeup.She is wearing a olive backless top, and wide belt..She has a light smile, a shy embarrassed nervous happy expression, red cheeks, and raised eyebrows, looking at the camera.
                    - 30mm Amatuer photo with a harsh white flash and exposure from the camera with a dark background with film grain giving it an authentic amateur feel. over the shoulder shot.A girl undressing in her college dorm, leaning forward, removing her clothes, pulling her top off to become topless.(An undressing girl showing her nipples, breasts, and navel.:1.1)beautiful Elizabeth Harris, a 18 year old untamed girl.She has massive breasts.She has a stacked body.She has brown Long and straight with heavy fringe hair.She has a diamond face shape with angular cheeks with  angular cheeks,  pointed chin with cleft, hazel eyes, and birthmarks.She has sophisticated and polished makeup.She is wearing a dark purple balconette bra, and statement necklace..She has a light smile, a shy embarrassed nervous happy expression, red cheeks, and raised eyebrows, looking at the camera.
                    - 30mm Amatuer photo with a harsh white flash and exposure from the camera with a dark background with film grain giving it an authentic amateur feel. hip level shot.A girl undressing in her college dorm, leaning forward, removing her clothes, pulling her top off to become topless.(An undressing girl showing her nipples, breasts, and navel.:1.1)cute Lea Roberts, a twenty-something devilish girl.She has medium breasts.She has a stacked body.She has red Long bob (lob) with soft waves and side-swept bangs hair.She has a round face shape with  angular cheeks,  receding chin with cleft, deep blue eyes, and high cheekbones.She has edgy makeup.She is wearing a caramel harness bra, and ear cuffs..She has a light smile, a shy embarrassed nervous happy expression, red cheeks, and raised eyebrows, looking at the camera.
                    - score_9,score_8_up,score_7_up,(Soft Lighting Photography by Mimoza Veliu and Mario Giacomelli:1.2),heavy saggy breasts,NSFW,photorealistic,a beautiful 20-year old girl,trying to get dressed before going out for a date,long hairs,4k,high-res,masterpiece,best quality,(polaroid photography:1.5),finely detailed skin,sharp focus,(at night, low light, overexposure),dynamic angle,detailed face:1.2,fitting room,full body,unbuttoned white shirt:1.4,exposed breasts,panty drop or pull,devilkkw/body-2/nudity_partial_focus_on_exposed_ass_or_crotch,devilkkw/body-2/nudity_misc,rating_explicit,tubular breasts,bottomless,starry background,granny flat,<lora:saggy-PN:1.1>,<lora:add-detail-xl:1>,white blond hair,<lora:skin_4:1>
                    - RAW photo, OverallDetail, easynegative, russian village, dark night, nsfw, nude, 1girl, solo, (RAW photo of villager woman), (standing in village house kitchen), (granny):0.4, (Balancing on one foot with arms outstretched), (seductive smile), highly detailed background, intricate details, (excelent complex lighting, cinematic lighting, ray tracing, human perspective), ((mature woman), (51 years old female)):1.5, (fat body), (redhead), (long single braid), (toned skin), (fat face), (bare breasts), (heavy tits), (gigantic tits), (saggy tits), (big nipples, beautiful nipples), (realistic breasts texture), (wide hips), (thick tights), (fat legs), (symmetrical face, detailed face), (wrinkles, wrinkled skin), age spots, (skin pores, skin imperfection), (looking at the viewer), sharp focus, photorealistic, 4k, hdr, ((Hyperrealistic)), dynamic angle
                    - score_9,score_8_up,score_7_up,score_6_up,score_5_up,score_4_up,RAW,8k,very detailed,topless,realistic cum,realistic cumshot,visible breasts,sporty,realistic,real,hyper realistic,(2girls),(source_real:1.5),the cutest face,petite,delicate facial features,(cute face:1.7),epic view,detailed eyes,cum on her body,cum on face,long trails of cum,cumshots,cumtrail,cum dripping on her body,blushing,flirty smile,natural lighting,tight waist,beautiful 18yo,freckles,blush,excessive tanlines,shiny skin,sweat,skin pores,((real photo)),amateur,real life photo,film grain,<lora:AmateurStyle_v1_PONY_REALISM:0.25>,drool,<lora:CumSwapXL:1>,cum pouring from mouth,cum falling from mouth,open mouth,tongue sucking,penis,fellatio,(irrumatio),oral,veiny penis,saliva,(cum in mouth),cum fall another girl mouth,drool,cum on face,CumSwap 2girls,cum on face,cum in throat,cum overflow,excessive cum,(<lora:Cumshot:1.1>),cooperative handjob,
                    - score_9,score_8_up,score_7_up,score_6_up,score_5_up,score_4_up,RAW,8k,very detailed,topless,realistic cum,realistic cumshot,visible breasts,sporty,realistic,real,hyper realistic,(2girls),(source_real:1.5),the cutest face,petite,delicate facial features,(cute face:1.7),epic view,detailed eyes,cum on her body,cum on face,long trails of cum,cumshots,cumtrail,cum dripping on her body,blushing,flirty smile,natural lighting,tight waist,beautiful 18yo,freckles,blush,excessive tanlines,shiny skin,sweat,skin pores,((real photo)),amateur,real life photo,film grain,<lora:AmateurStyle_v1_PONY_REALISM:0.25>,drool,<lora:CumSwapXL:1>,cum pouring from mouth,cum falling from mouth,open mouth,tongue sucking,penis,fellatio,(irrumatio),oral,veiny penis,saliva,(cum in mouth),cum fall another girl mouth,drool,cum on face,CumSwap 2girls,cum on face,cum in throat,cum overflow,excessive cum,<lora:Cumshot:1.1>,cooperative handjob,
                    - score_9,score_8_up,score_7_up,score_6_up,score_5_up,score_4_up,RAW,8k,very detailed,topless,realistic cum,realistic cumshot,brazillian girl,visible breasts,realistic,real,hyper realistic,(2girls),(source_real:1.5),the cutest face,petite,delicate facial features,(cute face:1.7),epic view,detailed eyes,cum on her body,cum on face,long trails of cum,cumshots,cumtrail,cum dripping on her body,blushing,natural lighting,tight waist,beautiful 18yo,freckles,blush,excessive tanlines,shiny skin,sweat,skin pores,((real photo)),amateur,real life photo,film grain,<lora:AmateurStyle_v1_PONY_REALISM:0.55>,drool,<lora:CumSwapXL:1>,cum pouring from mouth,cum falling from mouth,open mouth,tongue sucking,penis,oral,veiny penis,saliva,(cum in mouth),drool,cum on face,CumSwap 2girls,cum on face,cum in throat,cum overflow,(<lora:Cumshot:1.1>),
                    - here i will give you a data set for key words
                    - the prompt should look kinda like the examples with creative new keywords
                    - One more thing. i like sagging low hanging breasts with puffy nipples. so try to blend them in somewhere if possible
                    - Respond only with the new prompt. Nothing else. I repeat just the prompt.
                    - i strongly advice you to reply with only the new prompt.
                    - [prompt] - [style / artist / medium / art movement / photo style]"""
DEFAULT_NEGATIVE_PROMPT = "low quality, extra limbs, low detail"
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
