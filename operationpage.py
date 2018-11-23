# -*- coding: utf-8 -*-
import wx
import wx.grid
from sql import Sql_operation

class UserOperation(wx.Frame):
# class UserOperation(wx.Dialog):
    '''
    操作界面
    '''

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(UserOperation, self).__init__(None, **kw)
        # 设置窗口屏幕居中
        self.Center()
        # 创建窗口
        self.pnl = wx.Panel(self)
        # 调用操作界面函数
        self.OperationInterface(self, *args)

    def OperationInterface(self, *args):
        # 创建垂直方向box布局管理器

        global info
        info = args[1:]
        if len(info) > 1:
            with open('test.txt', 'w') as f:
                for i in info:
                    f.write(i+'\n')
        elif len(info) == 1:
            pass
        with open('test.txt', 'r') as f:
            #str->list
            info = f.read().splitlines()
            global table
            table = info[0]
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        # 创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl, label="")
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        # 添加logo静态文本到vbox布局管理器
        self.vbox.Add(logo, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=5)
        #################################################################################
        # 创建静态框
        sb_button = wx.StaticBox(self.pnl, label="选择操作")
        # 创建垂直方向box布局管理器
        vsbox_button = wx.StaticBoxSizer(sb_button, wx.VERTICAL)
        # 创建操作按钮、绑定事件处理
        check_button = wx.Button(self.pnl, id=10, label='查', size=(150, 50))
        add_button = wx.Button(self.pnl, id=11, label="增", size=(150, 50))
        delete_button = wx.Button(self.pnl, id=12, label="删", size=(150, 50))
        change_button = wx.Button(self.pnl, id=14, label ="改", size=(150,50))
        quit_button = wx.Button(self.pnl, id=13, label="退出", size=(150, 50))
        self.Bind(wx.EVT_BUTTON, self.ClickButton, id=10, id2=13)
        # 添加操作按钮到vsbox布局管理器
        vsbox_button.Add(add_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(delete_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(change_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(check_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(quit_button, 0, wx.EXPAND | wx.BOTTOM, 200)
        # 创建静态框
        sb_show_operation = wx.StaticBox(self.pnl, label="显示/操作窗口", size=(800, 500))
        # 创建垂直方向box布局管理器
        self.vsbox_show_operation = wx.StaticBoxSizer(sb_show_operation, wx.VERTICAL)
        # 创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        hbox.Add(vsbox_button, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(self.vsbox_show_operation, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 将hbox添加到垂直box
        self.vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        #################################################################################
        self.pnl.SetSizer(self.vbox)

    def ClickButton(self, event, *args):
        source_id = event.GetId()
        if source_id == 10:
            print("初始化查询操作！")
            inquire_button = InquireOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            print("初始化添加操作！")
            add_button = AddOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            print("初始化删除操作！")
            del_button = DelOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            self.Close(True)


# 继承UserOperation类，实现初始化操作界面
class InquireOp(UserOperation):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(InquireOp, self).__init__(None, **kw)
        # 创建学生信息网格
        self.stu_grid = self.CreateGrid(self, info)
        # self.stu_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelleftClick)
        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(self.stu_grid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 30)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            pass
        elif source_id == 11:
            print("InquireOp添加操作！")
            add_button = AddOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            print("InquireOp删除操作！")
            del_button = DelOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            self.Close(True)

    def CreateGrid(self, *args):
        # 连接login_users数据库
        op = Sql_operation("databases")
        # 获取stu_information表中的学生信息，返回为二维元组
        np = op.FindAll(table)
        column_names = (info[i] for i in range(len(info)))
        column_names = tuple(column_names)
        stu_grid = wx.grid.Grid(self.pnl)
        stu_grid.CreateGrid(len(np), len(np[0]) - 1)
        for row in range(len(np)):
            stu_grid.SetRowLabelValue(row  , str(np[row][0]) )  # 确保网格序列号与数据库id保持一致
            for col in range(1, len(np[row])):
                stu_grid.SetColLabelValue(col - 1, column_names[col])
                stu_grid.SetCellValue(row, col - 1, str(np[row][col]))
        stu_grid.AutoSize()
        return stu_grid

    # def OnLabelleftClick(self, event):
    #     # 连接login_users数据库
    #     op = Sql_operation("databases")
    #     # 获取users表中的用户名和密码信息，返回为二维元组
    #     np = op.FindAll(b)
    #     print("RowIdx: {0}".format(event.GetRow()))
    #     print("ColIdx: {0}".format(event.GetRow()))
    #     print(np[event.GetRow()])
    #     event.Skip()


# 继承UserOperation类，实现初始化操作界面
class AddOp(UserOperation):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(AddOp, self).__init__(*args, **kw)
        # 创建添加学生信息输入框、添加按钮
        self.stu_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_gender = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_age = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_cid = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_classid = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_phone = wx.TextCtrl(self.pnl, size=(210, 25))
        self.stu_cost = wx.TextCtrl(self.pnl, size=(210,25))
        self.add_affirm = wx.Button(self.pnl, label="添加", size=(80, 25))
        # 为添加按钮组件绑定事件处理
        self.add_affirm.Bind(wx.EVT_BUTTON, self.AddAffirm)
        #################################################################################
        # 创建静态框
        sb_name = wx.StaticBox(self.pnl, label="{}".format(info[1]))
        sb_age = wx.StaticBox(self.pnl, label="{}".format(info[2]))
        sb_cid = wx.StaticBox(self.pnl, label="{}".format(info[3]))
        sb_classid = wx.StaticBox(self.pnl, label="{}".format(info[4]))
        try:
            sb_gender = wx.StaticBox(self.pnl, label="{}".format(info[5]))
        except:
            pass
        # 创建水平方向box布局管理器
        try:
            sb_phone = wx.StaticBox(self.pnl, label="{}".format(info[6]))
        except:
            pass

        # try:
        #     sb_cost = wx.StaticBox(self.pnl, label = )
        hsbox_name = wx.StaticBoxSizer(sb_name, wx.HORIZONTAL)
        hsbox_age = wx.StaticBoxSizer(sb_age, wx.HORIZONTAL)
        hsbox_cid = wx.StaticBoxSizer(sb_cid, wx.HORIZONTAL)
        hsbox_classid = wx.StaticBoxSizer(sb_classid, wx.HORIZONTAL)
        try:
            hsbox_gender = wx.StaticBoxSizer(sb_gender, wx.HORIZONTAL)
        except:
            pass

        # 添加到hsbox布局管理器
        try:
            hsbox_phone = wx.StaticBoxSizer(sb_phone, wx.HORIZONTAL)
        except:
            pass



        hsbox_name.Add(self.stu_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_age.Add(self.stu_age, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_cid.Add(self.stu_cid, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_classid.Add(self.stu_classid, 0, wx.EXPAND | wx.BOTTOM, 5)
        try:
            hsbox_gender.Add(self.stu_gender, 0, wx.EXPAND | wx.BOTTOM, 5)
        except:
            pass
        try:
            hsbox_phone.Add(self.stu_phone, 0, wx.EXPAND | wx.BOTTOM, 5)
        except:
            pass
        #################################################################################
        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(hsbox_name, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_age, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_cid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_classid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        try:
            self.vsbox_show_operation.Add(hsbox_gender, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        except:
            pass
        try:
            self.vsbox_show_operation.Add(hsbox_phone, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        except:
            pass
        self.vsbox_show_operation.Add(self.add_affirm, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            print("AddOp查询操作！")
            inquire_button = InquireOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            pass
        elif source_id == 12:
            print("AddOp删除操作！")
            del_button = DelOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            del_button.Show()
            self.Close(True)
        elif source_id == 13:
            self.Close(True)

    def AddAffirm(self, event):
        # 连接login_users数据库
        op = Sql_operation("databases")
        # 向stu_information表添加学生信息
        stu_name = self.stu_name.GetValue()
        print('stu_name',stu_name)  #客户号
        stu_gender = self.stu_gender.GetValue()
        print('stu_gender',stu_gender)
        stu_age = self.stu_age.GetValue()
        print('stu_age',stu_age) #客户名
        stu_cid = self.stu_cid.GetValue()
        print('stu_cid',stu_cid) #地址
        stu_classid = self.stu_classid.GetValue()
        print('stu_classid',stu_classid) #联系方式
        stu_phone = self.stu_phone.GetValue()
        print('stu_phone',stu_phone)
        np = op.Insert(stu_name, stu_gender, stu_age, stu_cid, stu_classid, stu_phone, info=info)


# 继承InquireOp类，实现初始化操作界面
#删除界面
class DelOp(InquireOp):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(DelOp, self).__init__(*args, **kw)
        # 创建删除学员信息输入框、删除按钮
        self.del_id = wx.TextCtrl(self.pnl, pos=(407, 78), size=(210, 25))
        self.del_affirm = wx.Button(self.pnl, label="删除", pos=(625, 78), size=(80, 25))
        # 为删除按钮组件绑定事件处理
        self.del_affirm.Bind(wx.EVT_BUTTON, self.DelAffirm)
        #################################################################################
        # 创建静态框
        sb_del = wx.StaticBox(self.pnl, label="请选择需要删除的id")
        # 创建水平方向box布局管理器
        hsbox_del = wx.StaticBoxSizer(sb_del, wx.HORIZONTAL)
        # 添加到hsbox_name布局管理器
        hsbox_del.Add(self.del_id, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(hsbox_del, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(self.del_affirm, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)

    def ClickButton(self, event):
        source_id = event.GetId()
        if source_id == 10:
            print("DelOp查询操作！")
            inquire_button = InquireOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            inquire_button.Show()
            self.Close(True)
        elif source_id == 11:
            print("DelOp添加操作！")
            add_button = AddOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
            add_button.Show()
            self.Close(True)
        elif source_id == 12:
            pass
        elif source_id == 13:
            self.Close(True)

    def DelAffirm(self, event):
        # 连接login_users数据库
        op = Sql_operation("databases")
        # 向stu_information表添加学生信息
        del_id = self.del_id.GetValue()
        print(del_id)
        np = op.Del(int(del_id),info)
        del_button = DelOp(info, title=u"电力公司收费管理系统管理系统", size=(1024, 668))
        del_button.Show()
        self.Close(True)