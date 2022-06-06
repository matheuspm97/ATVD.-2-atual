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
  sex = int(request.form['sex'])
  age = int(request.form['age'])
  cp = int(request.form['cp'])
  chol = int(request.form['chol'])
  thal = int(request.form['thal'])
  thalach = int(request.form['thalach'])
  exang = int(request.form['exang'])
  predicao = model.predict([[sex, age, cp, chol, thal, thalach, exang]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)

# git add .
# git commit -m "nomenovo"
# git push

#0 - Baixa probabilidade de ter doença cardiovascular
#1 - Alta probabilidade de ter doença cardiovasculas