from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hola desde Flask en Docker! hOLA"})

@app.route("/vista")
def vista():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Bonito</title>
        <style>
            body {
                background: linear-gradient(135deg, #4e73df, #1cc88a);
                font-family: 'Segoe UI', sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                width: 350px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                animation: fadeIn 1s ease-in-out;
            }
            h1 {
                margin-bottom: 10px;
                font-size: 2rem;
            }
            p {
                font-size: 1.2rem;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to   { opacity: 1; transform: translateY(0); }
            }
            a {
                color: #e8f0fe;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola desde Flask!</h1>
            <p>Esta es una vista con HTML y CSS sin usar nada extra.</p>
            <p><a href="/">Ver JSON original</a></p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
