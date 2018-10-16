# -*- coding:utf-8 -*-

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#from write_excels import WriteExcel
 

#邮件服务器地
#mail_host = "shmail.tianma.cn"

#account_name
#mail_user = "yinpeng_hao" 

#account_passwd
#mail_passwd = sys.argv[1]
#print(mail_passwd)
#发送人
#sender = 'yinpeng_hao@tianma.cn'

#接收
#receivers = ['xuge_ning@tianma.cn']
#receivers = ['haoyinpeng@live.cn']

class SendEmail_excel():
	def __init__(self,mail_user,mail_passwd):
		self.mail_host = "shmail.tianma.cn"
		self.mail_user = mail_user
		self.mail_passwd = mail_passwd 

	
	def set_infos(self,sender,receivers,excel_path,excel_name,message_subject,message_text):
		self.sender = sender
		self.receivers = receivers
		self.excel_path = excel_path
		self.excel_name = excel_name
		self.message_subject = message_subject
		self.message_text = message_text

	def read_excel(self):
		att1 = MIMEText(open(self.excel_path,'rb').read(), 'base64', 'utf-8')
		att1['Content-Type'] = 'application/octet-stream'
		att1['Content-Disposition'] = 'attachment; filename= %s' ,str(self.excel_name)
		return att1

	def ready_content_of_mail(self):
		#邮件对象实例 可以添加附件 富文本的对象实例
		message = MIMEMultipart('alternative')
		#email theme
		#subject = '厦门委外资源成本信息 测试 请忽略'
		message['Subject'] = Header(self.message_subject,'utf-8').encode()
		#邮件文本内容
		message.attach(MIMEText(self.message_text,'plain','utf-8'))

		print('read excel...')
		message.attach(self.read_excel())
		return message
    
	def exce_send_email(self):
		try:
			smtobj = smtplib.SMTP()
			print('smtplib connect...')
			smtobj.connect(self.mail_host,25)
			smtobj.ehlo() #替换starttls
			#smtobj.starttls()#开启加密模式
			#smtobj.set_debuglevel(1)#开启日志
			print('login...')
			smtobj.login(self.mail_user,self.mail_passwd)
			smtobj.sendmail(self.sender,self.receivers,self.ready_content_of_mail().as_string())
			print('email sended successfully')
			smtobj.quit()
		except smtplib.SMTPException:
			print('email sended fail')


if __name__ == '__main__':
	pass