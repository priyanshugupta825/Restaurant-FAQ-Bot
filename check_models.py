from google import genai

GEMINI_API_KEY = "AIzaSyCw1SIlctGIemIRJF8oOYsvOLqWz48aG4Q"  # ← paste your key

client = genai.Client(api_key=GEMINI_API_KEY)

print("Available models:")
for model in client.models.list():
    print(" -", model.name)