'''
Shaun Gehrke
09/06/14
Design Patterns for Web Programming (DPW) 1409
Day 2 Lab: Simple-Form

'''


import webapp2 # use this library  - importing additional files

class MainHandler(webapp2.RequestHandler): # declares a class
    # constructor
    def get(self):
        # starts off my sections of the constructed page
        page_head = '''<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''









# DO NOT TOUCH - MAKES APP work in browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
