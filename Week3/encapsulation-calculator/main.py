'''
Shaun Gehrke
Lab 3 Encapsulated Calculator
DPW 1409

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Object for Pebble Beach
        pebble = Course()
        pebble.name = "Pebble Beach"
        pebble.yardage = 6828
        pebble.course_rating = 75.5
        pebble.par = 72
        pebble.slope = 145
        pebble.bogey_rating = ''
print cou

        # Object for Bethpage Black
        bethpage = Course()
        bethpage.name = "Bethpage Black"
        bethpage.yardage = 7386
        bethpage.course_rating = 78.1
        bethpage.par = 72
        bethpage.slope = 152
        bethpage.bogey_rating = ''


        # Object for TPC Sawgrass
        sawgrass = Course()
        sawgrass.name = "TPC Sawgrass"
        sawgrass.yardage = 7215
        sawgrass.course_rating = 76.8
        sawgrass.par = 72
        sawgrass.slope = 155
        sawgrass.bogey_rating = ''


        # Object for Shinecock Hills
        shinnecock = Course()
        shinnecock.name = "Shinecock Hills"
        shinnecock.yardage = 6781
        shinnecock.course_rating = 74.7
        shinnecock.par = 72
        shinnecock.slope = 140
        shinnecock.bogey_rating = ''


        # Object for Winged Foot
        winged = Course()
        winged.name = "Winged Foot"
        winged.yardage = 7258
        winged.course_rating = 76.1
        winged.par = 72
        winged.slope = 145
        winged.bogey_rating = ''


        # Object for Whistling Straits
        straits = Course()
        straits.name = "Whistling Straits"
        straits.yardage = 7362
        straits.course_rating = 77.2
        straits.par = 72
        straits.slope = 152
        straits.bogey_rating = ''



















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
