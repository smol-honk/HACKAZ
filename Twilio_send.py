#Name: SMSTrillio.py
#Purpose: Use Twilio API to send a Text message
#Authors: Tyler Mitchel, Joshua Djakaria

'''
Input: my_phone_number (+XXXXXXXXXX), their_phone_number (+XXXXXXXXXX), message ""
Output: sends message
'''
def sendMessage (my_phone_number,their_phone_number, message):

    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC06d2905b4d94a16aad3d1eb76811090b"
    auth_token  = "e946720e2f4a75d6ceb1ab38db0de729"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=message,
        to=their_phone_number,
        from_=my_phone_number)
    #we can add this function later if we want to
    #media_url="https://pbs.twimg.com/profile_images/458794430200152064/XdQULww6_400x400.png"

    #print (message.sid)

if __name__ == "__main__":
    sendMessage("+19287560154", "+19288974783","SHEPARD OF FIRE!")
