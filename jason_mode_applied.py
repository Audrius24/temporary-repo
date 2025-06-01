import openai
import os

from dotenv import load_dotenv
from pydantic import BaseModel
from rich import print

load_dotenv()

git remote add origin <your-repo-url>