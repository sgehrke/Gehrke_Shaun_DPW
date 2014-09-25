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
        p.cast = [['hello'],['test'],['arr']]
        self.response.write(p.print_page())





# this will connect the API and parse the json
class ModelClass(object):
    def __init__(self):
        #get info from the API
        self.url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=' + self.request.GET['movie'].replace(' ', '+') + '&page_limit=10&page=1&apikey=cbafcpcvjzx3b9g673aytwjp'
    # assemble the request
        self.request = urllib2.Request(self.url)
        #use the urllib2 library to create object to get url
        self.opener = urllib2.build_opener()
        #use the url to get a result - request info from the API
        self.result = opener.open(self.request)

        #parse the json
        self.jsondoc = json.load(self.result)

        list = jsondoc['movies'][0]
        self.content = '<br/>'
        self.dos = []
        for tag in list:
            self.write.response(tag)
            do = ModelData()
            do.title = tag['movies'][0]['title']
            do.year = tag['year']
        #create variable for the json data
 #######Stuck here tryng to get JSON YEAR to show because its in an array

        # self.title = jsondoc['movies'][0]['title']
        # self.response.write('Your Movie is: ' + self.title)
        # self.main = jsondoc['movies'][0]['posters']['original']
        # response = '<img src"' + self.main + '">'
        # self.response.write(response)


class ModelData(object):
    ''' this data object holds the data fetched by the model'''
    def __init__(self):
        self.title = ''
        self.year = ''
        self.rating = ''
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

        self._close = '''
    </body>
</html>'''

    def print_page(self):
        return self._head + self._body  + self._close


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
