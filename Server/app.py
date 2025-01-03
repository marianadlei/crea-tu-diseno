from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/placeholder.png')
def serve_image():
    # Asegúrate de usar la ruta absoluta
    return send_from_directory(os.path.abspath(os.getcwd()), 'placeholder.png')

@app.route("/")
def home():
    return "Bienvenido a mi servidor Flask. ¡Todo está funcionando correctamente!"

if __name__ == "__main__":
    app.run(debug=True)
