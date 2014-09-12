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
        page_head = '''<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css"
    </head>
    <body>'''
        # page for that will create the name for the key value pairs depending on the users response
        page_form = '''
        
        <form method="GET" action="">
            <label>Name: </label><input type="text" name="user"/>
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
            <label>Email: </label><input type="text" name="email"/>
            <label>Male: </label><input type="radio" value="male" name="gender"/>
            <label>Female: </label><input type="radio" value="female" name="gender"/>
            <label>Check if you are human? </label><input type="checkbox" name="agree" value="agree"/>
            <input type="reset" value="reset"/>
            <input type="submit" value="submit"/>
        </form>
'''
		
        page_response = '''
		<section>
			<h1>Thank you for becoming a member</h1>
				<p>{self.name}</p>
				<p>{self.address}</p>
				<p>{self.city}</p>
				<p>{self.state}</p>
				<p>{self.email}</p>
				<p>{self.gender}</p>
				<p>{self.agree}</p>
		</section>
'''
        page_close = '''
    </body>
<html>
'''


        if self.request.GET:
            # stores users info from the form
            user = self.request.GET['user']
            street = self.request.GET['street']
            city = self.request.GET['city']
            state = self.request.GET['state']
            email = self.request.GET['email']
            if self.request.GET["gender"] == 'male': # or if gender-male == true /on
                gender = "you are a man"
            if self.request.GET["gender"] == 'female':
                gender = "you are a natural woman"
            if self.request.GET["agree"]:
                agree = self.request.GET['agree']
            else:
                agree = "you silly Robot, Trix are for kids"
                self.respose.write(page_head + "You willy Robot Trix are for kids")
            # puts information onto the webpage
            self.response.write(page_head + page_response + user + ' ' + street + ' ' + city + ' ' + state + ' ' + email + ' ' + gender + ' ' + agree + page_close)
        else:
            self.response.write(page_head + page_form + page_close)

    def print_this(self):
        page = page.format(**locals())
        return page

# DO NOT TOUCH - MAKES APP work in browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
