import yagmail
import os

sender = 'xyz@gmail.com'
receiver = 'xyz@gmail.com'

subject = "This is the subject"

contents = """
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print('Email Sent!')