import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import config

def send_email(to_email, file):
    from_email = config.EMAIL_USER
    subject = "Planilha do contrato"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    body = "Segue em anexo a planilha do contrato."
    msg.attach(MIMEText(body, 'plain'))

    with open(file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={file}')
        msg.attach(part)

    try:
        server = smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT)
        server.starttls()
        server.login(from_email, config.EMAIL_PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")