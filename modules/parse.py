import sys
sys.path.insert(1, 'commands')
import file
import program
import general
import web
import help
import script

def input(command):
    #Input Parsing
    Single_CMD = True
    try:
        cmd, argument=command.split(" ",1)
        Single_CMD = False
        try:
            argument1, argument2=argument.split(" | ",1)
        except:
            pass
    except:
        cmd=command

    #File Management  
    if cmd.lower()=="cd":
        try:
            file.cd(str(argument))
        except:
            print("cd <Directory>")

    elif cmd.lower()=="ls" or cmd.lower()=="list" and Single_CMD==True:
        file.list() 

    elif cmd.lower()=="opendir" and Single_CMD==True:
        file.opendir()

    elif cmd.lower()=="copy":
        try:
            file.copy(str(argument1), str(argument2))
        except:
            print("copy <Source> | <Destination>")

    elif cmd.lower()=="delete" or cmd.lower()=="del":
        try:
            file.delete(argument)
        except:
            print("delete <File/Folder>")
            
    elif cmd.lower()=="mkdir":
        try:
            file.mkdir(argument)
        except:
            print("mkdir <Pattern>")
        
    #Execution    
    elif cmd.lower()=="run":
        try:
            program.run(argument)
        except:
            print("run <Executable>")
    elif cmd.lower()=="execute":
        try:
            program.execute(argument1, argument2)
        except:
            print("execute <Executable> | <Arguments>")
    elif cmd.lower()=="pwshscript":
        try:
            program.pwshscript(argument)
        except:
            print("pwshscript <Script URL>")            
        
    #General
    elif cmd.lower()=="help":
        try:
            help.help(argument) 
        except:
            print("---Help---")
            print("Categories:") 
            print("1. General") 
            print("2. Files")
            print("3. Web")
            print("4. Scripting")

    elif cmd.lower()=="about" and Single_CMD==True:
        general.about()

    elif cmd.lower()=="chorogon" and Single_CMD==True:
        general.chorogon()

    elif cmd.lower()=="ctt" and Single_CMD==True:
        general.ctt()

    elif cmd.lower()=="terminal":
        general.terminal(argument)    

    # Web
    elif cmd.lower()=="search" or cmd.lower()=="s":
        try:
            web.search(argument1, argument2)
        except:
            print("search <Engine> | <Query>")
            
    elif cmd.lower()=="url":
        try:
            web.url(argument)
        except:
            print("url <URL>")        

    #Scripts
    elif cmd.lower()=="script":
        script.ExecuteScript(argument)
        
    elif cmd.lower()=="debugscript":
        script.DebugScript(argument)    

    else:
        print("Invaild Syntax.")    
