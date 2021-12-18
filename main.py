import yagmail
import os
import time
from datetime import datetime as dt

sender = 'xyz@gmail.com'
receiver = 'xyz@gmail.com'

subject = "This is the subject"

contents = """
Here is the content of the email!
Hi!
"""

while True:
  if dt.now().hour == 20 and dt.now().minute == 15:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print('Email Sent!')
    time.sleep(60)