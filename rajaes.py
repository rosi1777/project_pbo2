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
        self.query = "SELECT id, username, password, nama, role FROM owner"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result


class Employee(RajaEs):

    def updateDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk, idKaryawan):
        self.query = "UPDATE employee SET username = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ?, tanggalMasuk = ? WHERE id = ?"
        self.query = self.query % (
            username, password, nama, gender, alamat, telepon, tanggalMasuk, idKaryawan)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataEmployee(self):
        self.query = "SELECT * FROM employee"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class Item(RajaEs):

    def getDataItem(self):
        self.query = "SELECT * FROM item"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class Order(RajaEs):

    def getDataOrder(self):
        self.query = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'proses'"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class Sale(RajaEs):

    def getDataSale(self):
        self.query = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'selesai'"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result
