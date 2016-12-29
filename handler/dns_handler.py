#!/usr/bin/python
#-*- coding:utf8 -*-
from application.main import *

class DnsDomainHandler(BaseHandler):
    @Auth
    def get(self):
        #print self.get_login_url()
        #print self.current_user
        #print self.user_info()
        domains = self.db.query("select * from t_zones")
        self.render2("domain.html",domain="active",domains=domains)

    @Auth
    def post(self):
        domain = self.get_argument("domain")
        comment = self.get_argument("comment")
        fun = self.get_argument("fun","add")
        if fun == "add":
            if_domain = self.db.get("select id,zone from t_zones where zone = %s",domain)
            if if_domain:
                self.write("2")
                return
            self.db.execute("insert into t_zones (zone,create_time,comment) values (%s,%s,%s)",domain,self.get_time(),comment)
            self.write("1")
        elif fun == "edit":
            id_  = self.get_argument("id")
            self.db.execute("update t_zones set zone = %s, comment = %s where id = %s",domain,comment,id_)
            self.write("1")

class DnsRecordHandler(BaseHandler):
    @Auth
    def get(self):
        did = self.get_argument("did",0)
        domains = self.db.query("select id,zone from t_zones where status = 'yes'")
        cur_domain = self.db.get("select * from t_zones where id = %s",did)
        records = self.db.query("select * from t_records where did = %s",did)
        self.render2("record.html",record="active",domains=domains,did=int(did),records=records,cur_domain=cur_domain)

    @Auth
    def post(self):
        did = self.get_argument("did")
        record = self.get_argument("record")
        type = self.get_argument("type")
        value = self.get_argument("value")
        priority = self.get_argument("priority")
        comment = self.get_argument("comment")
        fun = self.get_argument("fun","add")
        if type == "MX":
            priority = int(priority)
        else:
            priority = None
        if fun == "add":
            zone = self.db.get("select zone from t_zones where id = %s",did)['zone']
            self.db.execute("insert into t_records (did,host,zone,type,data,mx_priority,comment,create_time) values (%s,%s,%s,%s,%s,%s,%s,%s)",did,record,zone,type,value,priority,comment,self.get_time())
            self.write("1")
        elif fun == "edit":
            id = self.get_argument("id")
            self.db.execute("update t_records set host = %s, type = %s, data = %s, mx_priority = %s, comment = %s where id = %s",record,type,value,priority,comment,id)
            self.write("1")
