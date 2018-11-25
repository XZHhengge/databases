# -*- coding: utf-8 -*-
import wx
class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        nm = wx.StaticBox(panel, -1, 'Name:')
        nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)

        nmbox = wx.BoxSizer(wx.HORIZONTAL)
        fn = wx.StaticText(panel, -1, "First Name")

        nmbox.Add(fn, 0, wx.ALL | wx.CENTER, 5)
        nm1 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
        nm2 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
        ln = wx.StaticText(panel, -1, "Last Name")

        nmbox.Add(nm1, 0, wx.ALL | wx.CENTER, 5)
        nmbox.Add(ln, 0, wx.ALL | wx.CENTER, 5)
        nmbox.Add(nm2, 0, wx.ALL | wx.CENTER, 5)
        nmSizer.Add(nmbox, 0, wx.ALL | wx.CENTER, 10)

        sbox = wx.StaticBox(panel, -1, 'buttons:')
        sboxSizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(panel, -1, 'ok')

        hbox.Add(okButton, 0, wx.ALL | wx.LEFT, 10)
        cancelButton = wx.Button(panel, -1, 'cancel')
        testButton = wx.Button(panel, -1, 'test')
        testButton1 = wx.Button(panel, -1, 'test1')
        hbox.Add(testButton, 0, wx.ALL | wx.LEFT, 10)
        hbox.Add(testButton1, 0, wx.ALL | wx.LEFT, 10)
        hbox.Add(cancelButton, )

        sboxSizer.Add(hbox, 0, wx.ALL | wx.LEFT, 10)
        vbox.Add(nmSizer, 0, wx.ALL | wx.CENTER, 5)
        vbox.Add(sboxSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(vbox)
        self.Centre()

        panel.Fit()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Mywin(None, 'Staticboxsizer Demo - www.yiibai.com')
    app.MainLoop()