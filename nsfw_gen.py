from groq import Groq

import constants

client = Groq(
    api_key="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",
)


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
                "content": constants.DEFAULT_PROMPT_3
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
