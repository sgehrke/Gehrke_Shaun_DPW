'''
Name: Shaun Gehrke
Class: Design Patterns fro Web Programming 1409
Assignment: Python MadLib

'''
# Prompt the user for 3 strings
# One Dictionary - use to store prompted items like an object

teamString = dict()
teamString = {
    "user_team": raw_input("Please enter your favorite NFL teams name: "),
    "user_place": raw_input("Enter a place: "),
    "user_adjective": raw_input("Enter a descriptive word: ")
    }





# Getting the responses and storing them in variables
fav_team = teamString["user_team"]
place = teamString["user_place"]
adjective = teamString["user_adjective"]

# 1 for loop that changes all items to uppercase
for i in teamString:
    print teamString[i].upper()

if fav_team != "PACKERS":
    winner = "Green Bay Packers"


# One Array to store the information
user_int = []

# Prompt the user for 3 integers
score_win = user_int.append(raw_input("Enter a number above 14: "))
score_lose = user_int.append(raw_input("Enter a number under 14: "))
year_int = user_int.append(raw_input("Enter a number above 2015: "))


print user_int

if user_int[0] > 20:
    #win turns into dominated
    win = "dominated"
else:
    win = "win"


top_teams = ["Broncos ", "49ers ", "Eagles ", "Patriots", "Colts ", "Saints ", "Falcons ", "Chiefs"]
length_top_teams = len(top_teams)
tonights_teams = ["Packers", "Seahawks"]
length_tonights_teams = len(tonights_teams)
# use a randomizor to pick the winner of tonights game
# 1 Function that must return a value and have 2 parameters
# this randomizer will dynamically return things
def randomizer(b,c):
    import random
    b -= 1 # to start the index from 0 and is one mathematical operator b = b -1
    a = random.randint(0,b)
    print b
    print "the random number is", str(a)
    return c[a]


random_team = randomizer(length_top_teams, top_teams)
print random_team

tonights_pick = randomizer(length_tonights_teams, tonights_teams)
print tonights_pick


# if not the Packers or the Seahawks print message_1
if tonights_pick == fav_team:
    message_1 = '''
        The 2014 NFL season kicks off tonight with the Green Bay Packers taking on the Seattle Seahawks at the {place}
        stadium. The {tonights_pick} will {win} this game and go on have a {adjective} season. Your {fav_team} will play
        the {random_team} in this years super bowl and win by a score of {user_int[0]} - {user_int[1]}. The next time
        they will have an opportunity to play in a Superbowl will be in {user_int[2]}.
    '''
    message_1 = message_1.format(**locals())
    print message_1

else:
    message_2 = '''
        The 2014 NFL season kicks off tonight with the Green Bay Packers taking on the Seattle Seahawks at the {place}
        stadium. The {tonights_pick} will {win} this game and go on have a {adjective} season. Your {fav_team} will play
        the {random_team} in this years super bowl and win by a score of {user_int[0]} - {user_int[1]}. The next time
        they will have an opportunity to play in a Superbowl will be in {user_int[2]}.
    '''
    message_2 = message_2.format(**locals())
    print message_2




