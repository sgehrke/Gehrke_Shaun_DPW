'''
Shaun Gehrke
09/06/14
Design Patterns for Web Programming (DPW) 1409
Day 2 Lab: Simple-Form

'''


import webapp2 # use this library  - importing additional files

class MainHandler(webapp2.RequestHandler): # declares a class
    # constructor
    def get(self):
        # self.css = "css/style.css"

        # starts off my sections of the constructed page
        # codee will be validated through html until I learn the ways of pyhton
        page_head = '''<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css"
    </head>
    <header>
    </header>
    <body>'''
        # page for that will create the name for the key value pairs depending on the users response
        # with select/checkbox & radio use the value to dynamically enter key value pairs
        page_form = '''
        <section class="form1">
        <div class="form-left"><h1>The Worlds #1<br><strong>Sketchbooks</strong><hr></h1>
        <h2>ORDER YOURS TODAY!</h2>
        </div>
        <form method="GET" action="">
            <label>Name: </label><input  type="text" name="user"/>
            <label>Street Address: </label><input type="text" name="street"/>
            <label>City: </label><input type="text" name="city"/>
            <label>State: </label>
                <select name="state">
                    <option value="" selected="selected">Select a State</option>
                    <option value="AL">Alabama</option>
                    <option value="AK">Alaska</option>
                    <option value="AZ">Arizona</option>
                    <option value="AR">Arkansas</option>
                    <option value="CA">California</option>
                    <option value="CO">Colorado</option>
                    <option value="CT">Connecticut</option>
                    <option value="DE">Delaware</option>
                    <option value="DC">District Of Columbia</option>
                    <option value="FL">Florida</option>
                    <option value="GA">Georgia</option>
                    <option value="HI">Hawaii</option>
                    <option value="ID">Idaho</option>
                    <option value="IL">Illinois</option>
                    <option value="IN">Indiana</option>
                    <option value="IA">Iowa</option>
                    <option value="KS">Kansas</option>
                    <option value="KY">Kentucky</option>
                    <option value="LA">Louisiana</option>
                    <option value="ME">Maine</option>
                    <option value="MD">Maryland</option>
                    <option value="MA">Massachusetts</option>
                    <option value="MI">Michigan</option>
                    <option value="MN">Minnesota</option>
                    <option value="MS">Mississippi</option>
                    <option value="MO">Missouri</option>
                    <option value="MT">Montana</option>
                    <option value="NE">Nebraska</option>
                    <option value="NV">Nevada</option>
                    <option value="NH">New Hampshire</option>
                    <option value="NJ">New Jersey</option>
                    <option value="NM">New Mexico</option>
                    <option value="NY">New York</option>
                    <option value="NC">North Carolina</option>
                    <option value="ND">North Dakota</option>
                    <option value="OH">Ohio</option>
                    <option value="OK">Oklahoma</option>
                    <option value="OR">Oregon</option>
                    <option value="PA">Pennsylvania</option>
                    <option value="RI">Rhode Island</option>
                    <option value="SC">South Carolina</option>
                    <option value="SD">South Dakota</option>
                    <option value="TN">Tennessee</option>
                    <option value="TX">Texas</option>
                    <option value="UT">Utah</option>
                    <option value="VT">Vermont</option>
                    <option value="VA">Virginia</option>
                    <option value="WA">Washington</option>
                    <option value="WV">West Virginia</option>
                    <option value="WI">Wisconsin</option>
                    <option value="WY">Wyoming</option>
                </select>
            <label>Email: </label><input type="email" name="email"/>
            <label>Male: </label><input type="radio" value="male" name="gender"/>
            <label>Female: </label><input type="radio" value="female" name="gender"/>
            <label>Check if you are human? </label><input type="checkbox" name="agree" value="agree"/>
            <input type="reset" value="reset"/>
            <input type="submit" value="submit"/>
        </form>
        </section>
'''
# page_close has a container for the lower sketchbook image

        page_close = '''
        <div class="img-contain">
            <div class="form-center"></div>
        </div>
    </body>
    <footer></footer>
<html>
'''

# this if statement checks for the stored info from the user. If no response it will write else
        if self.request.GET:
            # stores users info from the form
            user = self.request.GET['user']
            street = self.request.GET['street']
            city = self.request.GET['city']
            state = self.request.GET['state']
            email = self.request.GET['email']
            #if the box is checked agree this will br human an be written to page_success
            agree = "human"
            # dynamic result here - this will change according to what is checked
            gender = self.request.GET["gender"] # or if gender-male == true /on
            # this is where the magic happens...with gender the page with have a diffent class added for a dif bg
            page_success = '''
        <section class="{gender}">
            <div class="form-left"><h1>Thank you for ordering our Sketchbook, {user}</h1></div>

                <div class="form-right">
                <p>We will ship your sketchbook to this address: </p>
                <p>{street}</p>
                <p>{city}, {state}</p>
                <hr/>
                <h3>Because you are a {agree}, we will also be sending you confirmation to {email}</h3>
                <p></p>
                </div>
        </section>
'''         # puts the correct information in dynamically
            page_success = page_success.format(**locals()) #

            # puts information onto the web page
            self.response.write(page_head + page_success + page_close)
        else:
            # this will be the first screen as there are no responses yet.
            self.response.write(page_head + page_form + page_close)

# DO NOT TOUCH - MAKES APP work in browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
