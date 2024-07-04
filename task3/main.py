import email
import smtplib
import imaplib
import settings
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Email:
    """
    Class for work with mail.
    """
    def __init__(self, login, password, GMAIL_SMTP, GMAIL_IMAP):
        self.login = login
        self.password = password
        self.GMAIL_SMTP = GMAIL_SMTP
        self.GMAIL_IMAP = GMAIL_IMAP

    """
    Method to send message via smtplib.
    """
    def send_msg(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(settings.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    """
    Method to receive message via imaplib.
    """
    def recieve_msg(self, header):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    gmail = Email(settings.login, settings.password, settings.GMAIL_SMTP, settings.GMAIL_IMAP)

    gmail.send_msg(recipients, subject, message)

    gmail.recieve_msg(header)