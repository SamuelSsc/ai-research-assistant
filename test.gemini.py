import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Me fale sobre inteligência artificial.")
print(response.text)
