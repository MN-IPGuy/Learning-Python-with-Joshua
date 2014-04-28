# Imports


# Functions
def CreateFile(FileName):
    try:
        FileData = open(FileName, "w+")
    except IOError:
        print("Fatal Error Creating Initial Data File\n")
        quit()
    FileData.close()

def LoadDataFile(FileName):
    print("Loading Data\n")
    try:
        FileData = open(FileName, "r")
    except IOError:
        CreateFile(FileName)
        FileData = open(FileName, "r")        
    DataLines = FileData.readlines()
    FileData.close()
    return DataLines

def GetUserInput(): 
    print ("A - Display Data Summary") 
    print ("B - Display Data from range") 
    print ("C - Display all data") 
    print ("D - Update data") 
    print ("E - Set zip code") 
    print ("F - Clear data") 
    print ("G - Quit") 
    UserInput = str.upper(input("Enter a selection[A-G] ")) 
    return UserInput

def DisplaySummary():
    print("DisplaySummary\n")

def DisplayRange():
    print("DisplayRange\n")

def DisplayAll():
    print("DisplayAll\n")

def UpdateData():
    print("Update Data\n")

def SetZip():
    print("SetZip\n")

def ClearData():
    print("ClearData\n")

# Main Routine
DataFileName = "JWC.csv"
ZipCode = "55603"
print("Initializing Joshua's Weather Collector\n")
DataList = LoadDataFile(DataFileName)
while True:
    UserInput = GetUserInput()
    if UserInput == "A":
        DisplaySummary()
    elif UserInput == "B":
        DisplayRange()
    elif UserInput == "C":
        DisplayAll()
    elif UserInput == "D":
        UpdateData()
    elif UserInput == "E":
        SetZip()
    elif UserInput == "F":
        ClearData()
    elif UserInput == "G":
        print("Exiting Program")
        quit()
    else:
        print("Invalid Input -- Try Again\n")
    PauseKey = input("Press Enter Key to Continue"\n)

