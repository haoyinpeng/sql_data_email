

from openpyxl import Workbook
import process_data
import datetime
import sqls

def write_excel(user,passwd):
	#create a workbook
	wb = Workbook()
	#create a sheet
	sheet1 = wb.create_sheet(index=0,title='outresource')
	results_all = process_data.get_test_datas(user,passwd)
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

class WriteExcel(Workbook):
	def __init__(self,user,passwd,data_kind,data_name,data_title):
		print('__init__')
		self.user = user
		self.passwd = passwd
		self.type = data_kind
		self.data_name = data_name
		self.data_title = data_title

	def write_excel(self):
		pass

