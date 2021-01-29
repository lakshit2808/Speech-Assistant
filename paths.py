import os

# Device User Name
def user():
    x = os.path.join(os.path.expandvars("%userprofile%"),"Documents and Settings")
    'C:\\Users\\USERNAME'
    return x[9:16]


# Folder Location for notes
def Folder_Location():
    Path = r"C:/Users/" + user() + "/Documents"
    def listdir(dir):
        fileName = os.listdir(dir)
        return fileName
    files = listdir(Path)

    if "Python" not in files:
        os.chdir(Path)
        x = os.mkdir("Python")
        Path = Path + "/" + x + "/"      
    else:
        Path = Path + "/Python/"  
    files = listdir(Path) 
    if "Speech_Assistant" not in files:
        os.chdir(Path)
        x = os.mkdir("Speech_Assistant")
        Path = Path + "/" + x 
    else:
        Path = Path + "/Speech_Assistant/"
    files = listdir(Path)
    if "Notes" not in files:
        os.chdir(Path)
        x = os.mkdir("Notes/")
        Path = Path + x

    else:
        Path = Path + "Notes/"
    return Path




# Folder Location for SS
def SS_Location():
    Path = r"C:/Users/" + user() + "/Documents"
    def listdir(dir):
        fileName = os.listdir(dir)
        return fileName
    files = listdir(Path)

    if "Python" not in files:
        os.chdir(Path)
        x = os.mkdir("Python")
        Path = Path + "/" + x + "/"      
    else:
        Path = Path + "/Python/"  
    files = listdir(Path) 
    if "Speech_Assistant" not in files:
        os.chdir(Path)
        x = os.mkdir("Speech_Assistant")
        Path = Path + "/" + x 
    else:
        Path = Path + "/Speech_Assistant/"
    files = listdir(Path)
    if "screenshot" not in files:
        os.chdir(Path)
        x = os.mkdir("screenshot/")
        Path = Path + x

    else:
        Path = Path + "screenshot/"
    return Path