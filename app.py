from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)

class cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(10), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('inicio.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = int(request.form['cpf'])
        
        db.session.add(cadastro(nome=nome, email=email, cpf=cpf))
        db.session.commit()
    return render_template('index.html')

@app.route('/tela.html', methods=['GET', 'POST'])
def tela():
    return render_template('tela.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)