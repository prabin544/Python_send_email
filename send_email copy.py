import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'sender email'
receiver = 'receiver email'

msg = MIMEMultipart('alternative')
msg['Subjcet'] = 'Your Subject Goes here'
msg['From'] = sender
msg['To'] = receiver

Error = 'Your Error msg as param'

html = f"""\
    <div>
        <h2> Test Case Failed During Build </h2>
    </div>
    <div>
        <p>{Error}</p>
    </div>
    """

part1 = MIMEText(html, 'html')

msg.attach(part1)

s = smtplib.SMTP('your domain host')
s.sendmail(sender, reciver, msg.as_string())
s.quit()