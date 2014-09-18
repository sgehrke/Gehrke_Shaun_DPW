'''
Shaun Gehrke
Lab 3 Encapsulated Calculator
DPW 1409

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Course(object):
    def __init__(self):
        self.name = ''
        self.yardage 0
        self.course_rating = 0
        self.par = ''
        self.slope = 0
        self.bogey_rating = 0 # this will be the number that a bogey golf should expect to score





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
