from twilio.rest import TwilioRestClient
from Twilio_send import sendMessage
from WolframAlpha import translate_english_to_language, clean_answer
from flask import render_template
import random
from flask import Flask, request, redirect, session
import twilio.twiml
import os
from server import app
import continuation

from flask import g

def after_this_request(func):
    if not hasattr(g, 'call_after_request'):
        g.call_after_request = []
    g.call_after_request.append(func)
    return func


@app.after_request
def per_request_callbacks(response):
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    return response