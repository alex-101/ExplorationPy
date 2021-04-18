global os, sys, importlib, time, webbrowser
try:
    import os, sys, importlib, time, webbrowser
except Exception as Exc:
    print("ERROR 001 ('README.txt')")
    input()
    exit()
global API
try:
    import API
except:
    print("ERROR 005 ('README.txt')")
    input()
    exit()    
sys.path.insert(0, 'Missions')
print("""
Welcome, to ExplorationPy.
Missions can be installed using the "Missions" folder.
""")
Option = False
def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
def fatal(strr):
    print("ERROR {} ('README.txt')".format(strr))
    input()
    exit()
while True:
    Option = input("""
1 | Play Mission
2 | Help
3 | Credits
4 | More
>""")
    if Option in ["1","2","3", "4"]:
        break
    print("Invalid.")
if Option=="1":
    Options = []
    for (file) in os.listdir('Missions'):
        if ('.py' in file) and (file!="__init__.py"):
            try:
                Mission = importlib.import_module(file.split(".py")[0])
                try:
                    MissionCon = Mission.ExplorationPyFile
                except AttributeError:
                    print("Unrecognised Mission File '{}'".format(file))
                    input()
                    exit()
                Options.append(Mission)
            except Exception as Except:
                fatal("003 ({})".format(Except))
    if len(Options) == 0:
        print("You don't have any missions installed, view the Help menu or the README.txt file to learn how to install them.")
        input()
        exit()
    i = 0
    for Mission in Options:
        print("""
> {} <
Name: {}
Author: {}

""".format(i,Mission.Name,Mission.AuthorS))
        i=i+1
    ################
    ## Get Chosen ##
    ################
    ChosenMission = False
    while True:
        try:
            ChosenMission = input("Select A Mission\n>")
            ChosenMission = Options[int(ChosenMission)]
            break
        except Exception:
            print("Failed to get provided mission.")
    print("""

---------------


Name: {}
AuthorS: {}
Description: {}
""".format(ChosenMission.Name, ChosenMission.AuthorS, ChosenMission.Description))
    input("-- HIT RETURN TO RUN THE MISSION --")
    print("Good luck - ExplorationPy")
    try:
        if ChosenMission.ExplorationPyFile == 1.1:
            ChosenMission.Game(API)
        else:
            print("You are running V1.1, this mission is wrote for 'V{}'.".format(ChosenMission.ExplorationPyFile))
    except Exception as Exc:
        print("Failed to load mission and invoke Game. This is most likely due to a fault in the mission. ({})".format(Exc))
if Option=="2":
    print("""
> How to install a mission.
Download a mission, and move it into the "Missions" folder.
Assuming it is valid, it will be available on the "Play Mission" menu.
""")
if Option=="3":
    print("""
> Credits
Alex
Python.org
""")

if Option=="4":
    Choice = API.menu(["API Reference", "Share/Download missions", "Issue A Bug Report", "Issue A Suggestion"])
    if Choice == "API Reference":
        webbrowser.open('https://github.com/alex-101/ExplorationPy/wiki',2)
    elif Choice == "Share/Download missions":
        webbrowser.open("https://github.com/alex-101/ExplorationPy/discussions/categories/missions",2)
    elif Choice == "Issue A Bug Report":
        webbrowser.open("https://github.com/alex-101/ExplorationPy/issues",2)
    else:
        webbrowser.open("https://github.com/alex-101/ExplorationPy/discussions/categories/suggestions",2)
        
input("HIT ENTER TO CLOSE")
exit()
