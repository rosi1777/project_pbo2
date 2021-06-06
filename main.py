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
            tempUsername.append(y[0])
            tempPassword.append(y[1])
            tempNama.append(y[2])
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

    def showAccount(self):

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

class EmployeeFrame(ui.EmployeeFrame):
    def __init__(self, parent):
        ui.EmployeeFrame.__init__(self, parent)


app = wx.App()
OwnerFrame = OwnerFrame(parent=None)
EmployeeFrame = EmployeeFrame(parent=None)
LoginFrame = LoginFrame(parent=None)
LoginFrame.Show()
app.MainLoop()
