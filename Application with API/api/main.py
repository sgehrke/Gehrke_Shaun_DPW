'''
Shaun Gehrke
DPW 1409 - 24
Final Project: Application with API
'''


import webapp2
import urllib2 #Python classes and code needed to request info
import json # makes json objects available

#CONTROLLER
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #writes to the page
        self.response.write(p.print_page())

# this will connect the API and parse the json
class ModelClass(object):
    def __init__(self):
        self.do = ''



class ModelData(object):
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


# VIEW with pages
class Page(object):
    def __init__(self):
        #template fot the page

        self.head = '''header'''
        self.body = '''filler'''
        self.close = '''footer'''

    def print_page(self):
        return self.head + self.body + self.close



# popoulates model class with insatnces of it...use if request GET to fill ...like this movie = ModelClass()
#                             movie.title = self...GET MOVIE TITLE



#RESULTS CLASS to display the updated nfo to HTML in View/Page class

#GETTER_SETTERS

#ABSTRACTION




#POLYMORPHISM


