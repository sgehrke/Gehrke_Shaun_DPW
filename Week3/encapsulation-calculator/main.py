'''
Shaun Gehrke
Lab 3 Encapsulated Calculator
DPW 1409

'''
import webapp2 # this is the main app import from google
from pages import Page # I created a seperate page - with this i can access it
from pages import Course

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page() # p instantiates the class Page
        c = Course() # c does the same for the class Course
        # Object for Pebble Beach
        pebble = Course()
        pebble.name = "Pebble Beach"
        pebble.yardage = 6828
        pebble.course_rating = 75.5 # this attribute is set to private in the contructor but with the getter-setter I am able to set the variable
        pebble.par = 72
        pebble.slope = 145
        pebble.calc_rating()
        pebble.bogey_rating = pebble.bogey_rating

        # Object for Bethpage Black
        bethpage = Course()
        bethpage.name = "Bethpage Black"
        bethpage.yardage = 7386
        bethpage.course_rating = 78.1
        bethpage.par = 72
        bethpage.slope = 152
        bethpage.calc_rating()
        print bethpage.bogey_rating


        # Object for TPC Sawgrass
        sawgrass = Course()
        sawgrass.name = "TPC Sawgrass"
        sawgrass.yardage = 7215
        sawgrass.course_rating = 76.8
        sawgrass.par = 72
        sawgrass.slope = 155
        sawgrass.calc_rating()
        print sawgrass.bogey_rating


        # Object for Shinecock Hills
        shinnecock = Course()
        shinnecock.name = "Shinnecock Hills"
        shinnecock.yardage = 6781
        shinnecock.course_rating = 74.7
        shinnecock.par = 72
        shinnecock.slope = 140
        shinnecock.calc_rating()
        print shinnecock.bogey_rating


        # Object for Winged Foot
        winged = Course()
        winged.name = "Winged Foot"
        winged.yardage = 7258
        winged.course_rating = 76.1
        winged.par = 72
        winged.slope = 145
        winged.calc_rating()
        print winged.bogey_rating


        # Object for Whistling Straits
        straits = Course()
        straits.name = "Whistling Straits"
        straits.yardage = 7362
        straits.course_rating = 77.2
        straits.par = 72
        straits.slope = 152
        straits.calc_rating()
        print straits.bogey_rating

        p.head = '''
        <!doctype html>
        <body>
        '''

        print c.name[0]
# This is a really neat way to dynamically acess and use the objects
        if self.request.GET:
            p.get_name = self.request.GET['name'] # uses the to dynamically fill the image tag
            course = self.request.GET['name'] # gets the click info
            c = locals()[course] # refers c to the object course
            p.course = c # lets pages.py have access to c
#both of the next lines print depending on conditional result
            print "line 88"
            print c
            self.response.write(p.page_result())
        else:
            self.response.write(p.print_page())
'''

So here I was going to have the conditionals do the work but I wanted it to be more dynamic- which is indicated by the above format with locals()
            # p.get_name = self.request.GET['name']
            # if self.request.GET['name'] == 'pebble':
            #     p.course = pebble
            # elif self.request.GET['name'] == 'bethpage':
            #     p.course = bethpage
            # elif self.request.GET['name'] == 'TPC':
            #     p.course = sawgrass
            # elif self.request.GET['name'] == 'shinnecock':
            #     p.course = shinnecock
            # elif self.request.GET['name'] == 'winged':
            #     p.course = winged
            # elif self.request.GET['name'] == 'whistling':
            #     p.course = straits
'''



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
