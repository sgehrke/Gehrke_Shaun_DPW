class Page(object):
    def __init__(self):
        self.title = ''
        self.css = "css/style.css"
        self.head = '''<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>Encapsulation</title>
	<link href="{self.css}" rel="stylesheet" type="text/css" />
</head>
<body>

	<header id="main"></header>
        '''

        self.body = '''	<section>
		<div class="container">
		<h1>Top <span>US</span><span style="color: blue;">GA</span></span> Course Ratings</h1>
			<ul class="thumbnails cf">
				<a href="/?name=Pebble+Beach"><li class="thumbnail">
					<header>
						<h2>Pebble Beach</h2>
					</header>
					<figure>
						<img src="images/course1_thumbnail.jpeg" alt="course1_thumbnail" width="259" height="194">
					</figure>

					<div><p>Pebble Beach Resorts is a legendary place. Combining a dramatic coastline with a mystical forest. Perhaps nowhere else on the planet does this combination come together quite like Pebble Beach.</p></div>

				</li></a>
				<li class="thumbnail">
					<header>
						<h2>Bethpage (Black)</h2>
					</header>
					<figure>
						<img src="images/course2_thumbnail.jpeg" alt="course2_thumbnail" width="259" height="194">
					</figure>
					<div><p>The Black Course is a difficult and challenging course that should be played only by low-handicap golfers. The course is for walkers only and its slope rating is one of the highest in the northeast.</p></div>
				</li>
				<li class="thumbnail">
					<header>
						<h2>TPC Sawgrass</h2>
					</header>
					<figure>
						<img src="images/course3_thumbnail.jpeg" alt="course3_thumbnail" width="259" height="194">
					</figure>
					<div><p>Home of THE PLAYERS Championship, birthplace of the TPC Network, and backdrop to the PGA TOUR headquarters, TPC Sawgrass is perhaps the world's most famous golf course</p></div>
				</li>
				<li class="thumbnail">
					<header>
						<h2>Shinnecock Hills</h2>
					</header>
					<figure>
						<img src="images/course4_thumbnail.jpeg" alt="course4_thumbnail" width="259" height="194">
					</figure>
					<div><p>Shinnecock Hills Golf Club, founded in 1891, is one of the historic golfing institutions in the United States. It is the oldest incorporated golf club and was one of the five founding member clubs of the USGA.</p></div>
				</li>
				<li class="thumbnail">
					<header>
						<h2>Winged Foot</h2>
					</header>
					<figure>
						<img src="images/course5_thumbnail.jpeg" alt="course5_thumbnail" width="259" height="194">
					</figure>
					<div><p>Winged Foot is nothing less than the finest golf club in metropolitan New York. Given the wealth of great golf in the area, that lofty position also means Winged Foot is surely on the short list of contenders for the best golf club in the world.</p></div>
				</li>
				<li class="thumbnail">
					<header>
						<h2>Whistling Straits</h2>
					</header>
					<figure>
						<img src="images/course6_thumbnail.jpeg" alt="course6_thumbnail" width="259" height="194">
					</figure>
					<div><p>Arguably the greatest championship course in the United States, it has hosted the 2004 & 2010 PGA Championships - and it is the future site of the 2015 PGA Championship and 2020 Ryder Cup.</p></div>
				</li>
			</ul>
		</div>
	</section>

        '''

        self.footer = '''
        <footer></footer>
</body>
</html>

        '''



    def print_page(self):
        page = self.head + self.body + self.footer
        page = page.format(**locals())
        return page




class Course(object):
    def __init__(self):
        self.name = ''
        self.yardage = 0
        self.course_rating = 0
        self.par = ''
        self.slope = 0
        self.__bogey_rating = 0 # this will be the number that a bogey golf should expect to score

    @property
    def bogey_rating(self):
        return self.__bogey_rating

    @bogey_rating.setter
    def bogey_rating(self, new_bogey_rating):
        self.__bogey_rating =  new_bogey_rating
        self.calc_rating()

    def calc_rating(self):
        self.__bogey_rating = round(self.slope / 5.381 + self.course_rating, 2)
