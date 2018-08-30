import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

def random_number():
    range_start = 10**(5)
    range_end = (10**6)-1
    return randint(range_start, range_end)

 
fromaddr = "abc@gmail.com"
toaddr = "xyz@gmail.com"
number = random_number()
text = "Your verfication code is " + str(number) 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password")
server.sendmail(fromaddr, toaddr, text)
server.quit()

