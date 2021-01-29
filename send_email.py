import smtplib

def sendEmail(to , msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('practiceproject28@gmail.com' , 'lakshithost')
    server.sendmail('practiceproject28@gmail.com' , to , msg)
    server.close()






























































"""#import time
#from plyer import notification
#import os


if __name__ == '__main__':
    while True:
        notification.notify(
            title= "Please drink water",
            message= "You have to drink water rigt now",
            app_icon = "C:/Users/Lakshit/Documents/Python/Speech_Assistant/Blackvariant-Shadow135-System-Reminders.ico",
            timeout=10
            
record audio
resond
        )
"""
