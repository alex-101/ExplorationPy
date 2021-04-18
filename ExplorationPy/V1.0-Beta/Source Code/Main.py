global os, sys, importlib, time
try:
    import os, sys, importlib, time
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
>""")
    if Option in ["1","2","3"]:
        break
    print("Invalid.")
if Option=="1":
    Options = []
    for (file) in os.listdir('Missions'):
        if ('.py' in file) and (file!="__init__.py"):
            Mission = importlib.import_module(file.split(".py")[0])
            try:
                Mission = importlib.import_module(file.split(".py")[0])
                try:
                    MissionCon = Mission.ExplorationPyFile
                except AttributeError:
                    print("Unrecognised Mission File '{}'".format(file))
                    input()
                    exit()
                Options.append(Mission)
            except Exception:
                fatal("003")
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
    ChosenMission.Game(API)
if Option=="2":
    print("""
> How to install a mission.
Download a mission, and move it into the "Missions" folder.
Assuming it is valid, it will be available on the "Play Mission" menu.
""")
if Option=="3":
    print("""
> Credits
N/A
""")
