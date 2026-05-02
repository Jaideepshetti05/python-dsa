import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@gmail.com", "password")

server.sendmail("your_email@gmail.com", "to@gmail.com", "Hello!")
server.quit()