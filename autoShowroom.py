import sqlite3
import time

class Automobile():
    def __init__(self, brand, model, year, price, hp, transmission, cc):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.hp = hp
        self.transmission = transmission
        self.cc = cc
    def __str__(self):
        return "Brand: {}\nModel: {}\nYear: {}\nPrice: {}\nHP: {}\nTransmission: {}\nCC: {}\n".format(self.brand,self.model,self.year,self.price,self.hp,self.transmission,self.cc)
class Showroom():
    def __init__(self):
        self.connectData()
    def connectData(self):
        self.con = sqlite3.connect("showroom.db")
        self.cursor = self.con.cursor() # I made a mistake here :)
        query = "CREATE TABLE IF NOT EXISTS autos (brand TEXT, model TEXT, year INT, price INT, hp INT, transmission TEXT, cc INT)"
        self.cursor.execute(query)
        self.con.commit()
    def disconnectData(self):
        self.con.close()
    def showAllAutos(self):
        query = "SELECT * FROM autos"
        self.cursor.execute(query)
        autos = self.cursor.fetchall()
        if (len(autos) == 0):
            print("There is not any auto in showroom.")
        else:
            for i in autos:
                auto = Automobile(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(auto)
    def queryAutos(self,brand):
        query = "SELECT * FROM autos WHERE brand = ?"
        self.cursor.execute(query,(brand,))
        autos = self.cursor.fetchall()
        if (len(autos) == 0):
            print("There is not like any brand you asked in showroom.")
        else:
            auto = Automobile(autos[0][0],autos[0][1],autos[0][2],autos[0][3],autos[0][4],autos[0][5],autos[0][6],)
            print(auto)
    def addAuto(self,auto):
        query = "INSERT INTO autos VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(query,(auto.brand, auto.model, auto.year, auto.price, auto.hp, auto.transmission, auto.cc))
        self.con.commit()
    def deleteAuto(self,brand,model,year):
        query = "DELETE FROM autos WHERE brand = ? AND model = ? AND year = ?"
        self.cursor.execute(query,(brand,model,year))
        self.con.commit()
    def raisePrice(self,brand,model,year,cc):
        query = "SELECT * FROM autos WHERE brand = ? AND model = ? AND year = ? AND cc = ?"
        self.cursor.execute(query,(brand,model,year,cc))
        autos = self.cursor.fetchall()
        if (len(autos) == 0):
            print("There is not any auto in showroom.")
        else:
            price = autos[0][3]
            amount = int(input("Enter amount: "))
            price += amount
            querySecond = "UPDATE autos SET price = ? WHERE brand = ? AND model = ? AND year = ? AND cc = ?"
            self.cursor.execute(querySecond,(price,brand,model,year,cc))
            self.con.commit()
    def reducePrice(self,brand,model,year,cc):
        query = "SELECT * FROM autos WHERE brand = ? AND model = ? AND year = ? AND cc = ?"
        self.cursor.execute(query,(brand,model,year,cc))
        autos = self.cursor.fetchall()
        if (len(autos) == 0):
            print("There is not any auto in showroom.")
        else:
            price = autos[0][3]
            amount = int(input("Enter amount: "))
            price -= amount
            querySecond = "UPDATE autos SET price = ? WHERE brand = ? AND model = ? AND year = ? AND cc = ?"
            self.cursor.execute(querySecond,(price,brand,model,year,cc))
            self.con.commit()