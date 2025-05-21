# chat_console.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# --- 1. Load Configuration ---
load_dotenv()  # Load variables from .env file (like SECRET)

# Get API key and other settings from environment variables
token = os.getenv("SECRET")
endpoint = os.getenv("OPENAI_API_BASE", "https://models.github.ai/inference") # Allow overriding endpoint via .env too
model_name = os.getenv("OPENAI_MODEL_NAME", "openai/gpt-4.1") # Allow overriding model via .env

# --- 2. Validate Configuration ---
if not token:
    print("KLAIDA: 'SECRET' API raktas nerastas aplinkos kintamuosiuose arba .env faile.")
    print("Prašome įsitikinti, kad turite .env failą tame pačiame aplanke kaip ir scenarijus,")
    print("ir jame yra eilutė: SECRET=jūsų_tikras_api_raktas")
    print("Arba nustatykite 'SECRET' aplinkos kintamąjį.")
    exit() # Stop the script if the API key is missing

# --- 3. Initialize AI Client ---
try:
    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )
except Exception as e:
    print(f"Klaida inicijuojant OpenAI klientą: {e}")
    exit()

# --- 4. Define AI Behavior (System Prompt) ---
# Task 9: Force AI to always answer in Lithuanian language.
# Using a Lithuanian prompt for the system might be more effective.
system_instruction = "Tu esi paslaugus dirbtinio intelekto asistentas. Privalai VISADA atsakyti tik lietuvių kalba, nepriklausomai nuo vartotojo klausimo kalbos. Būk mandagus ir paslaugus."
# English alternative (less strong but works):
# system_instruction = "You are a helpful AI assistant. You MUST ALWAYS respond exclusively in the Lithuanian language, regardless of the user's input language. Be polite and helpful."


# --- 5. Main Application Loop ---
print("Sveiki atvykę į AI Pokalbių Programą!")
print("Įveskite savo klausimą arba 'exit' norėdami išeiti.")
print("----------------------------------------------------")

while True:
    # Task 8: Get user input
    user_question = input("Jūs: ")

    # Task 10: Handle 'exit' command
    if user_question.strip().lower() == 'exit':
        print("Programa baigia darbą. Viso gero!")
        break # Exit the while loop

    # Handle empty input
    if not user_question.strip():
        print("AI: Prašome įvesti klausimą.")
        continue # Go to the next iteration of the loop, asking for input again

    # Task 8 (Continued): Call the AI
    try:
        print("AI galvoja...") # Give some feedback to the user
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_instruction,
                },
                {
                    "role": "user",
                    "content": user_question,
                }
            ],
            temperature=0.7,  # Controls randomness: 0.0 (deterministic) to 2.0 (very random)
            top_p=1.0,        # Nucleus sampling: 1.0 considers all tokens
            model=model_name
        )

        ai_answer = response.choices[0].message.content
        print(f"AI: {ai_answer}")

    except Exception as e:
        # Catch potential errors during the API call (network issues, API errors, etc.)
        print(f"Atsiprašome, įvyko klaida bendraujant su AI: {e}")
        print("Prašome pabandyti dar kartą arba patikrinti savo interneto ryšį ir API raktą.")
        # Depending on the error, you might want to 'break' the loop or offer other options.