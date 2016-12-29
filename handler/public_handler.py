#!/usr/bin/python
#-*- coding:utf8 -*-
from application.main import *
import os

class PublicAPIHandler(BaseHandler):

    @Auth
    def get(self):
        module = self.get_argument("module")
        fun = self.get_argument("fun")
        value = self.get_argument("value",None)
        id = self.get_argument("id",None)
        redirect_id = self.get_argument("did",None)
        if module == "record":
            if fun == "ch_status":
                self.db.execute("update t_records set status = %s where id = %s",value,id)
                self.redirect("/dns/record?did="+redirect_id)
            elif fun == "del":
                self.db.execute("delete from t_records where id = %s",id)
                self.redirect("/dns/record?did="+redirect_id)
        elif module == "domain":
            if fun == "ch_status":
                self.db.execute("update t_zones set status = %s where id = %s",value,id)
                self.redirect("/dns/domain")
            elif fun == "del":
                # 获取该域名的配置文件
                domain = self.db.get("select * from t_zones where id = %s",id)
                # 同时删除域名的所有记录
                self.db.execute("delete from t_records where did = %s",id)
                # 删除域名
                self.db.execute("delete from t_zones where id = %s",id)
                self.redirect("/dns/domain")
        elif module == "users":
            if fun == "ch_status":
                self.db.execute("update t_users set status = %s where id = %s",value,id)
                self.redirect("/users")
            elif fun == "del":
                self.db.execute("delete from t_users where id = %s",id)
                self.redirect("/users")
        elif module == "login_logs":
            if fun == "clear":
                try:
                    self.db.execute("truncate table t_login_logs")
                    self.write("1")
                    return
                except:
                    self.write("2")


