from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def ligar_bd():
    return sqlite3.connect("cliques.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clique", methods=["POST"])
def registar_clique():
    dados = request.get_json()
    botao = dados["botao"]
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = ligar_bd()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clicks (botao, data_hora) VALUES (?, ?)",
        (botao, data_hora)
    )
    conn.commit()
    conn.close()

    return jsonify({"estado": "ok"})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


