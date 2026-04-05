from flask import Flask, render_template, request
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

app = Flask(__name__)

# Conectar con Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.readonly"]
creds = Credentials.from_service_account_file("credenciales.json", scopes=SCOPES)
cliente = gspread.authorize(creds)

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

    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gracias – GestLogística</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'DM Sans', sans-serif;
            background: #F0EEE9;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        header {
            background: #0A0F8F;
            height: 160px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        header::after {
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, #5EBE82, #0A0F8F, #221D5C);
        }
        header img {
            height: 100%;
            object-fit: contain;
            padding: 20px 0;
        }
        .page {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 48px 20px;
        }
        .card {
            background: white;
            border-radius: 20px;
            box-shadow: 0 4px 40px rgba(10,15,143,0.08);
            max-width: 520px;
            width: 100%;
            overflow: hidden;
            text-align: center;
            animation: fadeUp 0.5s ease;
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .card-top {
            background: linear-gradient(135deg, #0A0F8F 0%, #221D5C 100%);
            padding: 48px 40px 40px;
            position: relative;
            overflow: hidden;
        }
        .card-top::before {
            content: '';
            position: absolute;
            top: -40px; right: -40px;
            width: 160px; height: 160px;
            border-radius: 50%;
            background: rgba(94,190,130,0.15);
        }
        .check-circle {
            width: 72px;
            height: 72px;
            background: rgba(94,190,130,0.2);
            border: 2px solid rgba(94,190,130,0.5);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
            position: relative;
        }
        .check-circle svg {
            width: 32px;
            height: 32px;
            stroke: #5EBE82;
            stroke-width: 2.5;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .card-top h2 {
            font-family: 'DM Serif Display', serif;
            font-size: 26px;
            font-weight: 400;
            color: white;
            margin-bottom: 10px;
            position: relative;
        }
        .card-top p {
            font-size: 14px;
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
            font-weight: 300;
            position: relative;
        }
        .card-bottom {
            padding: 32px 40px 36px;
        }
        .card-bottom p {
            font-size: 14px;
            color: #888;
            line-height: 1.7;
            font-weight: 300;
        }
        .card-bottom strong {
            color: #0A0F8F;
            font-weight: 600;
        }
        .divider {
            height: 1px;
            background: #F0EEE9;
            margin: 24px 0;
        }
        .footer-note {
            font-size: 12px;
            color: #bbb;
        }
    </style>
</head>
<body>
<header>
    <img src="/static/assets/logo1.svg" alt="GestLogística">
</header>
<div class="page">
    <div class="card">
        <div class="card-top">
            <div class="check-circle">
                <svg viewBox="0 0 24 24">
                    <polyline points="20 6 9 17 4 12"/>
                </svg>
            </div>
            <h2>¡Gracias por su opinión!</h2>
            <p>Su respuesta ha sido registrada correctamente.</p>
        </div>
        <div style="text-align: center; margin-top: 24px;">
            <img src="/static/assets/robot-gestlogistica1.png"
                style="width: 180px; opacity: 0.92; pointer-events: none;"
                alt="">
        </div>
        <div class="card-bottom">
            <p>En <strong>GestLogística</strong> valoramos profundamente su tiempo y sus comentarios. Cada respuesta nos ayuda a seguir mejorando el servicio que le ofrecemos.</p>
            <div class="divider"></div>
            <p class="footer-note">Sus respuestas son confidenciales y serán usadas únicamente para mejorar nuestro servicio.</p>
        </div>
    </div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)