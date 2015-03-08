from flask import Flask, request, redirect, session
import twilio.twiml
import os
from server import app
from Quiz import *

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    #from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    
    #print(Joshquiz.send_question)
    if Joshquiz.send_question == str(body):
        message = "Correct"
    else:
        message = "Incorrect"
    message = "Text"
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)

app.run(host='0.0.0.0', port=port) 
app.debug = True
 
if __name__ == "__main__":
    app.run(debug=True)
    #Joshquiz = Quiz("Josh")
    #Joshquiz.load_user_info()
    #Joshquiz.getQuestion()
    print(Joshquiz.send_question)
    print('steve')
