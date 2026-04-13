import os
from flask import Flask, render_template

app = Flask(__name__)

# Këtu mund të ndryshosh biletat manualisht
biletat = [
    {"itinerari": "Tirane - Londer", "cmimi": 100, "stoku": 5},
    {"itinerari": "Tirane - Rome", "cmimi": 60, "stoku": 10},
    {"itinerari": "Tirane - Zakynthos", "cmimi": 120, "stoku": 8}
]

@app.route('/')
def klienti():
    # Çmimi me +40 EUR shtesë
    return render_template('index.html', biletat=biletat, roli="Klient", shtesa=40)

@app.route('/agjensia')
def agjensia():
    # Çmimi me +10 EUR shtesë
    return render_template('index.html', biletat=biletat, roli="Agjensi", shtesa=10)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
