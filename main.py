import requests
from email.mime import text
from tkinter.constants import COMMAND
from typing import Text
import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from email.header import decode_header


from requests.api import get 
   
root = tk.Tk()  
root.geometry('640x480')
  
root.title('Email client')
number1 = tk.StringVar(root)  
number2 = tk.StringVar(root)
smtpip = "smtp-mail.outlook.com"
receiver = tk.StringVar(root)
oggetto = tk.StringVar(root)
textmail = tk.StringVar(root)
attach = tk.StringVar(root)
attachfilenames = tk.StringVar(root)
emailprovider = tk.StringVar(root)
htmlsend = tk.StringVar(root)
htmlpagecode = tk.StringVar(root)
downloadcheck = tk.StringVar(root)
mailprovider = tk.StringVar(root).set("outlook")
  
labelNum1 = tk.Label(root, text="Email").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Password").grid(row=2, column=0)  
labelNum3 = tk.Label(root, text="Destinatario").grid(row=3, column=0)  
labelNum4 = tk.Label(root, text="Oggetto").grid(row=4, column=0)  
labelNum5 = tk.Label(root, text="Testo").grid(row=5, column=0)  
labelNum6 = tk.Label(root, text="Allego un file?").grid(row=6, column=0)  
labelNum7 = tk.Label(root, text="Nome del file: ").grid(row=7, column=0)
labelNum8 = tk.Label(root, text="Manda pagina html?").grid(row=8, column=0)
labelNum9 = tk.Label(root, text="URL: ").grid(row=9, column=0)
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, show="*", textvariable=number2).grid(row=2, column=2)
destination = tk.Entry(root, textvariable=receiver).grid(row=3, column=2)
subjectmail = tk.Entry(root, textvariable=oggetto).grid(row=4, column=2)
Testo = tk.Entry(root, textvariable=textmail).grid(row=5, column=2)
checky = tk.Entry(root, textvariable=attach).grid(row=6, column=2)
allegonome = tk.Entry(root, textvariable=attachfilenames).grid(row=7, column=2)
sendhtml = tk.Entry(root, textvariable=htmlsend).grid(row=8, column=2)
htmlpage = tk.Entry(root, textvariable=htmlpagecode).grid(row=9, column=2)

def verify():
    print(tk.StringVar.get(number1))
    print(tk.StringVar.get(number2))

def setsmtp():
    if (mailprovider == "outlook"):
        global smtpip
        print(mailprovider)
        smtpip = "smtp-mail.outlook.com"
        print(smtpip)
    else:
        if (mailprovider == "gmail"):
            print(mailprovider)
            smtpip = "smtp.gmail.com"
            print(smtpip)

def mailgmail():
    global mailprovider
    mailprovider = "gmail"
    setsmtp()

def mailoutlook():
    global mailprovider
    mailprovider = "outlook"
    setsmtp()

gmailbutton = tk.Button(root, text="gmail", command=mailgmail).grid(row=0, column=0)
outlookbutton = tk.Button(root, text="outlook", command=mailoutlook).grid(row=0, column=1)

def servers():
    os.system("notepad servers.bin")

def sendmailloop():
    while True:
        if (tk.StringVar.get(htmlsend) == "si"):
            message = MIMEMultipart()
            message['From'] = tk.StringVar.get(number1)
            message['To'] = tk.StringVar.get(receiver)
            message['Subject'] = tk.StringVar.get(oggetto)
            data = requests.get(tk.StringVar.get(htmlpagecode))
            print(data.text)
            message.attach(MIMEText(data.text))
            if (tk.StringVar.get(attach) == "si"):
                attach_file_name = tk.StringVar.get(attachfilenames)
                attach_file = open(attach_file_name)
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload((attach_file).read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
                message.attach(payload)
                session = smtplib.SMTP(smtpip, 587)
                session.starttls()
                session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
                text = message.as_string()
                session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
                session.quit()
                print("email sent")
            else:
                session = smtplib.SMTP(smtpip, 587)
                session.starttls()
                session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
                text = message.as_string()
                session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
                session.quit()
                print("email sent")
        else:
            message = MIMEMultipart()
            message['From'] = tk.StringVar.get(number1)
            message['To'] = tk.StringVar.get(receiver)
            message['Subject'] = tk.StringVar.get(oggetto)
            message.attach(MIMEText(tk.StringVar.get(textmail), 'plain'))
            if (tk.StringVar.get(attach) == "si"):
                attach_file_name = tk.StringVar.get(attachfilenames)
                attach_file = open(attach_file_name)
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload((attach_file).read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
                message.attach(payload)
                session = smtplib.SMTP(smtpip, 587)
                session.starttls()
                session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
                text = message.as_string()
                session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
                session.quit()
                print("email sent")
            else:
                session = smtplib.SMTP(smtpip, 587)
                session.starttls()
                session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
                text = message.as_string()
                session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
                session.quit()
                print("email sent")

def sendmail():
    if (tk.StringVar.get(htmlsend) == "si"):
        message = MIMEMultipart()
        message['From'] = tk.StringVar.get(number1)
        message['To'] = tk.StringVar.get(receiver)
        message['Subject'] = tk.StringVar.get(oggetto)
        data = requests.get(tk.StringVar.get(htmlpagecode))
        print(data.text)
        message.attach(MIMEText(data.text))
        if (tk.StringVar.get(attach) == "si"):
            attach_file_name = tk.StringVar.get(attachfilenames)
            attach_file = open(attach_file_name)
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            session = smtplib.SMTP(smtpip, 587)
            session.starttls()
            session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
            text = message.as_string()
            session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
            session.quit()
            print("email sent")
        else:
            session = smtplib.SMTP(smtpip, 587)
            session.starttls()
            session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
            text = message.as_string()
            session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
            session.quit()
            print("email sent")
    else:
        message = MIMEMultipart()
        message['From'] = tk.StringVar.get(number1)
        message['To'] = tk.StringVar.get(receiver)
        message['Subject'] = tk.StringVar.get(oggetto)
        message.attach(MIMEText(tk.StringVar.get(textmail), 'plain'))
        if (tk.StringVar.get(attach) == "si"):
            attach_file_name = tk.StringVar.get(attachfilenames)
            attach_file = open(attach_file_name)
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            session = smtplib.SMTP(smtpip, 587)
            session.starttls()
            session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
            text = message.as_string()
            session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
            session.quit()
            print("email sent")
        else:
            session = smtplib.SMTP(smtpip, 587)
            session.starttls()
            session.login(tk.StringVar.get(number1), tk.StringVar.get(number2))
            text = message.as_string()
            session.sendmail(tk.StringVar.get(number1), tk.StringVar.get(receiver), text)
            session.quit()
            print("email sent")
  

buttonCal = tk.Button(root, text="Invia", command=sendmail).grid(row=10, column=0)  
buttonCaloop = tk.Button(root, text="Invia Loop", command=sendmailloop).grid(row=11, column=0)  
  
root.mainloop()
