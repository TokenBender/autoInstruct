from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_response(prompt):
  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": os.getenv("YOUR_SITE_URL"),
      "X-Title": os.getenv("YOUR_APP_TITLE"), 
    },
    model="mistralai/mixtral-8x7b-instruct",
    messages=[
      {
        "role": "user",
        "content": prompt,
      },
    ],
  )
  return completion.choices[0].message.content

# code to load a jsonl file and generate response
with open("input.jsonl", "r") as f:
  for line in f:
    data = json.loads(line)
    instruction = data["instruction"]
    response = generate_response(instruction)