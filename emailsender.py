import schedule
import time
import smtplib


def email_sender():
    email = "huachibot@gmail.com"
    password = "pedrito8350"
    send_to_email = "dangler.scott11@gmail.com"
    message = "test message 123"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, send_to_email, message)
    server.quit()
    print("email sent")


schedule.every(30).seconds.do(email_sender)

while True:
    schedule.run_pending()
    time.sleep(1)
