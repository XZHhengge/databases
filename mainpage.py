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
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作员工", (250, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作收费登记表", (370, 20), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作用电信息表", (130, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作用电类型表", (250, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作费用管理表", (370, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        # self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作用电信息表", (130, 160), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)

        self.m_button1.Bind(wx.EVT_BUTTON, response().Onclick)
        self.m_button2.Bind(wx.EVT_BUTTON, response().Onclick2)
        self.m_button3.Bind(wx.EVT_BUTTON, response().Onclick3)
        self.m_button4.Bind(wx.EVT_BUTTON, response().Onclick4)
        self.m_button5.Bind(wx.EVT_BUTTON, response().Onclick5)
        self.m_button6.Bind(wx.EVT_BUTTON, response().Onclick6)
# 客户
class response():
    def Onclick(self, *args):
        opseration = UserOperation('客户', '客户号','客户名', '地址', '联系方式',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作客户表", size=(1024,668))
        opseration.Show()
        # 员工
    def Onclick2(self, *args):
        opseration = UserOperation('员工', '员工号', '姓名', '性别', '联系方式',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作员工表", size=(1024,668))
        opseration.Show()

    # 收费登记
    def Onclick3(self, *args):
        opseration = UserOperation('收费登记', '客户号', '月份', '员工号', '应收费用', '实收费用', '结余费用',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作收费登记表", size=(1024,668))
        opseration.Show()

    # 用电信息
    def Onclick4(self, *args):
        opseration = UserOperation('用电信息', '客户号', '类别号', '月份', '客户_客户号', '用电度数',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作用电信息表", size=(1024,668))
        opseration.Show()

# 用电类型
    def Onclick5(self, *args):
        opseration = UserOperation('用电类型', '类别号', '类别名', '电价',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作用电类型表", size=(1024,668))
        opseration.Show()

# 费用管理
    def Onclick6(self, *args):
        opseration = UserOperation('费用管理', '客户号', '月份', '员工号', '费用', '收费标志',
                                   title="广油计科17-1电力公司收费管理系统管理系统操作费用管理表", size=(1024,668))
        opseration.Show()





if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()