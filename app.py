import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  sex = request.form['sex']
  age = request.form['age']
  cp = request.form['cp']
  chol = request.form['chol']
  thal = request.form['thal']
  thalach = request.form['thalach']
  exang = request.form['exang']
  predicao = model.predict([sex, age, cp, chol, thal, thalach, exang])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
