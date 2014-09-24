
import webapp2
import urllib2 #Python classes and code needed to request info
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p._body = "Movie Finder"
        p.input = [['movie', 'text', 'Movie Name'],['Submit', 'submit']]
        self.response.write(p.print_out())
        if self.request.GET:

            #get info from the API
            url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=' + self.request.GET['movie'].replace(' ', '+') + '&page_limit=10&page=1&apikey=cbafcpcvjzx3b9g673aytwjp'
            #assemble the request
            request = urllib2.Request(url)
            #use the urllib2 library to create object to get url
            opener = urllib2.build_opener()
            #use the url to get a result - request info from the API
            result = opener.open(request)

            #parse the json
            jsondoc = json.load(result)
            print jsondoc

            title = jsondoc['movies'][0]['title']
            self.response.write('Your Movie is: ' + title)
            main = jsondoc['movies'][0]['posters']['original']
            response = '<img src"' + main + '">'
            self.response.write(response)
            #parse the json


class Page(object):
    def __init__(self): # constructor function
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = 'Weather App'

        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body  + self._close

class FormPage(Page):
    def __init__(self):
        # constructor function fo the subclass
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__input = []
        self._form_inputs = ''
        #<input type="text" value="" name="" placeholder=""/>
        # ['first_name', 'text', 'First Name']

    @property
    def input(self):
        pass

    @input.setter
    def input(self, arr):
        #change my private input variable
        self.__input = arr

        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item add it im otherwise ...add it in
            try:
                self._form_inputs += '" placeholder="' + item[2] + '"/>'
            except:
                self._form_inputs += '"/>'
        #sort throught the array of arrays and create html based on array


    #POLYMORHISM ALERT!!!!!--------------subclass method overriding parent
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
