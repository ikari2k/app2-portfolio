import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = 'plutontestpython@gmail.com'
password = 'zdmtftedjxqbremt'

receiver = 'pluta.m@gmail.com'
my_context = ssl.create_default_context()

message = """\
Subject: Hi!
How are u?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context = my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)