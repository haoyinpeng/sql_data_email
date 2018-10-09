# -*- coding:utf-8 -*-

import sys
import cx_Oracle as oracle
import sqls
import openpyxl 
import datetime


#print(sys.argv[0])
#print(sys.argv[1])
SQL_STR = sqls.W_RESOURCE
SQL_PARAMS = sqls.PARAMS


if sys.argv[2]=='W':
	SQL_STR = sqls.W_RESOURCE
	SQL_PARAMS = sqls.W_PARAMS
elif sys.argv[2]=='..':
	pass



def get_pro_datas(user,passwd):
	#tns
	tns = oracle.makedsn('172.18.2.52',1521,'perp1')
	#connection
	db = oracle.connect(user,passwd,tns,encoding='utf-8',nencoding='utf-8')
	#cursor
	cursor = db.cursor()
	print('cursor...')

	if sys.argv[0] == 'outresource':
		#params = {'resource_code':str(sys.argv[1])}
		print('sys.argv[0]' + sys.argv[0])
		print('sys.argv[1]' + sys.argv[1])

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

def write_excel():
	#create a workbook
	wb = openpyxl.Workbook()
	#create a sheet
	sheet1 = wb.create_sheet(index=0,title='outresource')
	results_all = get_test_datas('','')
	#results_all = get_pro_datas()
	print('add title...')
	sheet1.append(sqls.W_TITLE)
	print('add lines...')
	for i in results_all:
		sheet1.append(i)

    #sheet1.add_table()
	print('save excel...')
	name_str = 'w_resouece_'+str(datetime.datetime.now().strftime('%Y%m%d%H%I%S'))+'.xlsx'
	wb.save(name_str)
	return name_str


if __name__ == '__main__':
	write_excel()
