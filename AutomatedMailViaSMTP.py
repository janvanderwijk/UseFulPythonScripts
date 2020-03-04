import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr=' '
to_addr=['ToEmail@email.com','ToEmail2@email.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='just to check'

body='hello world'

msg.attach(MIMEText(body,'plain'))

email='FromEmail@email.com'
password='passwordofFromEmailaccount'

mail=smtplib.SMTP('smtpserverfromemailserver',<portnumberofemailserver>)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()