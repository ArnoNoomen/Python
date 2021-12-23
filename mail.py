
import sys
import os
import argparse
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def main():

    parser = argparse.ArgumentParser(description='Mail')
    parser.add_argument('--subject', dest='subject', action='store', required=True)
    parser.add_argument('--from', dest='from1', action='store', required=True)
    parser.add_argument('--to', dest='to', action='store', required=True)
    parser.add_argument('--smtp', dest='smtp', action='store', required=True)
    args = parser.parse_args()
    
    msg = MIMEMultipart()
    msg['Subject'] = args.subject
    msg['From'] = args.from1
    msg['To'] = args.to
    body = "Salut!"
    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("example.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='example1.txt')
    msg.attach(part)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("example2.txt", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='example2.txt')
    msg.attach(part)
    
    print(msg)
    #server = smtplib.SMTP(args.smtp, 587)
    #server.starttls()
    #server.login(args.from1, args.pwd)
    #server.send_message(msg)
    #server.quit()

if __name__ == '__main__':
    main()
