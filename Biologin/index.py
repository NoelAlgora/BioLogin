from flask import Flask, render_template, request, make_response
from random import randint
from time import time

import datetime
import sklearn
from sklearn.externals import joblib

from resultados import Resultado
app = Flask(__name__)

@app.route("/")
def selectAction():
  return render_template("selectForm.html")

@app.route("/entrenar", methods=['GET', 'POST'])
def entrenar():
  res = Resultado()
  res.t_pulsado = []
  res.t_vuelo = []
  if request.method == 'POST':
    frase = request.form['value']
    if frase == "Tres tristes tigres":
      res.usuario = request.form.get('usuario')
      fly = request.form.getlist('fly[]')
      hit = request.form.getlist('hit[]')
      res.toFloatHit(hit)
      res.toFloatFly(fly)
      res.save()
      msg = "Guardado con exito"
      return render_template("trainForm.html", myRes = res, Msg = msg)
    else:
      msg = "Frase introdcida incorrecta"
      return render_template("trainForm.html", myRes = res, Msg = msg)
  if request.method == 'GET':
    return render_template("trainForm.html",myRes = res)

@app.route("/predecir", methods=['GET','POST'])
def predecir():
  res = Resultado()
  res.t_pulsado = []
  res.t_vuelo = []
  if request.method == 'POST':
    frase = request.form['value']
    if frase == "Tres tristes tigres":
      fly = request.form.getlist('fly[]')
      hit = request.form.getlist('hit[]')
      res.toFloatHit(hit)
      res.toFloatFly(fly)
      regr = joblib.load('gbc.pkl')
      res.predict(regr)
      msg = "Segun mi prediccion la frase la ha escrito: "
      return render_template("guessForm.html", myRes = res, Msg = msg)
    else:
      msg = "Frase introdcida incorrecta"
      return render_template("guessForm.html", myRes = res, Msg = msg)
  if request.method == 'GET':
    return render_template("guessForm.html",myRes = res)


app.debug = True

if __name__ == "__main__":
    app.run()