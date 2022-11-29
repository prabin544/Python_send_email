import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our HTML email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('localhost')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""

    email_content = """

Cell 1.1	Cell 1.2
Cell 2.1	

"""

    TO = 'pravin544@gmail.com'
    FROM ='pravin544@gmail.com'

    py_mail("Test email subject", email_content, TO, FROM)