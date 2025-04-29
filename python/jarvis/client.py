from openai import OpenAI

client = OpenAI(
    api_key = "",
    # pip install openai
)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": "you are a virtual assistant named Jarvis. You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is the weather like today?"
        }
    ]
)

print(completion.choices[0].message.content)