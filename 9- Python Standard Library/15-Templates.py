from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
from pathlib import Path

template = Template(Path("template.html").read_text())


message = MIMEMultipart()

message["from"] = "Faessal Sufi"
message["to"] = "faessalsufi42@gmail.com"
message["subject"] = "A real a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("cover.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("faisalsufi24@gmail.com", "veww iszm hwka vrli ")
    smtp.send_message(message)
    print("Sent...")
