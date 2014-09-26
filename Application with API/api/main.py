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

        if self.request.GET:
            mm = MovieModel()
            mm.title = self.request.GET['movie'].replace(' ', '+')
            mm.callAPI()# connects it to API


            mv = MovieView()
            mv.wdos = mm.dos # takes data on objects from model class
            p._body = mv.content



        self.response.write(p.print_page())

class MovieView(object):
    ''' This class handles how the user is shown the data
    '''
    def __init__(self):
        #data object to be populated by the movie class
        self.__wdos = []
        self.__content = '<br/>'



    def update(self):
        for do in self.__wdos:

            content_head = '''
            <section> '''

            main_content = '''
                <div class="container">
                    <img width="400" src="''' + do.poster + '''"></img>
                    <div id="main">
                        <h2>''' + do.title + '''</h2>
                        <ul>
                            <li>Year: ''' + str(do.year) + '''</li>
                            <li>Rating: ''' + do.mpaa_rating + '''</li>
                            <li>Runtime: ''' + str(do.runtime) + '''</li>
                            <li>Main Character: ''' + do.char + '''</li>

                        </ul>
                    </div>
                </div>
                    '''

#couldnt figure this art out so I changed attributes


            # cast_members = ''
            # print cast_members
            # for item in do.cast:
            #     # Retrieves each cast member if available
            #     try:
            #         cast_members += do.cast[item]
            #     except:
            #         cast_members += ''
            #     try:
            #         cast_members += do.characters[item]
            #     except:
            #         cast_members += ''

            content_close = '''
            </section>
            </div>
            <footer class="footer">Shaun Gehrke DPW 1409</footer>'''
            self.__content = content_head + main_content +  content_close


    @property
    def content(self):
        return self.__content
    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        self.update()

# this will connect the API and parse the json
class MovieModel(object):
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
        list = self.jsondoc['movies']
        self._dos = []


        for tag in list:

            do = MovieData()
            do.title = self.jsondoc['movies'][0]['title']
            do.year = self.jsondoc['movies'][0]['year']
            do.mpaa_rating = self.jsondoc['movies'][0]['mpaa_rating']
            do.poster =self.jsondoc['movies'][0]['posters']['original'].replace('_tmb.jpg', '_ori.jpg')
            do.runtime = self.jsondoc['movies'][0]['runtime']
            do.char = self.jsondoc['movies'][0]['abridged_cast'][0]['characters'][0]
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos


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
        self.runtime = 0
        self.poster = ''
        self.char = ''


# VIEW with pages
class Page(object):
    '''This is the template that will show as you get to the site -- and will be used later by the ResultsPage as a superclass'''
    def __init__(self): # constructor function
        self._head = '''
<!DOCTYPE HTML>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" href="css/style.css" title="css" type="text/css" media="screen" charset="utf-8">
	<title>Movie Case</title>
</head>'''
        self._body = 'MY API'
        self.form = '''
        <header>
            <div class="container">
            <h1>Movie Case</>
            <form method="GET" class="right">
                <input  class="right"type="text" name="movie" required="" placeholder="Search Movies Here"/>
                <input  class="right"type="submit" value="Submit"/>
            </form>
            </div>
        </header>'''

        self._close = '''
    </body>
</html>'''

    def print_page(self):
        return self._head + self.form + self._body + self._close


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


#ABSTRACTION




#POLYMORPHISM

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
