from mailerpy import Mailer

password = "xcgv zfhm xece ilhr"
mailer = Mailer("smtp.gmail.com", 587, "aadritthapa01@gmail.com", password)

to_emails = ["vpgrinder2@gmail.com"]

subject = "Test Email from mailerpy"

body = "Hello, this is a test email sent using mailerpy library in Python."

mailer.send_mail(to_emails, subject, body, attachments=None)