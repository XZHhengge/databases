# -*- coding: utf-8 -*-
import pymysql


# 创建数据库操作类
class Sql_operation(object):
    '''
    数据库操作
    '''

    # 用构造函数实现数据库连接，并引入mydb参数，实现调用不同的数据库
    def __init__(self, mydb):
        # 实例变量
        self.mydb = mydb
        # 打开数据库连接
        self.db = pymysql.connect(host="localhost", user="root", password="159874xzh", db=self.mydb, charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()

    # 定义查看数据表信息函数，并引入table_field、table_name参数，实现查看不同数据表的建表语句
    def FindAll(self, table_name):
        # 实例变量
        self.table_name = table_name
        # 定义SQL语句
        sql = "select * from %s" % (self.table_name)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)

    # 定义添加表数据函数
    def Insert(self, stu_name, stu_gender, stu_age, stu_cid, stu_classid, stu_phone, info):
        # 实例变量
        self.stu_name = stu_name  #1
        self.stu_age = stu_age      #2
        self.stu_cid = stu_cid     #3
        self.stu_classid = stu_classid #4

        self.stu_gender = stu_gender #5
        self.stu_phone = stu_phone
        # 定义SQL语句
        if info[0] == '客户':
            sql = "insert into 客户({},{},{},{}) " \
                  "values('%s','%s','%s','%s')".format('客户表客户号',info[2], info[3], info[4]) \
                  % ( self.stu_name, self.stu_age, self.stu_cid, self.stu_classid)
        elif info[0] == '员工':
            sql = "insert into 员工({},{},{},{}) " \
                  "values('%s','%s','%s','%s')".format('员工表员工号', info[2],info[3], info[4]) \
                  % ( self.stu_name, self.stu_age, self.stu_cid, self.stu_classid)
        elif info[0] == '收费登记':
            cost = float(stu_classid) - float(stu_gender)
            cost = str(cost)
            sql = "insert into 收费登记({},{},{},{},{},{}) " \
                    "values('%s','%s','%s','%s','%s','%s')".format('客户表客户号', info[2], info[3], info[4], info[5], '结余费用') \
                  % (stu_name, self.stu_age, self.stu_cid, self.stu_classid, self.stu_gender, cost)
        elif info[0] == '用电信息':
            sql = "insert into 用电信息({},{},{},{},{}) " \
                    "values('%s','%s','%s','%s','%s')".format('客户表客户号', info[2], info[3], '客户_客户号', info[4]) \
            % (stu_name,  self.stu_age, self.stu_cid, self.stu_classid, stu_gender)
        elif info[0] == '用电类型':
            sql = "insert into 用电类型({},{},{},{}) " \
                    "values('%s','%s','%s','%s')".format('客户表客户号', info[2], info[3], info[4]) \
            % (stu_name,  self.stu_age, self.stu_cid, self.stu_classid)
        elif info[0] == '费用管理 ':
            sql = "insert into 费用管理({},{},{},{},{})values('%s','%s','%s','%s','%s')"\
                      .format('客户表客户号', info[2], info[3], info[4], '收费标志') \
                  % (stu_name, self.stu_name, self.stu_age, self.stu_cid, '未收费')
        elif stu_name == None:
            print('输入为空')

        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    def updata_table(self, info, *args):
        print(info)
        print(args)
        list1 = []
        list2 = ['用电信息', '费用管理',]
        if info[0] == '客户':
            sql = "update {} set {}={}, {}={}, {}={} where {} = {}"\
                .format(info[0], info[2], args[1],info[3], args[2], info[4], args[3], '客户表客户号', args[0])
            print(sql)
        elif info[0] == '员工':
            sql = "update {} set {}='{}', {}='{}', {}={} where {} = {}" \
                .format(info[0], info[2], args[1],
                        info[3], args[2], info[4], args[3], '员工表员工号', args[0])
            print(sql)
        elif info[0] == '用电类型':
            sql = "update {} set {}={}, {}={}, {}={} where {} = '{}'" \
                .format(info[0], info[2], args[1],
                        info[3], args[2], info[4], args[3], '客户表客户号', args[0])
            print(sql)
        elif info[0] in list2:
            sql = "update {} set {}='{}', {}='{}', {}='{}', {}='{}' where {} = '{}'" \
                .format(info[0], info[2], args[1],
                        info[3], args[2], info[4], args[3], info[5], args[4], '客户表客户号', args[0])
            print(sql)
        # elif info[0] in '用电信息':
        #     sql = "update {} set {}='{}', {}='{}', {}='{}', {}='{}' where {} = '{}'" \
        #         .format(info[0], info[2], args[1],
        #                 info[3], args[2], info[4], args[3], info[5], args[4], '客户表客户号', args[0])
        #     print(sql)
        elif info[0] in '收费登记':
            cost = float(args[3]) - float(args[4])
            cost = str(cost)
            sql = "update {} set {}='{}', {}='{}', {}='{}', {}='{}', {}='{}' where {} = '{}'" \
                .format(info[0], info[2], args[1],
                        info[3], args[2], info[4], args[3], info[5], args[4], '结余费用', cost, '客户表客户号', args[0])
            print(sql)

        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 定义删除表数据函数
    def Del(self, stu_id, *args):
        # 实例变量
        table = args[0][0]
        table_id = args[0][1]
        self.stu_id = stu_id
        # 定义SQL语句
        sql = "delete from {} where {}={}".format(table, table_id, stu_id)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 用析构函数实现数据库关闭
    def __del__(self):
        # 关闭数据库连接
        self.db.close()