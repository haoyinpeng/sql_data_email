# -*- encoding:utf-8 -*-

from process_data import Data_Process 
from send_email import SendEmail_excel
from write_excels import WriteExcel 
import sqls
import sys 
import config


def get_w_resources(receivers):
    d = Data_Process(config.DB_USER,config.DB_PASSWD)
    #d.set_test_infos()
    d.set_pro_infos()
    results = d.get_datas(sqls.W_RESOURCE,sqls.W_PARAMS)
    w = WriteExcel()
    w.set_infos('','w_resources',sqls.W_TITLE)
    excel_name = w.write_excel(results)
    se = SendEmail_excel(config.EMAIL_USER,config.EMAIL_PASSWD)

    #account_passwd
    #mail_passwd = sys.argv[1]
    #print(mail_passwd)
    #发送人
    sender = 'yinpeng_hao@tianma.cn'

    #接收
    #receivers = ['xuge_ning@tianma.cn']
    #receivers = ['haoyinpeng@live.cn']
    #sender,receivers,excel_path,excel_name,message_subject,message_text
    se.set_infos(sender,receivers,excel_name,excel_name,'委外资源信息','请查收附件...')
    se.exce_send_email()



if __name__ == '__main__':
    print(sys.argv[1])
    if sys.argv[1] == '1':
        #get_w_resources(sys.argv[2],sys.argv[3],sys.argv[4])
        get_w_resources(config.RECEIVERS)
    elif sys.argv[1] == '2':
        pass
    else:
        pass