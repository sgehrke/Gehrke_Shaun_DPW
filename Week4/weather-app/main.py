
import webapp2
import urllib2 #Python classes and code needed to request info
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.input = [['zip', 'text', 'Zip Code'],['Submit', 'submit']]
        self.response.write(p.print_out())
        if self.request.GET:

            wm = WeatherModel()
            wm.zip = self.request.GET['zip']
            wm.callApi()

            wv = WeatherView()
            wv.wdos = wm.dos


            '''for item in list:
                self.content += item.attributes['day'].value
                self.content += "   HIGH: " + item.attributes['high'].value
                self.content += "   LOW: " + item.attributes['low'].value
                self.content += "   CONDITION: " + item.attributes['text'].value
                self.content += ' <img src="images/'+ item.attributes['code'].value + '.png" width="30"/>'
                self.content += '<br/>'
                # self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue)
            self.response.write(self.content)'''


class WeatherView(object):
    '''
    This class handles how data will be shown
    '''
    def __init__(self):
        self.__wdos = []

    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self,arr):
        self.__wdos = arr


class WeatherModel(object):
    ''' this model handles fetching parsing and sorting data form the API'''
    def __init__(self):
        self.url = url = 'http://xml.weather.yahoo.com/forecastrss?p='
        self.__zip = ''

    def callApi(self):
        #REQUESTS AND LOADS INFOR FROM API
        #assemble the request
        request = urllib2.Request(self.url+self.__zip)
        #use the urllib2 library to create object to get url
        opener = urllib2.build_opener()
        #use the url to get a result - request info from the API
        result = opener.open(request)
#parse the xml
        xmldoc = minidom.parse(result)

        #sorting the data
        list = xmldoc.getElementsByTagName('yweather:forecast')
        self._dos = []#array to store the data
        for tag in list:
            #create a data object
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high =  tag.attributes['high'].value
            do.low =  tag.attributes['low'].value
            do.code =  tag.attributes['code'].value
            do.condition = '<img src="images/'+ tag.attributes['text'].value
            do.date = tag.attributes['date'].value
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
    ''' this data object holds the data fetched my the model shown by the view'''
    def __index__(self):
        #attributses for each thing I want to collect
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''
        #designed to hold data in an associate array


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
        return self._head + self._body + self._close


#extends Page - ***INHERITANCE ****
class FormPage(Page):
    def __init__(self):
        # constructor function fo the superclass
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


# POLYMORHISM
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
