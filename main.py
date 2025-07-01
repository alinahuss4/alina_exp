from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ OpenAI API key not found.")
    exit()

# Use new client interface (OpenAI SDK v1.x)
client = openai.OpenAI(api_key=api_key)

# Send a prompt to gpt-3.5-turbo
prompt = "Summarise the importance of a balance sheet in finance."

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print("✅ OpenAI Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ OpenAI Error:", e)
