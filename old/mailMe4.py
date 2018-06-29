import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

#set sender, recipients, and write subject here! Seperate by a ", " to add more! <MULTIPLE RECIPIENTS NOT TESTED!>
email_sender = 'pireslabgrowthmonitor@gmail.com'
email_reciever = ['pireslabgrowthmonitor@gmail.com', 'brandingrindstaff@gmail.com']
subject = 'Email Alert!'

#Uses MIMEMultipart function to fill these text fields in email.
msg = MIMEMultipart()
msg['To'] =", ".join(email_reciever)
msg['From'] = email_sender
msg['Subject'] = subject

#Add a body to your email!  msg.attach attaches body to email, and msg.as_string makes text info a string.
body = 'Light below threshold during operation time!'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

#Sends the email and closes the program properly.
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_sender, 'calvbDe68bIh*>%DQM')
server.sendmail(email_sender, email_reciever, text)
server.quit()

