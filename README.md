### 关于bindweb
bindweb基于开源项目DNSmasqWeb进行二次开发, bindweb用于管理bind的dns记录, 在这里要感谢DNSmasqWeb的作者luxiaok

### 安装
```
yum -y install python-setuptools python-devel
easy_install pip
pip install tornado jinja2 MySQL-python torndb
```

### 创建用户并授权
```
CREATE DATABASE dnsdb;
CREATE USER 'dns'@'localhost' IDENTIFIED BY 'dns4bind';
GRANT SELECT, INSERT, UPDATE, DELETE, DROP ON `dnsdb`.* TO 'dns'@'localhost';
```

### 导入数据
```
mysql dnsdb < scripts/mysql.sql
```

### bind相关配置
```
view  ANY  {
        match-clients {any;};
        dlz "Mysql zone" {
        database "mysql
        {host=localhost dbname=dnsdb port=3306 user=dns pass=dns4bind ssl=false}
        {select zone from t_zones where zone='$zone$' and status='yes' limit 1}
        {select ttl, type, mx_priority, case when lower(type)='txt' then concat('\"', data, '\"') else data end from t_records where zone = '$zone$' and host = '$record$' and not (type = 'SOA' or type = 'NS') and status='yes' }
        {select ttl, type, mx_priority, data from t_records where zone = '$zone$' and (type = 'SOA' or type='NS')}
        {select ttl, type, host, mx_priority, data, resp_person, serial, refresh, retry, expire, minimum from t_records where zone = '$zone$' and not (type = 'SOA' or type = 'NS')}
        {select zone from xfr_table where zone = '$zone$' and client = '$client$'}";
        };
};
```
