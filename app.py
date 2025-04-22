
from flask import Flask, render_template, request, redirect, flash
import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage
import requests

app = Flask(__name__, template_folder="app/templates")
app.secret_key = "your_secret_key_here"

EMAIL_ADDRESS = "kushvanth2917@gmail.com"
EMAIL_PASSWORD = "Kushv@nth_17"
RECAPTCHA_SECRET = "your_recaptcha_secret_key"

def send_email(name, email, message):
    msg = EmailMessage()
    msg['Subject'] = "New Contact Form Submission"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"From: {name}\nEmail: {email}\nMessage:\n{message}")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    recaptcha_response = request.form['g-recaptcha-response']
    verify = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": RECAPTCHA_SECRET, "response": recaptcha_response}
    )
    result = verify.json()
    if not result.get("success"):
        flash("Captcha verification failed. Try again.")
        return redirect("/")

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    with open("contact_messages.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), name, email, message])

    send_email(name, email, message)

    flash("Thanks for contacting me! Message saved and emailed.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
