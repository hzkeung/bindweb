DROP TABLE IF EXISTS `t_login_logs`;
CREATE TABLE `t_login_logs` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `uid` int(3) NOT NULL COMMENT '用户ID',
  `username` varchar(30) DEFAULT NULL COMMENT '登录用户名',
  `login_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '登录时间',
  `login_host` varchar(15) DEFAULT NULL COMMENT '登录IP',
  `login_location` varchar(20) DEFAULT NULL COMMENT '登录地区',
  `login_status` int(1) NOT NULL DEFAULT '0' COMMENT '0:成功，1:失败，2:用户被禁用，3:用户名错误，4:密码错误，5:异常，6:未知状态',
  `user_agent` varchar(200) DEFAULT NULL COMMENT '用户代理',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `t_records`;
CREATE TABLE `t_records` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增列',
  `did` int(11) NOT NULL COMMENT '域名ID',
  `zone` varchar(255) NOT NULL COMMENT ' 域名',
  `host` varchar(255) NOT NULL DEFAULT '@' COMMENT '主机记录',
  `type` enum('MX','CNAME','NS','SOA','A','PTR') NOT NULL DEFAULT 'A' COMMENT '记录类型',
  `data` varchar(255) DEFAULT NULL COMMENT '记录值',
  `ttl` int(11) NOT NULL DEFAULT '800' COMMENT '缓存时间',
  `mx_priority` int(11) DEFAULT NULL COMMENT 'MX记录.  先级',
  `refresh` int(11) NOT NULL DEFAULT '3600' COMMENT '辅助域名服务器多长时间更新数据库',
  `retry` int(11) NOT NULL DEFAULT '3600' COMMENT '若辅助域名服.  器更新数据失败，多长时间再试',
  `expire` int(11) NOT NULL DEFAULT '86400' COMMENT '若辅助域名服务器无法从主服务器上更新数据，原有的数据何时失效',
  `minimum` int(11) NOT NULL DEFAULT '3600' COMMENT '设置被缓存的否定回答的存活时间',
  `serial` bigint(20) NOT NULL DEFAULT '2008082700' COMMENT '本区配置数据的序列号，用于从.  务器判断何时获取最新的区数据',
  `resp_person` varchar(64) NOT NULL DEFAULT 'root.domain.com.' COMMENT '区域管理员邮箱',
  `primary_ns` varchar(64) NOT NULL DEFAULT 'ns1.domain.com.' COMMENT '区域主节点机器名',
  `status` varchar(10) NOT NULL DEFAULT 'yes',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `up_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `comment` varchar(200) NOT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `t_users`;
CREATE TABLE `t_users` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `password` varchar(64) NOT NULL,
  `mobile` varchar(15) DEFAULT NULL COMMENT '电话号码',
  `email` varchar(50) DEFAULT NULL COMMENT '电子邮件',
  `cdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mask` varchar(3) NOT NULL DEFAULT '999',
  `is_admin` varchar(3) NOT NULL DEFAULT 'no' COMMENT '是否为管理员',
  `status` varchar(3) NOT NULL DEFAULT 'yes',
  `comment` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `t_users` WRITE;
INSERT INTO `t_users` VALUES (2,'admin','管理员','21232f297a57a5a743894a0e4a801fc3',NULL,NULL,'2014-11-22 16:37:50','2014-11-22 00:37:50','999','yes','yes','系统管理员\n');
UNLOCK TABLES;

DROP TABLE IF EXISTS `t_zones`;
CREATE TABLE `t_zones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zone` varchar(60) NOT NULL COMMENT '域名',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `up_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `comment` varchar(200) NOT NULL COMMENT '备注',
  `status` varchar(3) NOT NULL DEFAULT 'yes' COMMENT '状态',
  PRIMARY KEY (`id`),
  KEY `idx_zone` (`zone`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
