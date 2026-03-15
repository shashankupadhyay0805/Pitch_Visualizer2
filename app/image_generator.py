import os
import uuid

from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_API_KEY"),
)


def generate_image(prompt):

    try:

        image = client.text_to_image(
            prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0"
        )

        filename = f"static/images/{uuid.uuid4()}.png"

        image.save(filename)

        return filename

    except Exception as e:

        print("Image generation failed:", e)

        return "static/images/error.png"