# -*- coding:utf-8 -*-

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import write_excels
 

#邮件服务器地
mail_host = "shmail.tianma.cn"

#account_name
mail_user = "yinpeng_hao" 

#account_passwd
mail_passwd = sys.argv[1]
print(mail_passwd)
#发送人
sender = 'yinpeng_hao@tianma.cn'

#接收
receivers = ['xuge_ning@tianma.cn']
#receivers = ['haoyinpeng@live.cn']

#excel file
def get_file_excel():
    return write_excels.write_excel('B159212',sys.argv[1])

def ready_content_of_mail():
	print('ready message...')
	#邮件对象实例 可以添加附件 富文本的对象实例
	message = MIMEMultipart('alternative')
    #email theme
	subject = '厦门委外资源成本信息 测试 请忽略'
    
	message['Subject'] = Header(subject,'utf-8').encode()
    
    #邮件文本内容
	message.attach(MIMEText('测试邮件 请忽略','plain','utf-8'))

	print('read excel...')
	att1 = MIMEText(open(get_file_excel(),'rb').read(), 'base64', 'utf-8')
	att1['Content-Type'] = 'application/octet-stream'
	att1['Content-Disposition'] = 'attachment; filename="outresouece.xlsx"'
	message.attach(att1)
	return message 

def send_email():
	try:
		print('smtplib...')
		smtobj = smtplib.SMTP()
		smtobj.connect(mail_host,25)
		smtobj.ehlo()
		#smtobj.starttls()#开启加密模式
		#smtobj.set_debuglevel(1)#开启日志
		print('login...')
		smtobj.login(mail_user,mail_passwd)
		smtobj.sendmail(sender,receivers,ready_content_of_mail().as_string())
		print('email sended successfully')
		smtobj.quit()
	except smtplib.SMTPException:
		print('email sended fail')


if __name__ == '__main__':
	send_email()