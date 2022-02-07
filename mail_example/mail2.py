
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
# https://code.activestate.com/recipes/473810/

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

    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = args.subject
    msgroot['From'] = smtp_dict['from']
    msgroot['To'] = args.to

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
