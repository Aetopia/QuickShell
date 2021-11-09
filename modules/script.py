import configparser
import parse    

def ExecuteScript(Script_File):
    Index=1
    Script=configparser.ConfigParser()
    Script.read(Script_File)
    while True:
        try:
            Command=Script["Script"][str(Index)]
            Index+=1
            parse.input(Command)
        except:
            break
        
def DebugScript(Script_File):
    print("Script:", Script_File)
    Index=1
    Script=configparser.ConfigParser()
    Script.read(Script_File)
    while True:
        try:
            Command=Script["Script"][str(Index)]
            print("Executing:", Command, "\nAt Index:", "("+str(Index)+")")
            print("")
            Index+=1
            parse.input(Command)
        except:
            break
