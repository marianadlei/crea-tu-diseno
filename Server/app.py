from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuración de Flask
app = Flask(__name__)

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data["prompt"]

    try:
        # Llamada a la API de OpenAI para generar la imagen
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
