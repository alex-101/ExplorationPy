#// File Name: Example.py
#// Mission Name: Example
#// Description: Play this example world.
#// Credits: Alex

ExplorationPyFile = 1
Name = "The Void"
AuthorS = "Alex"
Description = "Voyager slips into a pocket of subspace where many other ships are trapped and must steal from each other to survive. Only with the help of other star ships can they all escape the void. You will play the captain."

global time
try:
    import time
except Exception as Exc:
    print("ERROR 006 ('README.txt')")
    input()
    exit()
def Game(API):
    #"""
    API.write("Welcome to the USS Voyager, registration NCC-74656",0.05)
    time.sleep(0.2)
    print("\n")
    API.write("In this Mission, you will play the captain.",0.1)
    API.say("Play")
    API.write("We're being pulled into an anomaly captain!",0.05)
    API.menu(["Try reversing the shield polarity.", "Divert power to the thrusters"])
    API.write("...",0.2)
    print("No effect")
    time.sleep(0.2)
    API.write("* You look outside, the stars are gone *",0.01)
    time.sleep(0.2)
    API.write("Captain! We're being fired on. Shields are at 65 %!",0.05)
    time.sleep(0.1)
    #"""
    Chosen = API.menu(["Hail Them", "Return Fire"])
    if Chosen=="Hail Them":
        API.write("Hailing them.",0.05)
        time.sleep(0.1)
        API.write("No response",0.05)
        time.sleep(0.2)
        API.say("Return Fire")
    API.write("Aye, firing",0.1)
    time.sleep(0.5)
    API.say("Can you identify them?")
    API.write("Negative.",0.1)
    time.sleep(1)
    API.write("There's another ship approaching, it's charging weapons.",0.025)
    API.menu(["Recieved", "Evasive Patterns!"])
    API.write("Captain, the other vessel. They're shooting our attacker.",0.01)
    time.sleep(0.5)
    API.write("Our attacker is retreating.",0.02)
    API.say("Maybe we have an ally here?")
    time.sleep(1)
    API.write("Negative captain, it's firing.",0.02)
    time.sleep(1)
    API.write("It's taken supplies of decks 5, 7 and 8.",0.02)
    Chosen = API.menu(["Disable their engines.", "Transport it back."])
    if Chosen=="Disable their engines.":
        API.write("Firing.",0.1)
    else:
        API.write("Negative captain, they've erected a shield.",0.02)
    time.sleep(0.4)
    API.write("They've gone to warp. We've lost them.",0.02)
    Chosen = API.menu(["Get me a damage report.", "I want an inventory of what's been taken."])
    if Chosen=="Get me a damage report.":
        API.write("Shields are holding at 40%, the navigational array has taken damage.",0.02)
    else:
        API.write("They got more than 90% of our food stores.",0.02)
    API.write("They also emptied three of our deuterium tanks",0.02)
    API.say("Why would anyone take deuterium? You can get it anywhere.")
    API.write("Apparantly not here, I'm not detecting any gases, planets or matter of any kind",0.01)
    time.sleep(1)
    API.write("Captain, another vessel approaching.",0.01)
    if API.menu(["Shields up, charge weapons.", "Hail It"])=="Hail It":
        API.write("Hailing it...")
    else:
        API.write("Aye.",0.2)
        time.sleep(0.3)
        API.write("It's hailing us.",0.15)
        API.say("Put it on screen.")
    ## "Hail"
    time.sleep(0.2)
    API.write("* The captain of the alien vessel appears on screen. *",0.01)
    time.sleep(0.2)
    API.say("I'm captain Janeway of the Starship Voyager.")
    API.write("\"General Valen, welcome to the Void.\"",0.1)
    time.sleep(0.2)
    API.say("Your the first ship we've seen here that hasn't tried to fire on us.")
    API.say("But, incase you change your mind we're prepared to defend ourselves.")
    API.write("\"I know, I've been observing you on sensors.\"",0.05)
    time.sleep(0.3)
    API.write("\"Your impressive, most ships don't survive the first few minutes.\"",0.05)
    time.sleep(0.3)
    API.say("I'd appreciate any information you could give me on where we are..")
    API.write("\"Of course.\"",0.05)
    time.sleep(0.5)
    API.write("\"We're encased by a an inert layer of space.\"",0.05)
    time.sleep(0.5)
    API.write("\"Matter and energy can't penetrate it.\"",0.05)
    if API.menu(["Then how did we get in?", "How do we get out."]) == "How do we get out.":
        # How to get out.
        API.write("You don't, matter only comes in.")
    else:
        # How you got in.
        API.write("\"The funnels, but they only pull matter in one direction.\"",0.05)
    time.sleep(0.3)
    API.say("There must be a way to escape.")
    time.sleep(0.3)
    API.write("\"New arrivals are always thinking about escape.\"",0.05)
    time.sleep(0.3)
    API.say("We have a sophisticated starship,")
    API.say("maybe if we work together we can find a way out.")
    time.sleep(0.3)
    API.write("\"Your being naive, no one ever gets out.\"",0.05)
    time.sleep(0.3)
    API.say("We may be able to devise a new approach.")
    time.sleep(0.3)
    API.write("\"Many have tried, all they did was waste resources that could of kept them alive longer.\"",0.05)
    time.sleep(0.3)
    API.write("\"Don't make stupid mistakes, we can help you.\"",0.05)
    API.say("What do you get in return?")
    API.write("\"Your gratitude, oh and your torpedoes.\"",0.05)
    API.menu(["We don't trade in weapons.","Alright."])
def __init__():
    print("Idek")