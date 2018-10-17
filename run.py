# -*- encoding:utf-8 -*-

from process_data import Data_Process 
from send_email import SendEmail_excel
from write_excels import WriteExcel 
import sqls


def main():
    d = Data_Process('','')
    d.set_test_infos()
    results = d.get_datas(sqls.W_RESOURCE,sqls.W_PARAMS)
    w = WriteExcel()
    excel_name = w.write_excel(results)
    se = SendEmail_excel('','')

    #account_passwd
    #mail_passwd = sys.argv[1]
    #print(mail_passwd)
    #发送人
    sender = 'yinpeng_hao@tianma.cn'

    #接收
    #receivers = ['xuge_ning@tianma.cn']
    receivers = ['haoyinpeng@live.cn']
    #sender,receivers,excel_path,excel_name,message_subject,message_text
    se.set_infos(sender,receivers,'',excel_name,'ceshi','send email...')
    se.exce_send_email()



if __name__ == '__main__':
    main()