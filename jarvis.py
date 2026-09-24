from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv("UNIFIED_API_KEY"),
    base_url = os.getenv("FREELLMAPI_BASE_URL")
)

print("Enter \"bye\" to exit")
while True:
    user_input = input("\nYou: ")

    if user_input.lower().strip() == "bye":
        break

    response = client.chat.completions.create(
        model = "auto",
        messages = [
            {"role": "user", "content": user_input}
        ]
    )
    print(f"Jarvis: {response.choices[0].message.content}")
