from flask import Flask
from controller import loginController

app = Flask(__name__)
app.register_blueprint(loginController)

@loginController.route("/")
def login():
    return render_template()