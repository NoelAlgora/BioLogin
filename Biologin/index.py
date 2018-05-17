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


@app.route("/entrenar", methods=['POST'])
def entrenar():
  res = Resultado()
  frase = request.form['value']
  if frase == "Tres tristes tigres":
    res.usuario = request.form.get('usuario')
    res.t_vuelo = request.form.getlist('fly[]')
    res.t_pulsado = request.form.getlist('hit[]')
    msg = "Guardado con exito"
    return render_template("trainForm.html", myRes = res, Msg = msg)
  else:
    msg = "Frase introdcida incorrecta"
    return render_template("trainForm.html", myRes = res, Msg = msg) 

@app.route("/predecir", methods=['POST'])
def predecir():
  res = Resultado()
  frase = request.form['value']
  if frase == "Tres tristes tigres":
    res.usuario = request.form.get('usuario')
    res.t_vuelo = request.form.getlist('fly[]')
    res.t_pulsado = request.form.getlist('hit[]')
    msg = "Segun mi prediccion la frase la ha escrito: "
    return render_template("guessForm.html", myRes = res, Msg = msg)
  else:
    msg = "Frase introdcida incorrecta"
    return render_template("guessForm.html", myRes = res, Msg = msg) 

@app.route("/train")
def train():
  res = Resultado()
  return render_template("trainForm.html",myRes = res)

@app.route("/guess")
def guess():
  return render_template("guessForm.html")



app.debug = True

if __name__ == "__main__":
    app.run()