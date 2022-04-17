from flask import Flask

app = Flask(__name__)

app.secret_key = "Ok man"

# secret key here if using session