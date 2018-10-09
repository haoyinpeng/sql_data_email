# -*- coding:utf-8 -*-

import sys
import cx_Oracle as oracle
import sqls
import openpyxl 
import datetime


#print(sys.argv[0])
#print(sys.argv[1])

def get_pro_datas():
	#tns
	tns = oracle.makedsn('172.18.2.52',1521,'perp1')
	#connection
	db = oracle.connect('B159212','flask&justDo-1',tns,encoding='utf-8',nencoding='utf-8')
	#cursor
	cursor = db.cursor()
	print('cursor...')

	if sys.argv[0] == 'outresource':
		#params = {'resource_code':str(sys.argv[1])}
		print('sys.argv[0]' + sys.argv[0])
		print('sys.argv[1]' + sys.argv[1])

	#execute sql
	sql_str = sqls.W_RESOURCE
	params = {'resource_code':'W%'}
	print('cursor execute...')
	cursor.execute(sql_str,params)
	#fetch results
	result_all = cursor.fetchall()
	#close cursor
	cursor.close()
	#close connection
	db.close()
	print('db.close()...')
	return result_all

def get_test_datas():
	#tns
	tns = oracle.makedsn('172.18.2.152',1531,'terp1')
	#connection
	db = oracle.connect('apps','netra0apps',tns,encoding='utf-8',nencoding='utf-8')
	#cursor
	cursor = db.cursor()
	print('cursor...')

	if sys.argv[0] == 'outresource':
		#params = {'resource_code':str(sys.argv[1])}
		print('sys.argv[0]' + sys.argv[0])
		print('sys.argv[1]' + sys.argv[1])

	#execute sql
	sql_str = sqls.W_RESOURCE
	params = {'resource_code':'W%'}
	print('cursor execute...')
	cursor.execute(sql_str,params)
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
	results_all = get_test_datas()
	#results_all = get_pro_datas()
	print('add title...')
	sheet1.append(['库存组织名称','库存组织ID','委外资源编码','描述','委外资源费率','失效日期'])
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
