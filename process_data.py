# -*- coding:utf-8 -*-

import sys
import cx_Oracle as oracle
import sqls
import openpyxl 
import datetime


#print(sys.argv[0])
#print(sys.argv[1])
SQL_STR = sqls.W_RESOURCE
SQL_PARAMS = sqls.W_PARAMS

def get_pro_datas(user,passwd):
	#tns
	tns = oracle.makedsn('172.18.2.52',1521,'perp1')
	#connection
	db = oracle.connect(user,passwd,tns,encoding='utf-8',nencoding='utf-8')
	#cursor
	cursor = db.cursor()
	print('cursor...')
	#execute sql
	print('cursor execute...')
	cursor.execute(SQL_STR,SQL_PARAMS)
	#fetch results
	result_all = cursor.fetchall()
	#close cursor
	cursor.close()
	#close connection
	db.close()
	print('db.close()...')
	return result_all

def get_test_datas(user,passwd):
	#tns
	tns = oracle.makedsn('172.18.2.152',1531,'terp1')
	#connection
	db = oracle.connect(user,passwd,tns,encoding='utf-8',nencoding='utf-8')
	#cursor
	cursor = db.cursor()
	print('cursor...')

	if sys.argv[1] == 'outresource':
		#params = {'resource_code':str(sys.argv[1])}
		print('sys.argv[1]' + sys.argv[1])
		print('sys.argv[2]' + sys.argv[2])

	#execute sql
	print('cursor execute...')
	cursor.execute(SQL_STR,SQL_PARAMS)
	#fetch results
	result_all = cursor.fetchall()
	#close cursor
	cursor.close()
	#close connection
	db.close()
	print('db.close()...')
	return result_all

class Data_Process():
    def __init__(self,user,passwd):
    	self.user = user 
    	self.passwd = passwd
	
    def set_pro_infos(self):
    	self.db_host = '172.18.2.152'
    	self.db_port = 1531
    	self.db_name = 'terp1'

	#设置测试环境连接信息
    def set_test_infos(self):
    	self.db_host = '172.18.2.152'
    	self.db_port = 1531
    	self.db_name = 'terp1'

    def get_pro_datas(self):
    	pass


if __name__ == '__main__':
	get_test_datas('','')

