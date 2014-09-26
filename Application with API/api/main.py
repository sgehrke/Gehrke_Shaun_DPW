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
        p = Page()#create instance of class page
        #writes to the page
        # sending information to the function by calling the setter by specifing the instance (Page)  with the setter eqialing the information
        self.response.write(p.print_page())
        if self.request.GET:
            mc = MovieClass()
            mc.title = self.request.GET['movie'].replace(' ', '+')
            mc.callAPI()

            wv = MovieView()
            wv.api_info = mc.do


class MovieView(object):
    ''' This class handles how the user is shown the data
    '''
    def __init__(self):
        #data object to be populated by the movie class
        self.api_info = MovieData()

    # def update(self):
    #     for tag in self.model:
    #         print tag


# this will connect the API and parse the json
class MovieClass(object):
    ''' This model handles fetching, parsing, and sorting data from the API'''
    def __init__(self):
        #get info from the API
        self.__url_open = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q='     #My API Key
        self.__url_close = '&page_limit=10&page=1&apikey=cbafcpcvjzx3b9g673aytwjp'
        self.__title = ''
        # calls the json document
        self.jsondoc = ''

    def callAPI(self):
        # Requests and loads data from API
        request = urllib2.Request(self.__url_open + self.__title + self.__url_close)
        # creates an object
        opener = urllib2.build_opener()
        # Requests data from API based on url
        result = opener.open(request)

        # Parses JSON data
        self.jsondoc = json.load(result)
        list = self.jsondoc['movies'][0]

        do = MovieData()
        do.title = self.jsondoc['movies'][0]['title']
        do.year = self.jsondoc['movies'][0]['year']
        do.mpaa_rating = self.jsondoc['movies'][0]['mpaa_rating']
        do.synopsis = self.jsondoc['movies'][0]['synopsis']
        # do.poster = self.jsondoc['movies'][0]['poster']
        do.cast = self.jsondoc['movies'][0]['abridged_cast']
        do.char = self.jsondoc['movies'][0]['abridged_cast'][0]['characters'][0]



    @property
    def title(self):
        pass

    @title.setter
    def title(self, new):
        self.__title = new

class MovieData(object):
    ''' this data object holds the data fetched by the model'''
    def __init__(self):
        self.title = ''
        self.year = 0
        self.mpaa_rating = ''
        self.synopsis = ''
        self.poster = ''
        self.cast = []
        self.char = []


# VIEW with pages
class Page(object):
    '''This is the template that will show as you get to the site -- and will be used later by the ResultsPage as a superclass'''
    def __init__(self): # constructor function
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = 'MY API'
        self.form = '''
        <form method="GET">
            <input type="text" name="movie" required="" placeholder="Search Movies Here"/>
            <input type="submit" value="Submit"/>
        </form>'''

        self._close = '''
    </body>
</html>'''

    def print_page(self):
        return self._head + self._body  + self.form + self._close


# #INHERITENCE
# class ResultPage(Page): # extends class page -subclass of Page
#     def __init__(self):
#         Page.__init__()# constructor for superclass
#         def __init__(self):
#
#             self.__cast = []
#
#
#     @property
#     def cast(self):
#         pass
#
#     @cast.setter
#     def cast(self, arr):
#         #change privat input and sorts through array to creat the input
#         self.__cast = arr
#         self.response.write(arr)
#



# popoulates model class with insatnces of it...use if request GET to fill ...like this movie = ModelClass()
#                             movie.title = self...GET MOVIE TITLE



#RESULTS CLASS to display the updated nfo to HTML in View/Page class

#GETTER_SETTERS

#ABSTRACTION




#POLYMORPHISM

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
