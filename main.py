from wx.core import MessageBox
import ui
import wx
import rajaes


class dlgAdd(ui.InsertKaryawan):
    def __init__(self, parent, id=-1):
        ui.InsertKaryawan.__init__(self, parent)
        self.parent = parent
        self.id = id

    def submitOnButtonClick(self, event):
        dlg = wx.MessageDialog(self, 'simpan data',
                               'Informasi', style=wx.YES_NO)
        retval = dlg.ShowModal()

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

        self.parent.updateDataO(self.usrCtrl.GetValue(
        ), self.pswCtrl.GetValue(), self.nameCtrl.GetValue())

        self.Destroy()

    def fillDataOwner(self, username, password, nama):
        self.usrCtrl.SetValue(username)
        self.pswCtrl.SetValue(password)
        self.nameCtrl.SetValue(nama)

class dlgAddItem(ui.InsertBarang):
    def __init__(self, parent, id=-1):
        ui.InsertBarang.__init__(self, parent)
        self.parent = parent
        self.id = id

    def submitItem(self, event):
        dlgI = wx.MessageDialog(self, 'simpan data',
                               'Informasi', style=wx.YES_NO)
        retval = dlgI.ShowModal()

        if self.id == -1:
            self.parent.insertDataItem(self.m_textCtrl3.GetValue(), self.m_textCtrl5.GetValue(
            ), self.m_textCtrl6.GetValue(), self.m_textCtrl24.GetValue())
        else:
            self.parent.updateDataBarang(self.id, self.m_textCtrl3.GetValue(), self.m_textCtrl5.GetValue(
            ), self.m_textCtrl6.GetValue(), self.m_textCtrl24.GetValue())

        self.Destroy()

    def fillDataItem(self, nama, hargaJual, hargaBeli, stok):
        self.m_textCtrl3.SetValue(nama)
        self.m_textCtrl5.SetValue(hargaJual)
        self.m_textCtrl6.SetValue(hargaBeli)
        self.m_textCtrl24.SetValue(stok)

class dlgAddOrder(ui.PenjualanPesanan):
    def __init__(self, parent, id=-1):
        ui.PenjualanPesanan.__init__(self, parent)
        self.parent = parent
        self.id = id

    def submitOrderSale(self, event):
        dlgP = wx.MessageDialog(self, 'simpan data',
                               'Informasi', style=wx.YES_NO)
        retval = dlgP.ShowModal()

        if self.id == -1:
            self.parent.insertDataOrder(self.namaCtrl.GetValue(), self.alamatCtrl.GetValue(
            ), self.barangCtrl.GetValue(), self.totalCtrl.GetValue(), self.dateCtrl.GetValue(), self.statusCtrl.GetValue())
        else:
            self.parent.updateDataPesanan(self.id, self.namaCtrl.GetValue(), self.alamatCtrl.GetValue(
            ), self.barangCtrl.GetValue(), self.totalCtrl.GetValue(), self.dateCtrl.GetValue(), self.statusCtrl.GetValue())

        self.Destroy()

    def fillDataOrder(self, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.namaCtrl.SetValue(namaPemesan)
        self.alamatCtrl.SetValue(alamat)
        self.barangCtrl.SetValue(barang)
        self.totalCtrl.SetValue(jumlah)
        self.dateCtrl.SetValue(tanggalPesan)
        self.statusCtrl.SetValue(status)

class dlgAddSale(ui.PenjualanPesanan):
    def __init__(self, parent, id):
        ui.PenjualanPesanan.__init__(self, parent)
        self.parent = parent
        self.id = id

    def submitOrderSale(self, event):
        dlgS = wx.MessageDialog(self, 'simpan data',
                                'Informasi', style=wx.YES_NO)
        retval = dlgS.ShowModal()

        self.parent.updateDataPenjualan(self.id, self.namaCtrl.GetValue(), self.alamatCtrl.GetValue(), self.barangCtrl.GetValue(), self.totalCtrl.GetValue(), self.dateCtrl.GetValue(), self.statusCtrl.GetValue())

        self.Destroy()

    def fillDataSale(self, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.namaCtrl.SetValue(namaPemesan)
        self.alamatCtrl.SetValue(alamat)
        self.barangCtrl.SetValue(barang)
        self.totalCtrl.SetValue(jumlah)
        self.dateCtrl.SetValue(tanggalPesan)
        self.statusCtrl.SetValue(status)

class LoginFrame(ui.Login):
    def __init__(self, parent):
        ui.Login.__init__(self, parent)

    def loginBtnOnButtonClick(self, event):
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
        login = False

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
                    login = True
                    self.Hide()
                elif tempRole[i] != "Owner":
                    EmployeeFrame.Show()
                    self.Hide()
                    login = True

        if login != True:
            alert = wx.MessageDialog(
                None, "username dan password salah", "pemeberitahuan", wx.YES_DEFAULT)
            asw = alert.ShowModal()


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

        colums = ['ID', 'Nama Pemesana', 'Alamat',
                  'Order', "Jumlah", "Tanggal Pesanan", "Status"]
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

    def AdEmpBtnOnButtonClick(self, event):
        dlg = dlgAdd(self)
        dlg.ShowModal()

    def insertDataEmployee(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.employee.addDataEmployee(
            username, password, nama, gender, alamat, telepon, tanggalMasuk)
        self.showEmployee()
        self.AddBtnKaryawan()

    def updateDataEmp(self, id, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.employee.updateDataEmployee(
            id, username, password, nama, gender, alamat, telepon, tanggalMasuk)
        self.showEmployee()
        self.AddBtnKaryawan()

    def tabelEmployeeOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 8:
            id = self.lstIdEmployee[baris]
            dlg = dlgAdd(self, id)
            userName = self.Karyawan.GetCellValue(baris, 1)
            psw = self.Karyawan.GetCellValue(baris, 2)
            name = self.Karyawan.GetCellValue(baris, 3)
            gnder = self.Karyawan.GetCellValue(baris, 4)
            address = self.Karyawan.GetCellValue(baris, 5)
            phone = self.Karyawan.GetCellValue(baris, 6)
            dat = self.Karyawan.GetCellValue(baris, 7)
            dlg.fillDataEmployee(userName, psw, name,
                                 gnder, address, phone, dat)
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

class EmployeeFrame(ui.EmployeeFrame):
    def __init__(self, parent):
        ui.EmployeeFrame.__init__(self, parent)
        self.showBarang()
        self.showOrder()
        self.showSale()
        self.AddBtnBarang()
        self.AddBtnPesanan()
        self.AddBtnSale()

    def logoutBtnClik(self, event):
        EmployeeFrame.Hide()
        LoginFrame.Show()

    def showBarang(self):

        n_cols = self.Item.GetNumberCols()
        n_rows = self.Item.GetNumberRows()
        if n_cols > 0:
            self.Item.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Item.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama', 'Harga Jual', 'Harga Beli', "Stok"]
        self.Item.AppendCols(len(colums))

        self.item = rajaes.Item()
        listItem = self.item.getDataItem()
        row = 0

        self.lstIdItem = []
        for col in range(len(colums)):
            self.Item.SetColLabelValue(
                col, colums[col])
        for item_row in listItem:
            self.Item.AppendRows(1)

            print(row, '. ', item_row)
            id, nama, hargaJual, hargaBeli, stok = item_row
            ids = str(id)
            hargaJuals = str(hargaJual)
            hargaBelis = str(hargaBeli)
            stoks = str(stok)
            self.Item.SetCellValue(row, 0, ids)
            self.Item.SetCellValue(row, 1, nama)
            self.Item.SetCellValue(row, 2, hargaJuals)
            self.Item.SetCellValue(row, 3, hargaBelis)
            self.Item.SetCellValue(row, 4, stoks)
            self.lstIdItem.append(id)
            row += 1

        self.Item.Fit()
        self.barang.Layout()

    def addItemBtn(self, event):
        dlgI = dlgAddItem(self)
        dlgI.ShowModal()

    def insertDataItem(self, nama, hargaJual, hargaBeli, stok):
        self.item.addDataItem(
            nama, hargaJual, hargaBeli, stok)
        self.showBarang()
        self.AddBtnBarang()

    def updateDataBarang(self, id, nama, hargaJual, hargaBeli, stok):
        self.item.updateDataItem(
            id, nama, hargaJual, hargaBeli, stok)
        self.showBarang()
        self.AddBtnBarang()

    def tabelItemOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 5:
            id = self.lstIdItem[baris]
            dlgI = dlgAddItem(self, id)
            name = self.Item.GetCellValue(baris, 1)
            jual = self.Item.GetCellValue(baris, 2)
            beli = self.Item.GetCellValue(baris, 3)
            stok = self.Item.GetCellValue(baris, 4)
            dlgI.fillDataItem( name, jual, beli, stok)
            dlgI.ShowModal()
        elif kolom == 6:
            dlgI = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlgI.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.item.deleteItem(self.lstIdItem[baris])
                self.showBarang()
                self.AddBtnBarang()

    def AddBtnBarang(self):
        jmlKolom = self.Item.GetNumberCols()
        self.Item.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.Item.SetColLabelValue(colEdit, '')
        self.Item.SetColLabelValue(colDelete, '')

        for row in range(self.Item.GetNumberRows()):
            self.Item.SetCellValue(row, colEdit, 'Edit')
            self.Item.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.Item.SetCellTextColour(row, colEdit, wx.WHITE)

            self.Item.SetCellValue(row, colDelete, 'Delete')
            self.Item.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.Item.SetCellTextColour(row, colDelete, wx.WHITE)

    def showOrder(self):
        n_cols = self.Order.GetNumberCols()
        n_rows = self.Order.GetNumberRows()
        if n_cols > 0:
            self.Order.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Order.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama Pemesana', 'Alamat',
                  'Order', "Jumlah", "Tanggal Pesanan", "Status"]
        self.Order.AppendCols(len(colums))

        self.order = rajaes.Order()
        listOrder = self.order.getDataOrder()
        row = 0

        self.lstIdOrder = []
        for col in range(len(colums)):
            self.Order.SetColLabelValue(
                col, colums[col])
        for order_row in listOrder:
            self.Order.AppendRows(1)

            print(row, '. ', order_row)
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status = order_row
            ids = str(id)
            total = str(jumlah)
            self.Order.SetCellValue(row, 0, ids)
            self.Order.SetCellValue(row, 1, namaPemesan)
            self.Order.SetCellValue(row, 2, alamat)
            self.Order.SetCellValue(row, 3, barang)
            self.Order.SetCellValue(row, 4, total)
            self.Order.SetCellValue(row, 5, tanggalPesan)
            self.Order.SetCellValue(row, 6, status)
            self.lstIdOrder.append(id)
            row += 1

        self.Order.Fit()
        self.pesanan.Layout()

    def addOrderBtn(self, event):
        dlgP = dlgAddOrder(self)
        dlgP.ShowModal()

    def insertDataOrder(self, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.order.addDataOrder(
            namaPemesan, alamat, barang, jumlah, tanggalPesan, status)
        self.showOrder()
        self.AddBtnPesanan()

    def updateDataPesanan(self, id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.order.updateDataOrder(
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status)
        self.showOrder()
        self.AddBtnPesanan()

    def tabelOrder(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 7:
            id = self.lstIdOrder[baris]
            dlgP = dlgAddOrder(self, id)
            pemesan = self.Order.GetCellValue(baris, 1)
            addre = self.Order.GetCellValue(baris, 2)
            itm = self.Order.GetCellValue(baris, 3)
            tlt = self.Order.GetCellValue(baris, 4)
            tglp = self.Order.GetCellValue(baris, 5)
            sts = self.Order.GetCellValue(baris, 6)
            dlgP.fillDataOrder(pemesan, addre, itm,
                              tlt, tglp, sts)
            dlgP.ShowModal()
        elif kolom == 8:
            dlgP = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlgP.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.order.deleteOrder(self.lstIdOrder[baris])
                self.showOrder()
                self.AddBtnPesanan()

    def AddBtnPesanan(self):
        jmlKolom = self.Order.GetNumberCols()
        self.Order.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.Order.SetColLabelValue(colEdit, '')
        self.Order.SetColLabelValue(colDelete, '')

        for row in range(self.Order.GetNumberRows()):
            self.Order.SetCellValue(row, colEdit, 'Edit')
            self.Order.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.Order.SetCellTextColour(row, colEdit, wx.WHITE)

            self.Order.SetCellValue(row, colDelete, 'Delete')
            self.Order.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.Order.SetCellTextColour(row, colDelete, wx.WHITE)

    def showSale(self):
        n_cols = self.Sale.GetNumberCols()
        n_rows = self.Sale.GetNumberRows()
        if n_cols > 0:
            self.Sale.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Sale.DeleteRows(0, n_rows, True)

        colums = ['ID', 'Nama Pemesana', 'Alamat',
                  'Order', "Jumlah", "Tanggal Pesanan", "Status"]
        self.Sale.AppendCols(len(colums))

        self.sale = rajaes.Sale()
        listSale = self.sale.getDataSale()
        row = 0

        self.lstIdSale = []
        for col in range(len(colums)):
            self.Sale.SetColLabelValue(
                col, colums[col])
        for sale_row in listSale:
            self.Sale.AppendRows(1)

            print(row, '. ', sale_row)
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status = sale_row
            ids = str(id)
            total = str(jumlah)
            self.Sale.SetCellValue(row, 0, ids)
            self.Sale.SetCellValue(row, 1, namaPemesan)
            self.Sale.SetCellValue(row, 2, alamat)
            self.Sale.SetCellValue(row, 3, barang)
            self.Sale.SetCellValue(row, 4, total)
            self.Sale.SetCellValue(row, 5, tanggalPesan)
            self.Sale.SetCellValue(row, 6, status)
            self.lstIdSale.append(id)
            row += 1
        self.Sale.Fit()
        self.penjualan.Layout()

    def updateDataPenjualan(self, id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.sale.updateDataSale(
            id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status)
        self.showSale()
        self.AddBtnSale()

    def tabelSale(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)
        if kolom == 7:
            id = self.lstIdSale[baris]
            dlgS = dlgAddSale(self, id)
            pemesan = self.Sale.GetCellValue(baris, 1)
            addre = self.Sale.GetCellValue(baris, 2)
            itm = self.Sale.GetCellValue(baris, 3)
            tlt = self.Sale.GetCellValue(baris, 4)
            tglp = self.Sale.GetCellValue(baris, 5)
            sts = self.Sale.GetCellValue(baris, 6)
            dlgS.fillDataSale(pemesan, addre, itm,
                               tlt, tglp, sts)
            dlgS.ShowModal()
        
        elif kolom == 8:
            dlgS = wx.MessageDialog(
                self, 'Hapus data', 'Informasi', style=wx.YES_NO)
            retval = dlgS.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.sale.deleteSale(self.lstIdSale[baris])
                self.showSale()
                self.AddBtnSale()

    def AddBtnSale(self):
        jmlKolom = self.Sale.GetNumberCols()
        self.Sale.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.Sale.SetColLabelValue(colEdit, '')
        self.Sale.SetColLabelValue(colDelete, '')

        for row in range(self.Sale.GetNumberRows()):
            self.Sale.SetCellValue(row, colEdit, 'Edit')
            self.Sale.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.Sale.SetCellTextColour(row, colEdit, wx.WHITE)

            self.Sale.SetCellValue(row, colDelete, 'Delete')
            self.Sale.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.Sale.SetCellTextColour(row, colDelete, wx.WHITE)


app = wx.App()
OwnerFrame = OwnerFrame(parent=None)
EmployeeFrame = EmployeeFrame(parent=None)
LoginFrame = LoginFrame(parent=None)
LoginFrame.Show()
app.MainLoop()
