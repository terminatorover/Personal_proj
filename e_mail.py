#usr/bin/python

import smtplib

recpient = 'recpient.mail.com'
sender = 'sender.mail.com'


msg = """I just wanted to say hello"""

username = str('senders username info')
password  = str('senders pass')

try:


    server = smtplib.SMTP('smtp.gmail.com',587)
    #establish connection 
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)

#send mail
    server.sendmail(sender,recpient,msg)   
    print "message sent"
except:
       server.quit()
       print "message not sent"

 


