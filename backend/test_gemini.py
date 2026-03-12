# test_gemini.py
import os
from dotenv import load_dotenv
load_dotenv()

from google import genai  # this is correct for the new SDK

# Initialize the client (it picks up GEMINI_API_KEY from env)
client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a short motivational quote."
    )
    print("Gemini Response:\n", response.text)
except Exception as e:
    print("Error calling Gemini:", e)