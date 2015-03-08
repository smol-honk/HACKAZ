import flask
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC06d2905b4d94a16aad3d1eb76811090b" 
AUTH_TOKEN = "e946720e2f4a75d6ceb1ab38db0de729" 
 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def text(to, body):
    flask.flash("To: " + to)
    flask.flash("Body: " + body)
    
    client.messages.create(
        to = to,
        from_="+19287560154",
        body = body,
 )
    
