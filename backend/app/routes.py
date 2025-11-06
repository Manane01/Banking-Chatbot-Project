# Routes principales Flask

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello Bank Chatbot!"
