from pymongo.mongo_client import MongoClient
import datetime

class Resultado():

    t_pulsado = []
    t_vuelo = []
    usuario = ""
    usuario_predicho = ""
    prediction = ""
    
    def toFloatHit(self,list):
        for item in list:
            self.t_pulsado.append(int(item))
    def toFloatFly(self,list):
        for item in list:
            self.t_vuelo.append(int(item))

    def tPulsadoAdd(self,val):
        self.t_pulsado.append(val)

    def tVueloAdd(self,val):
        self.t_vuelo.append(val)

    def toTuple(self):
        return (self.t_pulsado[0],self.t_pulsado[1],self.t_pulsado[2],self.t_pulsado[3],
                self.t_pulsado[4],self.t_pulsado[5], self.t_pulsado[6],self.t_pulsado[7],
                self.t_pulsado[8], self.t_pulsado[9],self.t_pulsado[10],self.t_pulsado[11],
                self.t_pulsado[12],self.t_pulsado[13],self.t_pulsado[14],self.t_pulsado[15],
                self.t_pulsado[16],self.t_pulsado[17],self.t_pulsado[18],
                self.t_vuelo[0],self.t_vuelo[1],self.t_vuelo[2],self.t_vuelo[3],self.t_vuelo[4],
                self.t_vuelo[5], self.t_vuelo[6],self.t_vuelo[7],self.t_vuelo[8],self.t_vuelo[9],
                self.t_vuelo[10],self.t_vuelo[11], self.t_vuelo[12],self.t_vuelo[13],self.t_vuelo[14],
                self.t_vuelo[15],self.t_vuelo[16],self.t_vuelo[17],
                self.usuario)
    
    def predict(self, model):
        self.prediction = model.predict([self.toTuple()[:-1]])[0]
        if self.prediction == 0:
            self.usuario_predicho = "Noel"
        else:
            self.usuario_predicho = "Ivan"

    def save(self):
        if self.usuario == "Noel":
            target = int(0)
        else:
            target = int(1)
        biolog = {
            
            "letra1": self.t_pulsado[0],
            "letra2": self.t_pulsado[1],
            "letra3": self.t_pulsado[2],
            "letra4": self.t_pulsado[3],
            "letra5": self.t_pulsado[4],
            "letra6": self.t_pulsado[5],
            "letra7": self.t_pulsado[6],
            "letra8": self.t_pulsado[7],
            "letra9": self.t_pulsado[8],
            "letra10": self.t_pulsado[9],
            "letra11": self.t_pulsado[10],
            "letra12": self.t_pulsado[11],
            "letra13": self.t_pulsado[12],
            "letra14": self.t_pulsado[13],
            "letra15": self.t_pulsado[14],
            "letra16": self.t_pulsado[15],
            "letra17": self.t_pulsado[16],
            "letra18": self.t_pulsado[17],
            "letra19": self.t_pulsado[18],
            "vuelo1": self.t_vuelo[0],
            "vuelo2": self.t_vuelo[1],
            "vuelo3": self.t_vuelo[2],
            "vuelo4": self.t_vuelo[3],
            "vuelo5": self.t_vuelo[4],
            "vuelo6": self.t_vuelo[5],
            "vuelo7": self.t_vuelo[6],
            "vuelo8": self.t_vuelo[7],
            "vuelo9": self.t_vuelo[8],
            "vuelo10": self.t_vuelo[9],
            "vuelo11": self.t_vuelo[10],
            "vuelo12": self.t_vuelo[11],
            "vuelo13": self.t_vuelo[12],
            "vuelo14": self.t_vuelo[13],
            "vuelo15": self.t_vuelo[14],
            "vuelo16": self.t_vuelo[15],
            "vuelo17": self.t_vuelo[16],
            "vuelo18": self.t_vuelo[17],
            "usuario":  target
        }

        client = MongoClient('localhost', 27017)
        db = client['myDB']
        collection = db["biologin"]
        collection.insert_one(biolog)