import os

from flask import Flask, render_template, send_file

app = Flask(__name__)


# Rota específica para StreamingAssets
@app.route('/StreamingAssets/<path:filename>')
def serve_streaming_assets(filename):
    streaming_assets_path = os.path.join('static', 'StreamingAssets', filename)

    # Verifica se o arquivo existe
    if not os.path.isfile(streaming_assets_path):
        return "File not found", 404

    return send_file(streaming_assets_path)

@app.route('/')
def home():
    return render_template("home.html")
