
import sys
import os
import argparse
import smtplib
import json
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

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

    msg = MIMEMultipart()
    msg['Subject'] = args.subject
    msg['From'] = smtp_dict['from']
    msg['To'] = args.to
    #body = "Salut!"
    #msg.attach(MIMEText(body, 'plain'))

    for rij in attach_dict:
        if rij['toevoegen'].upper() == 'N':
            continue
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(rij['filename'], "rb").read())
        encoders.encode_base64(part)
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
