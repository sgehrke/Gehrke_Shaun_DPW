class Page(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/style.css"
        self.head = '''
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.__body = "Welcome to my OOP Python Page!"
        self.close = '''
    </body>
</html>
        '''

        self.whole_page = ""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()