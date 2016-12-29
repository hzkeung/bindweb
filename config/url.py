#!/usr/bin/python
#-*- coding:utf8 -*-

from handler import *

HandlersURL = [
    (r"/(|login)/?", login_handler.LoginHandler),
    (r"/logout", login_handler.LogoutHandler),
    (r"/dashboard/?", index_handler.IndexHandler),
    (r"/dns/domain", dns_handler.DnsDomainHandler),
    (r"/dns/record", dns_handler.DnsRecordHandler),
    (r"/public/api", public_handler.PublicAPIHandler),
    (r"/users", users_handler.UsersHandler),
    (r"/users/logs", users_handler.LoginLogsHandler),
]
