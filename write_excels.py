

import openpyxl
import process_data

def write_excel():
	#create a workbook
	wb = openpyxl.Workbook()
	#create a sheet
	sheet1 = wb.create_sheet(index=0,title='outresource')
	results_all = process_data.get_test_datas('','')
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

