import ui
import wx


class MyGui(ui.Login):
    def __init__(self, parent):
        ui.Login.__init__(self, parent)

app = wx.App()
frame = MyGui(parent=None)
frame.Show()
app.MainLoop()
