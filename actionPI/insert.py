# -*- coding: utf-8 -*-
import pymysql
 
import time
import random
#order: 0->quik 1->voice 1->temp 2->humi
 
def sql_thq():
 
    th_time = time.strftime('%H:%M',time.localtime(time.time()))
    q_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    conn = pymysql.connect(host = 'localhost',  # 远程主机的ip地址， 
                               user = 'root',   # MySQL用户名
                               db = 'myaction',   # database名
                               passwd = 'usbw',   # 数据库密码
                               port = 3306,  #数据库监听端口，默认3306
                               charset = "utf8")  #指定utf8编码的连接
    cursor = conn.cursor()  # 创建一个光标，然后通过光标执行sql语句
    sql = "INSERT INTO `page1_thdata` VALUE('%s','%s', '%s') "%('',int(random.uniform(10,30)),int(random.uniform(10,50)))
    cursor.execute(sql)
    conn.commit() 
    cursor.close()
 
          
temp = [25,26,26,26,25,25,26,27];
hmui = [52,53,53,52,53,54,55,52];
count = 0
while True:
                                                            
    sql_thq()
time.sleep(2)
 
