import smtplib

def sendEmail(to , msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'password')
    server.sendmail('youremail@gmail.com' , to , msg)
    server.close()































































