def help(query):
    if query.lower()=="general":
        print("help: Gives a list of usable QuickShell commands.")
        print("about: Information on QuickShell.")
        print("terminal <CMD/PowerShell>: Switch the terminal from QuickShell to CMD/PowerShell.")
        print("run <Program>: Run a program without arguments.")
        print("execute <Program> | <Arguments>: Run a program with arguments")
        print("pwshscript <Script Link>: Execute a PowerShell script via a link.")

    elif query.lower()=="files":  
        print("cd <Directory>: Changes the working file directory.")
        print("ls/list: Lists files and folders present within the current directory.")
        print("opendir: Opens File Explorer in the current directory.")
        print("delete <File/Folder>: Deletes the specified file/folder.")
        print("copy <Source> | <Destination>: Copies a file/folder to the specified destination.")   
        
    elif query.lower()=="web":    
        print("search <Engine> | <Query>: Search up for something on the internet.\nSearch Engines: Google/DuckDuckGo/DuckDuckGoLite/QWant/Brave\nMiscellaneous Search Engines: Wikipedia/Emoji (Emojipedia)")
        print("url <URL>: Open up a URL.")

    elif query.lower()=="scripting":
        print("script <Script File>: Execute a QuickShell Script.")
        print("debugscript <Script File>: Debug a QuickShell Script.")
         
    else:
        print("Queried category not found.")      
