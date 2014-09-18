

import webapp2

from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # create an instance of the page class - creates a page using this class - it will also call the constructor method
        p = Page()
        p.title = "MyPage!"
        p.body = "Miss piggy loves Kermit da Frog"

        self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
