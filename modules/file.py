#Modules
import os
import glob
import subprocess
import shutil 

#Switch to another directory.
def cd(pattern):
    try:
        if pattern=="..":
            os.chdir(os.path.dirname(os.getcwd()))    
        else:
            os.chdir(pattern)
    except OSError as Error:
        print(str(Error))
        

#Lists all of the folders and files within the current directory.    
def list():
    print("Directory of", os.getcwd())
    print("")
    print(*glob.glob("*"), sep="\n")
    

#Open Windows Explorer within the current directory.
def opendir():
    subprocess.Popen(["explorer.exe", os.getcwd()])

#Delete File/Folder      
def delete(src):
    try:
        if os.path.isfile(src)==True:
            os.remove(src)
            print("Deleted File ->", src)
        elif os.path.isdir(src)==True:
            shutil.rmtree(src)
            print("Deleted Folder ->", src)
        else:
            print("Cannot delete the specified file/folder.")
    except OSError as Error:
        print(str(Error))
        
#Copy File/Folder
def copy(src, dst):
    try:
        if os.path.isfile(src)==True:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print("Copied", src, "->", dst)
        elif os.path.isdir(src)==True:
            shutil.copytree(src, dst)
            print("Copied", src, "->", dst)
        else:
            print("Cannot copy the specified file/folder.")
    except OSError as Error:
        print(str(Error))

# Create a Directory
def mkdir(Pattern):
    sourcedir=os.getcwd()
    try:
        os.mkdir(pattern)
        os.chdir(pattern)
        print("Directory Created ->", os.getcwd())
        os.chdir(sourcedir)
    except OSError as Error:
        print(str(Error))
