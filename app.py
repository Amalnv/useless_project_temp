from flask import flask, render_template,request
import smtplib
from email.mime.text import MIMEText

app=flask(__name__)

SENDER_EMAIL='your_email@gmail.com'
SENDER_PASSWORD='your_app_password'

@app.route('/',methods=['GET','POST'])
def secret_form():
    if request.method=='POST':
        secret=request.form['secret']
        secret_form = request.form['secret_form']
        to_email = request.form['to_email']
        forbidden_people=request.form['forbidden_people'].split(',')

        email_body=f"""
           You've received a SECRET !

           Secret: {secret}

           Source: {secret_from}

            Please do NOT share this with:
            {','.join([p.strip() for p in forbidden_people])}
            """

            try:
                send_secret_email(to_email,"shhh... It's a secret",email_body)
                return "Secret sent succesfully!"
            except Exception as e:
                returm f"failed to sent email: {e}"
    return render_template('form.html')
def send_secret_email(to_email, subject,body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail,com,465") as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
if __name__ == "__main__":
    app.run(debug=True)