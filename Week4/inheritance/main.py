
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.input = [['first_name', 'text', 'First Name'],['last_name', 'text', 'Last Name'],['Submit', 'submit']]
        self.response.write(p.print_out_form())

class Page(object):
    def __init__(self): # constructor function
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = 'Filler'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

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

        print self._form_inputs

    def print_out_form(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
