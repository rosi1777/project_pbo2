from wx.core import MessageBox
import ui
import wx
import rajaes

class dlgAdd(ui.InsertKaryawan):
    def __init__(self, parent, id=-1):
        ui.InsertKaryawan.__init__(self, parent)
        self.parent=parent
        self.id = id

    def submitOnButtonClick( self, event ):
        dlg= wx.MessageDialog(self, 'simpan data', 'Informasi', style=wx.YES_NO)
        retval= dlg.ShowModal()

        if self.id == -1:
            self.parent.insertDataEmployee(self.ctrlUsername.GetValue(), self.ctrlPassword.GetValue(
            ), self.ctrlNama.GetValue(), self.ctrlGender.GetValue(), self.ctrlAlamat.GetValue(), self.ctrlTelepon.GetValue(), self.ctrlTahunMasuk.GetValue())
        else:
            self.parent.updateDataEmp(self.id, self.ctrlUsername.GetValue(), self.ctrlPassword.GetValue(
            ), self.ctrlNama.GetValue(), self.ctrlGender.GetValue(), self.ctrlAlamat.GetValue(), self.ctrlTelepon.GetValue(), self.ctrlTahunMasuk.GetValue())

        self.Destroy()

    def fillDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.ctrlUsername.SetValue(username)
        self.ctrlPassword.SetValue(password)
        self.ctrlNama.SetValue(nama)
        self.ctrlGender.SetValue(gender)
        self.ctrlAlamat.SetValue(alamat)
        self.ctrlTelepon.SetValue(telepon)
        self.ctrlTahunMasuk.SetValue(tanggalMasuk)

class dlgOwner(ui.UpdateOwner):
    def __init__(self, parent):
        ui.UpdateOwner.__init__(self, parent)
        self.parent = parent

    def submitUpdateOwner(self, event):
        dlg = wx.MessageDialog(self, 'simpan data',
                               'Informasi', style=wx.YES_NO)

        self.parent.updateDataO(self.usrCtrl.GetValue(), self.pswCtrl.GetValue(), self.nameCtrl.GetValue())

        self.Destroy()

    def fillDataOwner(self, username, password, nama):
        self.usrCtrl.SetValue(username)
        self.pswCtrl.SetValue(password)
        self.nameCtrl.SetValue(nama)

class LoginFrame(ui.Login):
    def __init__(self, parent):
        ui.Login.__init__(self, parent)

    def loginBtnOnButtonClick( self, event ):
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
        login=False

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
                    login=True
                    self.Hide()
                elif tempRole[i] != "Owner":
                    EmployeeFrame.Show()
                    self.Hide()
                    login=True

        if login!=True:
            alert=wx.MessageDialog(None, "username dan password salah","pemeberitahuan", wx.YES_DEFAULT)
            asw=alert.ShowModal()


class OwnerFrame(ui.OwnerFrame):
    def __init__(self, parent):
        ui.OwnerFrame.__init__(self, parent)
        self.showAccount()
        self.showItem()
        self.showOrder()
        self.showSale()
        self.showEmployee()
        self.AddBtnKaryawan()
        # self.AddBtnSale()
        # self.AddBtnBarang()
        # self.AddBtnPesanan()
        
    def logoutBtn(self, event):
        OwnerFrame.Hide()
        LoginFrame.Show()

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

    def UpdateAccount(self, event):
        dlgO = dlgOwner(self)
        dlgO.ShowModal()

    def updateDataO(self, username, password, nama):
        self.owner.updateDataOwner(username, password, nama)
        self.showAccount()
    
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
        
        self.Barang.Fit()
        self.dataBarang.Layout()

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

        self.Pesanan.Fit()
        self.dataPesanan.Layout()


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
        self.Penjualan.Fit()
        self.dataPenjualan.Layout()

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
    
    def AdEmpBtnOnButtonClick( self, event ):
        dlg = dlgAdd(self)
        dlg.ShowModal()

    def insertDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.employee.addDataEmployee(
            username, password, nama, gender, alamat, telepon, tanggalMasuk)
        self.showEmployee()
        self.AddBtnKaryawan()

    def updateDataEmp(self, id, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.employee.updateDataEmployee(id, username, password, nama, gender, alamat, telepon, tanggalMasuk)
        self.showEmployee()
        self.AddBtnKaryawan()

    def tabelEmployeeOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 8:
            # wx.MessageBox('Edit data', 'Informasi')
            id = self.lstIdEmployee[baris]
            dlg = dlgAdd(self, id)
            userName = self.Karyawan.GetCellValue(baris, 1)
            psw = self.Karyawan.GetCellValue(baris, 2)
            name = self.Karyawan.GetCellValue(baris, 3)
            gnder = self.Karyawan.GetCellValue(baris, 4)
            address = self.Karyawan.GetCellValue(baris, 5)
            phone = self.Karyawan.GetCellValue(baris, 6)
            dat = self.Karyawan.GetCellValue(baris, 7)
            dlg.fillDataEmployee(userName, psw, name, gnder, address, phone, dat)
            dlg.ShowModal()
        elif kolom == 9:
            dlg = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.employee.deleteEmployee(self.lstIdEmployee[baris])
                self.showEmployee()
                self.AddBtnKaryawan()

    # def AddBtnSale(self):
    #     jmlKolom = self.Penjualan.GetNumberCols()
    #     self.Penjualan.AppendCols(2)
    #     colEdit = jmlKolom
    #     colDelete = jmlKolom + 1

    #     self.Penjualan.SetColLabelValue(colEdit, '')
    #     self.Penjualan.SetColLabelValue(colDelete, '')

    #     for row in range(self.Penjualan.GetNumberRows()):
    #         self.Penjualan.SetCellValue(row, colEdit, 'Edit')
    #         self.Penjualan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
    #         self.Penjualan.SetCellTextColour(row, colEdit, wx.WHITE)

    #         self.Penjualan.SetCellValue(row, colDelete, 'Delete')
    #         self.Penjualan.SetCellBackgroundColour(row, colDelete, wx.RED)
    #         self.Penjualan.SetCellTextColour(row, colDelete, wx.WHITE)

        

    def AddBtnKaryawan(self):
        jmlKolom = self.Karyawan.GetNumberCols()
        self.Karyawan.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.Karyawan.SetColLabelValue(colEdit, '')
        self.Karyawan.SetColLabelValue(colDelete, '')

        for row in range(self.Karyawan.GetNumberRows()):
            self.Karyawan.SetCellValue(row, colEdit, 'Edit')
            self.Karyawan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.Karyawan.SetCellTextColour(row, colEdit, wx.WHITE)

            self.Karyawan.SetCellValue(row, colDelete, 'Delete')
            self.Karyawan.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.Karyawan.SetCellTextColour(row, colDelete, wx.WHITE)

        self.Karyawan.Fit()
        self.infoAkun.Layout()

    # def AddBtnBarang(self):
    #     jmlKolom = self.Barang.GetNumberCols()
    #     self.Barang.AppendCols(2)
    #     colEdit = jmlKolom
    #     colDelete = jmlKolom + 1

    #     self.Barang.SetColLabelValue(colEdit, '')
    #     self.Barang.SetColLabelValue(colDelete, '')

    #     for row in range(self.Barang.GetNumberRows()):
    #         self.Barang.SetCellValue(row, colEdit, 'Edit')
    #         self.Barang.SetCellBackgroundColour(row, colEdit, wx.BLUE)
    #         self.Barang.SetCellTextColour(row, colEdit, wx.WHITE)

    #         self.Barang.SetCellValue(row, colDelete, 'Delete')
    #         self.Barang.SetCellBackgroundColour(row, colDelete, wx.RED)
    #         self.Barang.SetCellTextColour(row, colDelete, wx.WHITE)

        
    
    # def AddBtnPesanan(self):
    #     jmlKolom = self.Pesanan.GetNumberCols()
    #     self.Pesanan.AppendCols(2)
    #     colEdit = jmlKolom
    #     colDelete = jmlKolom + 1

    #     self.Pesanan.SetColLabelValue(colEdit, '')
    #     self.Pesanan.SetColLabelValue(colDelete, '')

    #     for row in range(self.Pesanan.GetNumberRows()):
    #         self.Pesanan.SetCellValue(row, colEdit, 'Edit')
    #         self.Pesanan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
    #         self.Pesanan.SetCellTextColour(row, colEdit, wx.WHITE)

    #         self.Pesanan.SetCellValue(row, colDelete, 'Delete')
    #         self.Pesanan.SetCellBackgroundColour(row, colDelete, wx.RED)
    #         self.Pesanan.SetCellTextColour(row, colDelete, wx.WHITE)

        
        
        

class EmployeeFrame(ui.EmployeeFrame):
    def __init__(self, parent):
        ui.EmployeeFrame.__init__(self, parent)


app = wx.App()
OwnerFrame = OwnerFrame(parent=None)
EmployeeFrame = EmployeeFrame(parent=None)
LoginFrame = LoginFrame(parent=None)
LoginFrame.Show()
app.MainLoop()
