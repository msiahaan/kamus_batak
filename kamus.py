import wx
import dialog

class KamusApp(wx.App):
    '''Class Aplikasi Kamus'''
    def __init__(self):
        '''Constructor'''
        wx.App.__init__(self)

    def OnInit(self):
        self.SetAppName('Kamus')
        self.maindialog = dialog.MainDialog()
        self.maindialog.dlg.Show()
        return True

app = KamusApp()
app.MainLoop()
