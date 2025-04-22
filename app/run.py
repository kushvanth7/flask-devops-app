from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__, template_folder="app/templates")
app.secret_key = "6LeTxiArAAAAACtfDlD6XSxr3uRnLkS_YnorzsHW"  # Required for flash messages

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    # You can log/store/send the message here
    print(f"New message from {name} ({email}): {message}")
    flash("Thanks for contacting me!")
    return redirect("/")
