import sys
import base64
import os
import argparse
import smtplib
import json
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

def main():

    subject = 'test5'
    emails = {}
    try:
        with open("testbestanden/emails.json", encoding='iso-8859-1') as fp1:
            emails = json.loads(fp1.read())
    except FileNotFoundError:
        print('emails.json is niet aanwezig')
        sys.exit(1)

    smtp_dict = {}
    try:
        with open("testbestanden/smtp.json", encoding='iso-8859-1') as fp1:
            smtp_dict = json.loads(fp1.read())
    except FileNotFoundError:
        print('smtp.json is niet aanwezig')
        sys.exit(1)
   
    for email in emails:

        print(email['to'])
       
        msgroot = MIMEMultipart('related')
        msgroot['Subject'] = subject
        msgroot['From'] = smtp_dict['from']
        msgroot['To'] = email['to']
      
        msgroot.preamble = 'This is a multi-part message in MIME format.'
        msgalternative = MIMEMultipart('alternative')
        msgroot.attach(msgalternative)
        msgtext = MIMEText('<img src="cid:image1">', 'html')
        msgalternative.attach(msgtext)
        fp1 = open('testbestanden/Knipsel.PNG', 'rb')
        msgimage = MIMEImage(fp1.read())
        fp1.close()
        msgimage.add_header('Content-ID', '<image1>')
        msgroot.attach(msgimage)

    try:
        # print(smtp_dict['server'])
        # print( smtp_dict['pwd'])
        # print(smtp_dict['port'])
        # print(smtp_dict['from'])

        server = smtplib.SMTP(smtp_dict['server'], smtp_dict['port'])
        server.starttls()
        server.login(smtp_dict['from'], smtp_dict['pwd'])
        server.send_message(msgroot)
        server.quit()
    except:
        print('fout met verzenden')
        sys.exit(1)


if __name__ == '__main__':
    main()