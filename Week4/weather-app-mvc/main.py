
import webapp2
import urllib2 #Python classes and code needed to request info
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip','text','zip code'],['Submit','submit']]

        if self.request.GET: # only if there is a zip variable in the url

            wm = WeatherModel() # creates model
            wm.zip = self.request.GET['zip'] # sends zip from url to model
            wm.callAPI() # tells it to connect to api

            wv = WeatherView() # creates view
            wv.wdos = wm.dos # takes data objects from model and gives them to view
            p._body = wv.content

        self.response.write(p.print_out())



class WeatherView(object):
    '''this class handles how the data is shown to the user'''
    def __init__(self):
        self.__wdos = []
        self.__content = '<br>'

    def update(self):
        for do in self.__wdos:

            self.__content += do.day
            self.__content += '    HIGH: ' + do.high + '    LOW: ' + do.low
            self.__content += '    CONDITION: ' + do.condition
            self.__content += '    <img src="images/' + do.code + '.png" width="20"><br>'

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

class WeatherModel(object):
    '''this model handles fetching parsing and sorting data from yahoos weather api'''
    def __init__(self):
        self.__url = 'http://xml.weather.yahoo.com/forecastrss?p='
        self.__zip = ''
        self.__xmldoc = ''
        # parse the url

    def callAPI(self):
        # requests and loads info from api
        # assemble the request
        request = urllib2.Request(self.__url + self.__zip)
        # use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        # use the url to get a result - request info from the api
        result = opener.open(request)
        # parsing data
        self.__xmldoc = minidom.parse(result)

        # sorting data
        list = self.__xmldoc.getElementsByTagName('yweather:forecast')
        self._dos = []

        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes ['low'].value
            do.date = tag.attributes ['date'].value
            do.code = tag.attributes ['code'].value
            do.condition = tag.attributes ['text'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z

class WeatherData(object):
    ''' this data object holds the data fetched by the model shown by the view '''
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''

class Page(object): # borrowing stuff from object class
    def __init__(self): # constructor
        self._head = '''
<!doctype html>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = ''

        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    # constructor function for the super class
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self,arr):
        # change my private inputs variable
        self.__inputs = arr
        # sort through the mega array and create html inputs based on the info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try: # if there is a third item, add it in
                self._form_inputs += '" placeholder="' + item[2] + '">'
            except: # otherwise, end the tag
                self._form_inputs += '" >'

    # polymorphism... overriding

    def print_out(self):
        return self._head + 'Weather App' + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
