#!/usr/bin/python
#-*- coding:utf8 -*-
from application.main import *

class UsersHandler(BaseHandler):
    def get(self):
        users = self.db.query("select * from t_users")
        self.render2("users.html",users=users,users_admin="active")

    def post(self):
        username = self.get_argument("username",None)
        name = self.get_argument("name",None)
        email = self.get_argument("email",None)
        mobile = self.get_argument("mobile",None)
        password = self.get_argument("password",None)
        comment = self.get_argument("comment",None)
        id = self.get_argument("id",None)
        fun = self.get_argument("fun")
        if fun == "add":
            check_user = self.db.get("select id,username,name from t_users where username = %s",username)
            if check_user:
                self.write("2")
                return
            self.db.execute("insert into t_users (username,name,email,mobile,password,comment,cdate) values (%s,%s,%s,%s,md5(%s),%s,CURRENT_TIMESTAMP)",username,name,email,mobile,password,comment)
            self.write("1")
            return
        elif fun == "edit":
            self.db.execute("update t_users set name=%s,email=%s,mobile=%s,comment=%s where id=%s",name,email,mobile,comment,id)
            self.write("1")
        elif fun == "pass":
            self.db.execute("update t_users set password=md5(%s) where id=%s",password,id)
            self.write("1")

class LoginLogsHandler(BaseHandler):
    def get(self):
        logs = self.db.query("select * from t_login_logs")
        self.render2("users_logs.html",logs=logs,users_logs="active")
