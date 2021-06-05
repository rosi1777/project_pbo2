import ui
import wx
import rajaes


class LoginFrame(ui.Login):
    def __init__(self, parent):
        ui.Login.__init__(self, parent)

    def btnLogin(self, event):

        self.owner = rajaes.Owner()
        listOwner = self.owner.getDataOwner()

        username = self.usernameCtrl.GetValue()
        password = self.passwordCtrl.GetValue()

        tempUsername = []
        tempPassword = []
        tempNama = []
        tempRole = []

        for x in listOwner:
            tempUsername.append(x[0])
            tempPassword.append(x[1])
            tempNama.append(x[2])
            tempRole.append(x[3])

        for i in range(len(tempUsername)):
            if username == tempUsername[i] and password == tempPassword[i]:
                if tempRole[i] == "Owner":
                    OwnerFrame.Show()
                    LoginFrame.Hide()
                elif tempRole[i] != "Owner":
                    OwnerFrame.Show()

class OwnerFrame(ui.OwnerFrame):
    def __init__(self, parent):
        ui.OwnerFrame.__init__(self, parent)

app = wx.App()
OwnerFrame = OwnerFrame(parent=None)
LoginFrame = LoginFrame(parent=None)
LoginFrame.Show()
app.MainLoop()
