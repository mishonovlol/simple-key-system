import marshal
import zlib
import requests
from pystyle import *
import os
import time
import shutil
Write.Print(Center.XCenter("""
 /$$   /$$                            /$$$$$$                        /$$                            
| $$  /$$/                           /$$__  $$                      | $$                            
| $$ /$$/   /$$$$$$  /$$   /$$      | $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$ 
| $$$$$/   /$$__  $$| $$  | $$      |  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$
| $$  $$  | $$$$$$$$| $$  | $$       \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$
| $$\  $$ | $$_____/| $$  | $$       /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$
| $$ \  $$|  $$$$$$$|  $$$$$$$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$
|__/  \__/ \_______/ \____  $$       \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/
                     /$$  | $$                 /$$  | $$                                            
                    |  $$$$$$/                |  $$$$$$/                                            
                     \______/                  \______/                                             
              Made By mishonov#0001 
\n"""), Colors.yellow, interval=0)
name = Write.Input("Enter File Name:", Colors.yellow_to_green, interval=0.01)
keysys = Write.Input("Enter Key System Name:", Colors.orange_to_yellow, interval=0.01)
code = requests.get("https://raw.githubusercontent.com/mishonovlol/simple-key-system/main/key.py")
with open(f"{name}.py", 'w') as f:
    f.write(code.text.replace("nameing", keysys))
Write.Print("Key System Was SucessFully Built\n",Colors.white_to_green, interval=0.01)
yo = Write.Input("Would you like a tutorial y/n:", Colors.yellow_to_green, interval=0.01)
if yo == "y":
   Write.Print("Build the key system, edit the file created, input your key and then add your script where is says to add it (YOU CAN ALSO OBFUSCATE IT)\n",Colors.white_to_green, interval=0.01)
elif yo == "n":
      Write.Print("Okay\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()
      
#DONT EDIT ANYTHING
