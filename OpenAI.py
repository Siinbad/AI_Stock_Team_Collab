import openai


openai.api_key = "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"


def write_prompt(textbox):
    prompt = textbox
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=.4,
        max_tokens=64
    )
    print(response)
    return response
