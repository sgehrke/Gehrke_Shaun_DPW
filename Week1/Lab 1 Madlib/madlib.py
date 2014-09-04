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
    "user_verb": raw_input("Enter a verb: "),
    "user_adjective": raw_input("Enter a descriptive word: ")
    }

# 1 Loop for or while



# Getting the responses and storing them in variables
fav_team = teamString["user_team"]
word = teamString["user_verb"]
adjective = teamString["user_adjective"]


# Prompt the user for 3 integers
# One Array to store the information

user_int = []

score_win = raw_input("Enter a number above 14: ")
score_lose = raw_input("Enter a number under 14: ")
year_int = raw_input("Enter a number above 2015: ")

user_int.append("score_win")
user_int.append("score_lose")
user_int.append("year_int")
#print user_int



# 2 mathematical operators --use a randomizor to pick the winner




winner = "Green Bay Packers"



top_teams = ["Broncos ", "49ers ", "Eagles ", "Patriots", "Colts ", "Saints ", "Falcons ", "Chiefs"]
tonights_teams = ["Packers", "Seahawks"]


# 1 Function that must return a value and have 2 parameters
def randomTeam():
    import random
    a = random.randint(0,7)
    return top_teams[a]

random_team = randomTeam()
print random_team

# tonights game winner generator
def tonightsWinner():
    import random
    a = random.randint(0, 1)
    return tonights_teams[a]
tonights_pick = tonightsWinner()
print tonights_pick

# 2 Conditional statements (if)
# if not the Packers or the Seahawks print message_1
if fav_team == "Packers" or fav_team  == "Seahawks":
    message_1 = '''
        The 2014 NFL season kicks off tonight with the Green Bay Packers taking on the Seattle Seahawks. The {tonights_pick}
        will win this game and go on to play in the Superbowl. If your {fav_team} are fortunate enough make it to the
        Superbowl, they will be defeated by the {winner} by a score of {score_win} - {score_lose}. The next time they
        will have an opportunity will be in {year_int}.
    '''
    message_1 = message_1.format(**locals())
    print message_1

# if the Packers print message_2
message_2 = '''

    '''
print message_2

# if the Seahawks print message_3
message_3 = '''

    '''
print message_3


