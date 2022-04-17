from flask_app import app
from flask_app.controllers import controller_emails
from flask_app.models import email

if __name__ == "__main__":
    app.run(debug=True)