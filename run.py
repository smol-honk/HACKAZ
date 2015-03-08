from twilio.rest import TwilioRestClient
from Twilio_send import sendMessage
from WolframAlpha import translate_english_to_language, clean_answer
import random
from flask import Flask, request, redirect, session
import twilio.twiml
import os
from server import app


class Quiz():
    def __init__(self, user):
        self.user = user
        self.score = 0
            
    def check_user(self):
        self.user_check = False
        self.file = open("Users.txt", 'r')
        for line in file:
            if line == self.user:
                self.user_check = True
        self.file.close()
        return self.user_check
    
    def load_user_info(self):
        try:
            self.check_user()
            self.info = {}
            self.file = open(self.user + '.txt', 'r')
            for line in self.file:
                self.temp = line.split()
                self.info[self.temp[0]] = {self.temp[1] : self.temp[2]}
            self.file.close()
        except:
            return "You are not a valid user."

    def save_user_info(self):
        self.file = open(self.user + '.txt', 'w')
        for question in self.info.values():
            for answer in question.keys():
                self.file.write(question, " ", answer, " ", question[answer])

    def load_questions(self):
        self.questions = []
        self.questions_file = open("Words.txt", 'r')
        for line in self.questions_file:
            line = line.replace("\n", "")
            self.questions.append(line)
        return self.questions

    def getQuestion(self):
        self.possible_questions = self.load_questions()
        print(self.possible_questions)
        self.temp = random.choice(self.possible_questions)
        self.question = Question(self.temp)
        self.send_question = self.question.getWolfAnswer(self.question.get_word())
        self.question.text_question(self.send_question)
        
    def set_score(self, score):
        self.score = score
        
    def add_score(self, score):
        self.score += 1
class Question():
    def __init__(self, question):
        self.word = question

    def get_word(self):
        return self.word

    def getWolfAnswer(self, question, language="Spanish"):
        return clean_answer(translate_english_to_language(question, language))

    def text_question(self, message):
        user_number = input("What's your phone number?: ")
        sendMessage("+19287560154", "+1"+ user_number, message)
        
    def next_question(self):
        self.word = random.choice(self.load_questions)
        print(self.word)
        return self.question.text_question(self.word)
        
Joshquiz = Quiz("Josh")
Joshquiz.load_user_info()
Joshquiz.getQuestion()
print(Joshquiz.send_question)
    



port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    body = request.values.get('Body', None)
    
    if Joshquiz.question.get_word() == str(body).lower():
        message = "Good job! You got that one correct!" 
    else:
        message = "Incorrect. The correct answer is " + str(Joshquiz.question.get_word())

    print(Joshquiz.score)
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)

app.run(host='0.0.0.0', port=port) 

 


