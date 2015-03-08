#Name: quizGame.py
#Purpose: to run the quizGame!
#Author: Joshua Djakaria
class quizGame(object):

    def __init__(self):
        self.points = 0
        self.threshold = 1
        self.checkpoint = 0
    def get_points(self):
        return self.points

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_right(self):
        self.points +=1
        if  self.points % self.threshold == 0:
            self.checkpoint = self.points

    def get_wrong(self):
        self.points = self.checkpoint
