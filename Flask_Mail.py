from flask import Flask
from flask_mail import Mail , Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME']= 'maidris2001@gmail.com'
app.config['MAIL_PASSWORD']= 'hnqo utgf oghs icva'
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('WAGWAN FAM?', sender= 'maidris2001@gmail.com', recipients = ['hardeolar20@gmail.com'])
    msg.body = "Test-run Flask message sent from Flask-Mail app"
    mail.send(msg)
    return "Message Sent!"

if __name__ == '__main__':
    app.run(debug = True)