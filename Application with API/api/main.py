'''
Shaun Gehrke
DPW 1409 - 24
Final Project: Application with API
'''


import webapp2
import urllib2 #Python classes and code needed to request info
import json # makes json objects available


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
# Model class created as a constructor for the data
class ModelClass()
    def __init__(self):
        self.title = ''
        self.year = ''
        self.rating = ''
        self.synopsis = ''
        self.thumbnail = ''
        self.cast = []
        self.char = []

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
