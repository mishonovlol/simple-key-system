#DONT TOUCH THIS PART
#DONT TOUCH THIS PART
#DONT TOUCH THIS PART
######################
import requests
from colorama import Fore
import http

keylink = ""
name = ""

def printname():
  input(f"\n\nPlease Enter The Key to {name}\n>> ")

def printname2():
  print(f"\nWelcome To {name}!\nPress Enter To Access...")
  
key_system = printname()
print("\n\nChecking The Key...")
key = requests.get(keylink).text
if key_system == key:
    pass
else:
    input("Key Is Incorrect, Press Enter To Exit...")
    exit()
printname2()
input()
######################
#PASTE YOUR SOURCE BELOW
#PASTE YOUR SOURCE BELOW
#PASTE YOUR SOURCE BELOW
