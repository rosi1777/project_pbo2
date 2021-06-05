import sqlite3

class RajaEs:
    def __init__(self):
        self.con = sqlite3.connect("rajaes.db")
        self.cursor = self.con.cursor()

    def executeQuery(self, query, retVal = False):
        self.cursor.execute(query)
        all_result = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_result

class Owner(RajaEs):

    def updateDataOwner(self, username, password, nama):
        self.query = "UPDATE owner SET username = ?, password = ?, nama = ? where id = 1"
        self.query = self.query % (username, password, nama)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataOwner(self):
        self.query = "SELECT username, password, nama, role FROM owner"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result
