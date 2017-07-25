import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
mail_host="smtp.126.com"
mail_user="xxxxx@126.com"
mail_pass="xxxxx"
  
sender = mail_user
to_account = "xxxxx@qq.com"
receivers = [to_account]
 
message = MIMEText('hello', 'plain', 'utf-8')
message['From'] = sender
message['To'] = to_account
 
subject = 'A good Notice'
message['Subject'] = Header(subject, 'utf-8')

print(message);
print("=================================");
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "success"
    smtpObj.quit()
except smtplib.SMTPException, e:
    print "Error: can not send:" , e