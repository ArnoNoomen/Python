import sys
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

    subject = 'test4'
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
    attach_dict = {}
    try:
        with open("testbestanden/attach.json", encoding='iso-8859-1') as fp1:
            attach_dict = json.loads(fp1.read())
    except FileNotFoundError:
        pass

    for email in emails:

        print(email['email'])
        msg = MIMEMultipart('related')
        msg['Subject'] = subject
        msg['From'] = smtp_dict['from']
        msg['To'] = email['email']

        #msg.attach(MIMEText(body, 'plain'))
        msgtext = MIMEText('<img src="cid:image1"><br><img src="cid:image2">', 'html')
        msg.attach(msgtext)

        for rij in attach_dict:

            part = MIMEBase('application', rij['application'])
            part.set_payload(open(rij['filename'], "rb").read())
            encoders.encode_base64(part)
            if rij['embedded'].upper() == 'J':
                part.add_header('Content-ID', f"{rij['attachname']}")
            else:
                part.add_header('Content-Disposition', 'attachment', filename=rij['attachname'])
            msg.attach(part)

        try:
            server = smtplib.SMTP(smtp_dict['server'], smtp_dict['port'])
            server.starttls()
            server.login(smtp_dict['from'], smtp_dict['pwd'])
            server.send_message(msg)
            server.quit()
        except:
            print('fout met verzenden')
            sys.exit(1)

if __name__ == '__main__':
    main()
