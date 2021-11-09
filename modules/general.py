#General
#Modules
import subprocess
import ctypes
#About
def about():
    print("QuickShell made by Aetopia.")
    print("A basic terminal made in Python.")
    print("This project was an attempt to create a basic working terminal program in Python.")
    
    
    
#Switch the terminal from QuickShell to CMD/Powershell.      
def terminal(cmd):
    if cmd=="cmd":
        print("Terminal Set => Command Prompt")
        ctypes.windll.kernel32.SetConsoleTitleW("QuickShell (Command Prompt)")
        print("")
        subprocess.run([("cmd.exe")])
        print("Terminal Set => QuickShell")

    if cmd=="powershell":
        print("Terminal Set => PowerShell")
        ctypes.windll.kernel32.SetConsoleTitleW("QuickShell (PowerShell)")
        print("")
        subprocess.run([("powershell.exe")])
        print("Terminal Set => QuickShell")
            
def chorogon():
    #I added this because I really love Miss Kobayashi's Dragon Maid.
    print("An Easter egg for Miss Kobayashi's Dragon Maid.\nOwO")
def ctt():
    subprocess.Popen(["start", 'https://dsc.gg/ctt'], shell=True)
            
