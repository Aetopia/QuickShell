#Modules
import os
import sys
sys.path.insert(1, 'modules')
import parse
import ctypes
#Initialization
ctypes.windll.kernel32.SetConsoleTitleW("QuickShell")
print("QuickShell")
print("A basic terminal made in Python.")

#Main
while True:
    ctypes.windll.kernel32.SetConsoleTitleW("QuickShell")
    #Input
    print("")
    print("Path:", os.getcwd())
    command=input("Command > ")
    if command.lower()=="exit":
        break
    else:
        parse.input(command)
    
       
