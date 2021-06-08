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
        self.query = "UPDATE owner SET username = \'%s\', password = \'%s\', nama = \'%s\' where id = 1"
        self.query = self.query % (username, password, nama)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataOwner(self):
        self.query = "SELECT id, username, password, nama, role FROM owner"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class Employee(RajaEs):

    def updateDataEmployee(self, id, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.query = "UPDATE employee SET username = \'%s\', password = \'%s\', nama = \'%s\', gender = \'%s\', alamat = \'%s\', telepon = \'%s\', tanggalMasuk = \'%s\' WHERE id = %i"
        self.query = self.query % (username, password, nama, gender, alamat, telepon, tanggalMasuk, id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataEmployee(self):
        self.query = "SELECT * FROM employee"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

    def addDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.query = 'INSERT INTO employee (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (
            username, password, nama, gender, alamat, telepon, tanggalMasuk)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def deleteEmployee(self, id):
        self.query = 'DELETE FROM employee where id = %i'
        self.query = self.query % (id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

class Item(RajaEs):

    def getDataItem(self):
        self.query = "SELECT * FROM item"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

    def addDataItem(self, nama, hargaJual, hargaBeli, stok):
        self.query = 'INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (
            nama, hargaJual, hargaBeli, stok)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def deleteItem(self, id):
        self.query = 'DELETE FROM item where id = %i'
        self.query = self.query % (id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def updateDataItem(self, id, nama, hargaJual, hargaBeli, stok):
        self.query = "UPDATE item SET nama = \'%s\', hargaJual = \'%s\', hargaBeli = \'%s\', stok = \'%s\' WHERE id = %i"
        self.query = self.query % (
            nama, hargaJual, hargaBeli, stok, id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

class Order(RajaEs):

    def getDataOrder(self):
        self.query = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'proses'"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

    def addDataOrder(self, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.query = 'INSERT INTO ordered (namaPemesan, alamat, barang, jumlah, tanggalPesan, status) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
        self.query = self.query % (
            namaPemesan, alamat, barang, jumlah, tanggalPesan, status)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def deleteOrder(self, id):
        self.query = 'DELETE FROM ordered where id = %i'
        self.query = self.query % (id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def updateDataOrder(self, id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.query = "UPDATE ordered SET namaPemesan = \'%s\', alamat = \'%s\', barang = \'%s\', jumlah = \'%s\', tanggalPesan = \'%s\', status = \'%s\' WHERE id = %i"
        self.query = self.query % (
            namaPemesan, alamat, barang, jumlah, tanggalPesan, status, id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

class Sale(RajaEs):

    def getDataSale(self):
        self.query = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'selesai'"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

    def deleteSale(self, id):
        self.query = 'DELETE FROM ordered where id = %i'
        self.query = self.query % (id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def updateDataSale(self, id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.query = "UPDATE ordered SET namaPemesan = \'%s\', alamat = \'%s\', barang = \'%s\', jumlah = \'%s\', tanggalPesan = \'%s\', status = \'%s\' WHERE id = %i"
        self.query = self.query % (
            namaPemesan, alamat, barang, jumlah, tanggalPesan, status, id)
        print('self.query : ', self.query)
        self.executeQuery(self.query)
