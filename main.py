import os
import json
from flask import Flask, render_template, request
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURACIÓN DE CREDENCIALES (EL CAMBIO ESTÁ AQUÍ) ---
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]

# 1. Intentamos leer la variable de entorno que pusiste en Render
google_creds_env = os.environ.get('GOOGLE_CREDS_JSON')

if google_creds_env:
    # Si existe (estamos en Render), cargamos el texto JSON
    info = json.loads(google_creds_env)
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
else:
    # Si no existe (estamos en tu PC), usamos el archivo local
    creds = Credentials.from_service_account_file("credenciales.json", scopes=SCOPES)

cliente = gspread.authorize(creds)
# ---------------------------------------------------------

# Abre tu hoja — pon el nombre exacto de tu Google Sheet
hoja = cliente.open("Gestlogística reseñas").sheet1

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    pregunta1 = request.form["pregunta1"]
    pregunta2 = request.form["pregunta2"]
    comentario1 = request.form.get("comentario1", "")
    comentario2 = request.form.get("comentario2", "")

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    hoja.append_row([fecha, pregunta1, comentario1, pregunta2, comentario2])

    # ... (el resto de tu HTML de "Gracias" se mantiene igual) ...
    return render_template("gracias.html", pregunta1=pregunta1, pregunta2=pregunta2)

if __name__ == "__main__":
    # Importante: Render usa la variable PORT, si no la encuentra usa 8000
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)