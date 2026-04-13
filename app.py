import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurimi i Database-s
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biletat.db'
db = SQLAlchemy(app)

# Modeli i Biletes
class Bileta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itinerari = db.Column(db.String(100), nullable=False)
    cmimi = db.Column(db.Float, nullable=False)
    stoku = db.Column(db.Integer, nullable=False)

# Krijimi i database-s brenda serverit
with app.app_context():
    db.create_all()

@app.route('/')
def klienti():
    biletat = Bileta.query.all()
    return render_template('index.html', biletat=biletat, roli="Klient", shtesa=40)

@app.route('/agjensia')
def agjensia():
    biletat = Bileta.query.all()
    return render_template('index.html', biletat=biletat, roli="Agjensi", shtesa=10)

# PANELI I ADMINIT
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        itinerari = request.form.get('itinerari')
        cmimi = float(request.form.get('cmimi'))
        stoku = int(request.form.get('stoku'))
        
        re_bileta = Bileta(itinerari=itinerari, cmimi=cmimi, stoku=stoku)
        db.session.add(re_bileta)
        db.session.commit()
        return redirect(url_for('admin'))
    
    biletat = Bileta.query.all()
    return render_template('admin.html', biletat=biletat)

@app.route('/delete/<int:id>')
def delete(id):
    bileta_per_fshirje = Bileta.query.get_or_404(id)
    db.session.delete(bileta_per_fshirje)
    db.session.commit()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
