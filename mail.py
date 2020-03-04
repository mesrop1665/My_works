import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Grab'
msg['From'] =  'levon.hakobyan.2018@gmail.com'
msg['To'] = 'mesrop.araqelyan.04@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('mesrop.araqelyan.04@gmail.com','mospos321')
sub = input('subject')
body = input('body: ')
server.send_message(msg)