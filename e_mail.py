#usr/bin/python

import smtplib

recpient = 'recpient.mail.com'
sender = 'sender.mail.com'


msg = """I just wanted to say hello"""

username = str('senders username info')
password  = str('senders pass')

#try:


server = smtplib.SMTP('smtp.gmail.com',587)
#SMTP.verify(username)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
#    server.set_debuglevel(1)
#message = msg.as_string()
server.sendmail(sender,recpient,msg)   

server.quit()

 


