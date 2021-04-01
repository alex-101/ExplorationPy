#// API.py by Alex for ExplorationPy missions.
import time

# API.menu(List)
# Returns "string" chosen item of List.
def menu(array):
    i=1
    for v in array:
        print("{} | {}".format(i,v))
        i=i+1
    while True:
        Chosen = input(">")
        try:
            Chosen = array[int(Chosen)-1]
            break
        except Exception:
            Chosen = False
    print("\n")
    return Chosen

# API.write(String)
# Returns nil.  
def write(string,letter):
    for i in range(len(string)):
        v = string[i]
        print(v, end="")
        time.sleep(letter)
        
    print("\n") 
#
#
def say(string):
    input("> "+string)
    print("\n")