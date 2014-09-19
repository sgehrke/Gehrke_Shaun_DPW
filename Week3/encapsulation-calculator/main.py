'''
Shaun Gehrke
Lab 3 Encapsulated Calculator
DPW 1409

'''
import webapp2
from pages import Page
from pages import Course

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        c = Course()
        # Object for Pebble Beach
        pebble = Course()
        pebble.name = "Pebble Beach"
        pebble.yardage = 6828
        pebble.course_rating = 75.5
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
        shinnecock.name = "Shinecock Hills"
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



        if self.request.GET:
            p.get_name = self.request.GET['name']
            if self.request.GET['name'] == 'pebble':
                p.course = pebble
                # p.get_yardage = self.request.GET['yardage']
                # p.get_course_rating = self.request.GET['course_rating']
                # p.get_par = self.request.GET['par']
                # p.get_slope = self.request.GET['slope']
            # p.get_bogey_rating = p.calc_rating()

            self.response.write(p.page_result())
        else:
            self.response.write(p.print_page())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
