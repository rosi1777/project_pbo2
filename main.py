import ui
import wx
import rajaes


class LoginFrame(ui.Login):
    def __init__(self, parent):
        ui.Login.__init__(self, parent)

    def btnLogin(self, event):

        self.owner = rajaes.Owner()
        listOwner = self.owner.getDataOwner()

        self.employee = rajaes.Employee()
        listEmployee = self.employee.getDataEmployee()

        username = self.usernameCtrl.GetValue()
        password = self.passwordCtrl.GetValue()

        tempUsername = []
        tempPassword = []
        tempNama = []
        tempRole = []

        for x in listOwner:
            tempUsername.append(x[1])
            tempPassword.append(x[2])
            tempNama.append(x[3])
            tempRole.append(x[4])

        for y in listEmployee:
            tempUsername.append(y[1])
            tempPassword.append(y[2])
            tempNama.append(y[3])
            tempRole.append(y[4])

        for i in range(len(tempUsername)):
            if username == tempUsername[i] and password == tempPassword[i]:
                if tempRole[i] == "Owner":
                    OwnerFrame.Show()
                    LoginFrame.Hide()
                elif tempRole[i] != "Owner":
                    EmployeeFrame.Show()
                    LoginFrame.Hide()


class OwnerFrame(ui.OwnerFrame):
    def __init__(self, parent):
        ui.OwnerFrame.__init__(self, parent)
        self.showAccount()
        self.showItem()
        self.showOrder()
        self.showSale()
        self.showEmployee()

    def showAccount(self):

        n_cols = self.Akun.GetNumberCols()
        n_rows = self.Akun.GetNumberRows()
        if n_cols > 0:
            self.Akun.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Akun.DeleteRows(0, n_rows, True)

        colums = ['Username', 'Password', 'Nama']
        self.Akun.AppendCols(len(colums))

        self.owner = rajaes.Owner()
        listOwner = self.owner.getDataOwner()
        row = 0

        self.lstIdOwner = []
        for col in range(len(colums)):
            self.Akun.SetColLabelValue(
                col, colums[col]) 
        for owner_row in listOwner:
            self.Akun.AppendRows(1)

            print(row, '. ', owner_row)
            id, username, password, nama, role = owner_row
            self.Akun.SetCellValue(row, 0, username)
            self.Akun.SetCellValue(row, 1, password)
            self.Akun.SetCellValue(row, 2, nama)
            self.lstIdOwner.append(id)
            row += 1
    
    def showItem(self):

        n_cols = self.Barang.GetNumberCols()
        n_rows = self.Barang.GetNumberRows()
        if n_cols > 0:
            self.Barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Barang.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama', 'Harga Jual', 'Harga Beli', "Stok"]
        self.Barang.AppendCols(len(colums))

        self.item = rajaes.Item()
        listItem = self.item.getDataItem()
        row = 0

        self.lstIdItem = []
        for col in range(len(colums)):
            self.Barang.SetColLabelValue(
                col, colums[col])
        for item_row in listItem:
            self.Barang.AppendRows(1)

            print(row, '. ', item_row)
            id, nama, hargaJual, hargaBeli, stok = item_row
            ids = str(id)
            hargaJuals = str(hargaJual)
            hargaBelis = str(hargaBeli)
            stoks = str(stok)
            self.Barang.SetCellValue(row, 0, ids)
            self.Barang.SetCellValue(row, 1, nama)
            self.Barang.SetCellValue(row, 2, hargaJuals)
            self.Barang.SetCellValue(row, 3, hargaBelis)
            self.Barang.SetCellValue(row, 4, stoks)
            self.lstIdItem.append(id)
            row += 1

    def showOrder(self):
        n_cols = self.Pesanan.GetNumberCols()
        n_rows = self.Pesanan.GetNumberRows()
        if n_cols > 0:
            self.Pesanan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Pesanan.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama Pemesana', 'Alamat', 'Order', "Jumlah", "Tanggal Pesanan", "Status"]
        self.Pesanan.AppendCols(len(colums))

        self.order = rajaes.Order()
        listOrder = self.order.getDataOrder()
        row = 0

        self.lstIdOrder = []
        for col in range(len(colums)):
            self.Pesanan.SetColLabelValue(
                col, colums[col])
        for order_row in listOrder:
            self.Pesanan.AppendRows(1)

            print(row, '. ', order_row)
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status = order_row
            ids = str(id)
            total = str(jumlah)
            self.Pesanan.SetCellValue(row, 0, ids)
            self.Pesanan.SetCellValue(row, 1, namaPemesan)
            self.Pesanan.SetCellValue(row, 2, alamat)
            self.Pesanan.SetCellValue(row, 3, barang)
            self.Pesanan.SetCellValue(row, 4, total)
            self.Pesanan.SetCellValue(row, 5, tanggalPesan)
            self.Pesanan.SetCellValue(row, 6, status)
            self.lstIdOrder.append(id)
            row += 1

    def showSale(self):
        n_cols = self.Penjualan.GetNumberCols()
        n_rows = self.Penjualan.GetNumberRows()
        if n_cols > 0:
            self.Penjualan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Penjualan.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama Pemesana', 'Alamat',
                  'Order', "Jumlah", "Tanggal Pesanan", "Status"]
        self.Penjualan.AppendCols(len(colums))

        self.sale = rajaes.Sale()
        listSale = self.sale.getDataSale()
        row = 0

        self.lstIdSale = []
        for col in range(len(colums)):
            self.Penjualan.SetColLabelValue(
                col, colums[col])
        for sale_row in listSale:
            self.Penjualan.AppendRows(1)

            print(row, '. ', sale_row)
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status = sale_row
            ids = str(id)
            total = str(jumlah)
            self.Penjualan.SetCellValue(row, 0, ids)
            self.Penjualan.SetCellValue(row, 1, namaPemesan)
            self.Penjualan.SetCellValue(row, 2, alamat)
            self.Penjualan.SetCellValue(row, 3, barang)
            self.Penjualan.SetCellValue(row, 4, total)
            self.Penjualan.SetCellValue(row, 5, tanggalPesan)
            self.Penjualan.SetCellValue(row, 6, status)
            self.lstIdSale.append(id)
            row += 1

    def showEmployee(self):
        n_cols = self.Karyawan.GetNumberCols()
        n_rows = self.Karyawan.GetNumberRows()
        if n_cols > 0:
            self.Karyawan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Karyawan.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Username', 'Password',
                  'Nama', "Gender", "Alamat", "Telepon", "Tanggal Masuk"]
        self.Karyawan.AppendCols(len(colums))

        self.employee = rajaes.Employee()
        listEmployee = self.employee.getDataEmployee()
        row = 0

        self.lstIdEmployee = []
        for col in range(len(colums)):
            self.Karyawan.SetColLabelValue(
                col, colums[col])
        for employee_row in listEmployee:
            self.Karyawan.AppendRows(1)

            print(row, '. ', employee_row)
            id, username, pasword, nama, gender, alamat, telepon, tanggalMasuk = employee_row
            ids = str(id)
            phone = str(telepon)
            self.Karyawan.SetCellValue(row, 0, ids)
            self.Karyawan.SetCellValue(row, 1, username)
            self.Karyawan.SetCellValue(row, 2, pasword)
            self.Karyawan.SetCellValue(row, 3, nama)
            self.Karyawan.SetCellValue(row, 4, gender)
            self.Karyawan.SetCellValue(row, 5, alamat)
            self.Karyawan.SetCellValue(row, 6, phone)
            self.Karyawan.SetCellValue(row, 7, tanggalMasuk)
            self.lstIdEmployee.append(id)
            row += 1

class EmployeeFrame(ui.EmployeeFrame):
    def __init__(self, parent):
        ui.EmployeeFrame.__init__(self, parent)


app = wx.App()
OwnerFrame = OwnerFrame(parent=None)
EmployeeFrame = EmployeeFrame(parent=None)
LoginFrame = LoginFrame(parent=None)
LoginFrame.Show()
app.MainLoop()
