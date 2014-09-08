'''
Shaun Gehrke
09/06/14
Design Patterns fot Web Programming (DPW) 1409
Day 2 Lab: Classes Worksheet

'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
