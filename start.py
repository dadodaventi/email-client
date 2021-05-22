import os

os.system('pip install requests')
os.system('pip install tk')
servers = open("servers.bin", "w")
servers.write("Server smtp supportati: smtp-mail.outlook.com(outlook), smtp.gmail.com(gmail) default outlook")
servers.close()
os.system('py main.py')
os.remove('servers.bin')