#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("hemavathy10iadrt@gmail.com","hema") #sender's mail id
message="hi"#message to be sent
s.sendmail("hemavathy10iadrt@gmail.com","hemavathy10iadrt@gmail.com",message) #reciver's mail id
s.quit()

