# -*- coding: utf-8 -*-
import wx.grid
import wx
# import sys
from operationpage import UserOperation
# reload(sys)
# sys.setdefaultencoding('utf8')
#建一个窗口类MyFrame1继承wx.Frame
class MyFrame1(wx.Frame):
    def __init__(self, parent):
        #Wx.Frame (parent, id, title, pos, size, style, name)
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"广油计科17-1电力公司收费管理系统管理系统", pos=wx.DefaultPosition, size=wx.Size(610, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center() #居中显示 # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。

        self.m_panel1 = wx.Panel(self)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作客户表", (130, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作费用管理表", (250, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作收费等级表", (370, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作电类型表", (130, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作结余登记表", (250, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作员工表", (370, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作用电信息表", (130, 160), wx.DefaultSize,
                                    style=wx.BORDER_MASK)

        self.m_button1.Bind(wx.EVT_BUTTON, response().Onclick)

class response():
    def Onclick(self, *args):
        opseration = UserOperation(None, title="广油计科17-1电力公司收费管理系统管理系统操作客户表", size=(1024,668))
        opseration.Show()


class response2():
    def Onclick(self, *args):
        opseration = UserOperation(None, title="操作客户表", size=(1024,668))
        opseration.Show()





if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()