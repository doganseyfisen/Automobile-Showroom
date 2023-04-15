import sqlite3


class Automobile:
    def __init__(self, brand, model, year, price, hp, transmission, cc):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.hp = hp
        self.transmission = transmission
        self.cc = cc

    def __str__(self):
        return "Brand: {}\nModel: {}\nYear: {}\nPrice: {}\n" \
               "HP: {}\nTransmission: {}\nCC: {}\n".format(self.brand,
                                                           self.model,
                                                           self.year,
                                                           self.price, self.hp,
                                                           self.transmission,
                                                           self.cc)


class Showroom:
    def __init__(self):
        self.cursor = None
        self.con = None
        self.connect_data()

    def connect_data(self):
        self.con = sqlite3.connect("showroom.db")
        self.cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS autos (brand TEXT, model TEXT, " \
                "year INT, price INT, hp INT, transmission TEXT, cc INT)"
        self.cursor.execute(query)
        self.con.commit()

    def disconnect_data(self):
        self.con.close()

    def show_all_autos(self):
        query = "SELECT * FROM autos"
        self.cursor.execute(query)
        autos = self.cursor.fetchall()

        if len(autos) == 0:
            print("There is not any auto in showroom.")

        else:
            for i in autos:
                auto = Automobile(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                print(auto)

    def query_autos(self, brand):
        query = "SELECT * FROM autos WHERE brand = ?"
        self.cursor.execute(query, (brand,))
        autos = self.cursor.fetchall()

        if len(autos) == 0:
            print("There is not like any brand you asked in showroom.")

        else:
            auto = Automobile(autos[0][0], autos[0][1], autos[0][2],
                              autos[0][3], autos[0][4], autos[0][5],
                              autos[0][6], )
            print(auto)

    def add_auto(self, auto):
        query = "INSERT INTO autos VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(query, (
            auto.brand, auto.model, auto.year, auto.price, auto.hp,
            auto.transmission, auto.cc))
        self.con.commit()

    def delete_auto(self, brand, model, year):
        query = "DELETE FROM autos WHERE brand = ? AND model = ? AND year = ?"
        self.cursor.execute(query, (brand, model, year))
        self.con.commit()

    def raise_price(self, brand, model, year, cc):
        query = "SELECT * FROM autos WHERE brand = ? AND model = ? AND year " \
                "= ? AND cc = ?"
        self.cursor.execute(query, (brand, model, year, cc))
        autos = self.cursor.fetchall()

        if len(autos) == 0:
            print("There is not any auto in showroom.")

        else:
            price = autos[0][3]
            amount = int(input("Enter amount: "))
            price += amount
            query_second = "UPDATE autos SET price = ? WHERE brand = ? AND " \
                           "model = ? AND year = ? AND cc = ?"
            self.cursor.execute(query_second, (price, brand, model, year, cc))
            self.con.commit()

    def reduce_price(self, brand, model, year, cc):
        query = "SELECT * FROM autos WHERE brand = ? AND model = ? AND year " \
                "= ? AND cc = ?"
        self.cursor.execute(query, (brand, model, year, cc))
        autos = self.cursor.fetchall()

        if len(autos) == 0:
            print("There is not any auto in showroom.")

        else:
            price = autos[0][3]
            amount = int(input("Enter amount: "))
            price -= amount
            query_second = "UPDATE autos SET price = ? WHERE brand = ? AND " \
                           "model = ? AND year = ? AND cc = ?"
            self.cursor.execute(query_second, (price, brand, model, year, cc))
            self.con.commit()
