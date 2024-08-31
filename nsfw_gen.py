import os

from groq import Groq

import constants


# The Groq client is used to generate new prompts from the given image
# prompts. The API key is loaded from the environment variable
# GROQ_API_KEY.
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def createPrompts(prompt):
    """
    Create distinctive new prompts from the given image prompt.

    Parameters:
    prompt (str): The original image prompt.

    Returns:
    str: A distinctive new prompt.
    """

    # Create a chat completion using the Groq client
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": constants.DEFAULT_PROMPT_4 if "nsfw" in prompt else constants.DEFAULT_PROMPT_3
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    # Return the generated prompt
    return completion.choices[0].message.content

# print(createPrompts("woman and a man kissing"))
