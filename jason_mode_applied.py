import openai
import os

from dotenv import load_dotenv
from pydantic import BaseModel
from rich import print
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

model = "gpt-4o"  # Use a valid OpenAI model

question = input("Enter your question: ")

# Step 1: Language Detection
class LithuanianQuestionCheck(BaseModel):
    is_lithuanian_language: bool

lang_detection_prompt = (
    "You are a helpful assistant that detects if the user is speaking Lithuanian. "
    "Respond with JSON: {\"is_lithuanian_language\": true/false}."
)

lang_detection_response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": lang_detection_prompt},
        {"role": "user", "content": question}
    ],
    temperature=0.3,
)

language_check = json.loads(lang_detection_response.choices[0].message.content)

# Step 2: Answer if Lithuanian
if language_check and language_check.get("is_lithuanian_language"):
    print("[bold green]Detected Lithuanian language. Answering question...[/bold green]")

    answer_response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Atsakyk į klausimus lietuvių kalba kuo tiksliau ir aiškiau."},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
    )

    answer = answer_response.choices[0].message.content
    print("[bold blue]Atsakymas:[/bold blue]", answer)

else:
    print("[bold red]Klausimas nėra lietuvių kalba. Prašome pateikti klausimą lietuviškai.[/bold red]")