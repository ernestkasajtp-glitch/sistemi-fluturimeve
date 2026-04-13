import os
from flask import Flask, render_template

app = Flask(__name__)

# Biletat e tua
biletat = [
    {"itinerari": "Tiranë - Londër", "cmimi": 100, "stoku": 5},
    {"itinerari": "Tiranë - Romë", "cmimi": 60, "stoku": 10}
]

@app.route('/')
def klienti():
    return render_template('index.html', biletat=biletat, roli="Klient", shtesa=40)

@app.route('/agjensia')
def agjensia():
    return render_template('index.html', biletat=biletat, roli="Agjensi", shtesa=10)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
