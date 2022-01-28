
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

# https://support.microsoft.com/en-us/topic/how-to-send-an-email-with-an-embedded-image-879d3e13-6bc4-6c61-417a-b7419d304d52

def main():

    parser = argparse.ArgumentParser(description='Mail')
    parser.add_argument('--subject', dest='subject', action='store', required=True)
    parser.add_argument('--to', dest='to', action='store', required=True)
    args = parser.parse_args()

    smtp_dict = {}
    try:
        with open("testbestanden/smtp.json", encoding='iso-8859-1') as fp1:
            smtp_dict = json.loads(fp1.read())
    except FileNotFoundError:
        print('testbestanden/smtp.json is niet aanwezig')
        sys.exit(1)
    attach_dict = {}
    try:
        with open("testbestanden/attach.json", encoding='iso-8859-1') as fp1:
            attach_dict = json.loads(fp1.read())
    except FileNotFoundError:
        pass

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = args.subject
    msgRoot['From'] = smtp_dict['from']
    msgRoot['To'] = args.to

    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    #msgText = MIMEText('This is the alternative plain text message.')
    #msgAlternative.attach(msgText)
    msgText = MIMEText('<img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)
    fp = open('testbestanden/Knipsel.PNG', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        server = smtplib.SMTP(smtp_dict['server'], smtp_dict['port'])
        server.starttls()
        server.login(smtp_dict['from'], smtp_dict['pwd'])
        server.send_message(msgRoot)
        server.quit()
    except:
        print('fout met verzenden')
        sys.exit(1)

if __name__ == '__main__':
    main()
