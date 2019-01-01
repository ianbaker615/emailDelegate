#!/usr/bin/env python3

#send reverb messages via email to proper recipient

import datetime
import smtplib
import clipboard

#handle login and connection
conn = smtplib.SMTP('smtp.gmail.com', 587) # establish connection
conn.ehlo() #start connection
conn.starttls()#encrypt password
conn.login('ian@chicagomusicexchange.com', 'shtrztkpiplihoit')

#handle email sending
date = datetime.datetime.now().strftime("%x")
url = clipboard.paste()
print('Enter recipient name')
recipient = input()
recipient = recipient + '@chicagomusicexchange.com'
conn.sendmail('ian@chicagomusicexchange.com', recipient, f'Subject: rvb {date} - message 4 u\n\n {url}\n\n')

#exit connection
conn.quit()

