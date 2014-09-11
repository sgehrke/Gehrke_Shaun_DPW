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
        # starts off my sections of the constructed page
        page_head = '''<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''
        # page for that will create the name for the key value pairs depending on the users response
        page_form = '''
        <form method="GET" action="">
            <label>Name: </label><input type="text" name="user"/><br/>
            <label>Street Address: </label><input type="text" name="street"/><br/>
            <label>City: </label><input type="text" name="city"/><br/>
            <label>State: </label>
                <select name="state">
                    <option value="" name=state" selected="selected">Select a State</option>
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
            <label>Email: </label><input type="text" name="email"/><br/>
            <label>Male </label><input type="radio" value="male" name="gender"/>
            <label>Female </label><input type="radio" value="female" name="gender"/>
            <input type="submit" value="submit"/>
            <input type="reset" value="reset"/>

        </form>'''








# DO NOT TOUCH - MAKES APP work in browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
