import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("WEBSITE_SITE_NAME", "Local / desconocido")
    region = os.getenv("REGION_NAME", "No disponible")
    instance_id = os.getenv("WEBSITE_INSTANCE_ID", "No disponible")
    port = os.getenv("PORT", "8000")

    return f"""
    <html>
        <head>
            <title>Info App Service</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 40px;
                }}
                .card {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    max-width: 600px;
                    margin: auto;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #2c3e50;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 App Service Info</h1>
                <p><strong>Nombre de la app:</strong> {app_name}</p>
                <p><strong>Región:</strong> {region}</p>
                <p><strong>Instance ID:</strong> {instance_id}</p>
                <p><strong>Puerto:</strong> {port}</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
