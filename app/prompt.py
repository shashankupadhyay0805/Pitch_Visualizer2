import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

STYLE = "digital illustration, cinematic lighting, concept art"

def enhance_prompt(sentence):

    prompt = f"""
Convert the following sentence into a detailed cinematic visual scene.

Sentence:
{sentence}

Style:
{STYLE}

Return only the visual scene description for an image generator.
"""

    try:

        response = model.generate_content(prompt)

        if response.text:
            return response.text.strip()

    except Exception as e:
        print("Prompt generation error:", e)

    return sentence + ", " + STYLE