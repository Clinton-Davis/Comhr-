import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main Pain with instuction"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    return "HI " + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)



app.run(host=os.getenv('IP'),debug=True)
   