#Modules
import subprocess
import ctypes

#Run a program without arguments.
def run(program):
    try:
        if program.lower()=="cmd" or program.lower()=="cmd.exe" or program.lower()=="powershell" or program.lower()=="powershell.exe":
            print("Use the 'terminal' command to switch terminals.")   
        else:
            subprocess.run([str(program)])
    except OSError as Error:
        print(Error)

def execute(program, arguments):
    try:
        if program.lower()=="cmd" or program.lower()=="cmd.exe" or program.lower()=="powershell" or program.lower()=="powershell.exe":
            print("Use the 'terminal' command to switch terminals.")   
        else:
            arguments=arguments.split()
            subprocess.run([str(program)]+arguments)
    except OSError as Error:
        print(Error) 

def pwshscript(script_link):
    try:
        subprocess.run(["powershell","iex","(irm "+script_link+")"],shell=True)
        ctypes.windll.kernel32.SetConsoleTitleW("QuickShell")
    except OSError as Error:
        print(Error)

               
            
        
