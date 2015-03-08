from twilio.rest import TwilioRestClient
from Twilio_send import sendMessage
from WolframAlpha import translate_english_to_language, clean_answer
import random

class Quiz():
    def __init__(self, user):
        self.user = user
            
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
class Question():
    def __init__(self, question):
        self.word = question

    def get_word(self):
        return self.word

    def getWolfAnswer(self, question, language="Spanish"):
        return clean_answer(translate_english_to_language(question, language))

    def text_question(self, message):
        sendMessage("+19287560154", "+19288974783", message)
        
def start():
    Joshquiz = Quiz("Josh")
    Joshquiz.load_user_info()
    Joshquiz.getQuestion()
    
