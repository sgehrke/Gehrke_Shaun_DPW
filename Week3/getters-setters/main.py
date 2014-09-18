'''
Shaun Gehrke
DPW 1409
getters-setters
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #t is for tommy - this is his grade
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99
        self.response.write("Tommies final grade is " + str(t.final_grade))
        #s is for sally - this is the instance of Transcript for sally
        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        self.response.write("<br/>Sallies final grade is " + str(s.final_grade))
class Transcript(object):
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0

    @property # getter
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def calc_grade(self):
        #calculate final grade
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
