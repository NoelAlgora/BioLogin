from resultados import Resultado
import pandas as pd
from sklearn import linear_model
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
import time

nObservations = 0
from pymongo.mongo_client import MongoClient


client = MongoClient('localhost', 27017)
db = client['myDB']
collection = db["biologin"]



def train():
  global nObservations

  records = []
  for v  in collection.find({}):
      res = Resultado()
      res.t_pulsado.append(v["letra1"])
      res.t_pulsado.append(v["letra2"])
      res.t_pulsado.append(v["letra3"])
      res.t_pulsado.append(v["letra4"])
      res.t_pulsado.append(v["letra5"])
      res.t_pulsado.append(v["letra6"])
      res.t_pulsado.append(v["letra7"])
      res.t_pulsado.append(v["letra8"])
      res.t_pulsado.append(v["letra9"])
      res.t_pulsado.append(v["letra10"])
      res.t_pulsado.append(v["letra11"])
      res.t_pulsado.append(v["letra12"])
      res.t_pulsado.append(v["letra13"])
      res.t_pulsado.append(v["letra14"])
      res.t_pulsado.append(v["letra15"])
      res.t_pulsado.append(v["letra16"])
      res.t_pulsado.append(v["letra17"])
      res.t_pulsado.append(v["letra18"])
      res.t_pulsado.append(v["letra19"])
      res.t_vuelo.append(v["vuelo1"])
      res.t_vuelo.append(v["vuelo2"])
      res.t_vuelo.append(v["vuelo3"])
      res.t_vuelo.append(v["vuelo4"])
      res.t_vuelo.append(v["vuelo5"])
      res.t_vuelo.append(v["vuelo6"])
      res.t_vuelo.append(v["vuelo7"])
      res.t_vuelo.append(v["vuelo8"])
      res.t_vuelo.append(v["vuelo9"])
      res.t_vuelo.append(v["vuelo10"])
      res.t_vuelo.append(v["vuelo11"])
      res.t_vuelo.append(v["vuelo12"])
      res.t_vuelo.append(v["vuelo13"])
      res.t_vuelo.append(v["vuelo14"])
      res.t_vuelo.append(v["vuelo15"])
      res.t_vuelo.append(v["vuelo16"])
      res.t_vuelo.append(v["vuelo17"])
      res.t_vuelo.append(v["vuelo18"])
      res.usuario=v["usuario"]
      records.append(res.toTuple())

  features = ["letra1","letra2","letra3","letra4","letra5","letra6","letra7","letra8","letra9","letra10",
              "letra11","letra12","letra13","letra14","letra15","letra16","letra17","letra18","letra19",
              "vuelo1","vuelo2","vuelo3","vuelo4","vuelo5","vuelo6","vuelo7","vuelo8","vuelo9","vuelo10",
              "vuelo11","vuelo12","vuelo13","vuelo14","vuelo15","vuelo16","vuelo17","vuelo18"]
  target = "usuario"

  labels =  features + [target]
  df = pd.DataFrame.from_records(records, columns = labels)
  print ("Before filtering ", df.shape)

  df = df[df.usuario < 10]

  print ("After filtering ", df.shape)

  if df.shape[0] <= nObservations:
    return

  nObservations = df.shape[0]

  params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
            'learning_rate': 0.01, 'loss': 'ls'}
  regr = ensemble.GradientBoostingRegressor(**params)

  X = df[features]
  y = df[target]
  regr  = regr.fit(X, y)


  prediction = regr.predict(X)
  print("Error", mean_squared_error(prediction, y))

  joblib.dump(regr, 'regr.pkl',  protocol=2)
  print("DUMP")
  return df.shape[0]

while True:
  train()
  time.sleep(3)

