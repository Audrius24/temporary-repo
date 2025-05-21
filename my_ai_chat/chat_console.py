import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the secret API key from the .env file
token = os.getenv("SECRET")
endpoint = "https://models.github.ai/inference"  # your model endpoint
model = "openai/gpt-4.1-mini"  # your model name

# Set up the OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# System message that tells the AI how to behave
system_message = {
    "role": "system",
    "content": "You are a helpful assistant.",
}

# Welcome message
print("Welcome to the AI Console Chat!")
print("Type 'exit' or 'quit' to end the conversation.\n")

# Start the chat loop
while True:
    # Ask user for input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    # Send the message to the AI
    response = client.chat.completions.create(
        messages=[
            system_message,
            {"role": "user", "content": user_input}
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    # Print the AI's reply
    print("AI:", response.choices[0].message.content.strip())
