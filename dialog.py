import sys
import wx
from wx import xrc
from entry import words

dialogxrc = None

class MainDialog:
    def __init__(self):
        global dialogxrc
        dialogxrc = xrc.XmlResource('kamus.xrc')
        self.dlg = dialogxrc.LoadDialog(None, 'dUtama')

        # customize widgets

        self.getControl('bTerjemahkan').Bind(wx.EVT_BUTTON, self.onTerjemahkan)
        self.getControl('bKeluar').Bind(wx.EVT_BUTTON, self.onKeluar)

    def getControl(self, xmlid):
        control = self.dlg.FindWindowById(xrc.XRCID(xmlid))
        assert control != None, 'Programming Error: control with xmlid ' + xmlid + ' was not found'
        return control

    def onTerjemahkan(self, event):
        wBatak = self.getControl('tBatak').GetValue().title()
        try:
            wIndonesia = words[wBatak]
        except KeyError:
            wIndonesia = 'No entry!'
            
        self.getControl('tIndonesia').SetValue(wIndonesia)

    def onKeluar(self, event):
        sys.exit()