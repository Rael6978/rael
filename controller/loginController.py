from flask import Blueprint, render_template

loginController = Blueprint("Login", __name__)

@loginController.route("/", methods = POST, GET)