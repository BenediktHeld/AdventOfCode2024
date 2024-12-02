# Dateiname
dateiname = 'Day2.txt'  # Ersetze dies durch den Pfad zu deiner Datei

# Array zum Speichern der Listen
array = []

# Datei einlesen
with open(dateiname, 'r', encoding='utf-8') as datei:
    for zeile in datei:
        # Versuche, die Zeile in eine Liste von Ganzzahlen umzuwandeln
        try:
            zahlen_liste = [int(zahl) for zahl in zeile.split() if zahl.isdigit()]
            # Die Liste zur Array hinzufügen
            array.append(zahlen_liste)
        except ValueError as e:
            print(f"Fehler beim Verarbeiten der Zeile: {zeile.strip()} - {e}")

def CheckArray(array):
    anzahlSave = 0
    for i in range(len(array)):
        if ProblemDampener(array[i])==True:
            anzahlSave = anzahlSave + 1
    return anzahlSave

def ProblemDampener(List):
    HelpList = List.copy()
    for i in range(len(HelpList)):
        List.pop(i)
        if CheckList(List)==True:
            return True
        List = HelpList.copy()
    return False
def CheckList(List):
    if CheckIncreasing(List)==True or CheckDecresing(List)==True:
        return True
    else:
        return False

def CheckIncreasing(List):
    ret = True
    for i in range(len(List)-1):
        if List[i] < List[i+1] and CheckDifference(List) == True:
            ret = True
        else:
            return False
    return ret

def CheckDecresing(List):
    ret = True
    for i in range(len(List)-1):
        if List[i] > List[i+1] and CheckDifference(List) == True:
            ret = True
        else:
            return False
    return ret

def CheckDifference(List):
    ret = True
    for i in range(len(List)-1):
        if List[i] > List[i+1]:
            if ((List[i]-List[i+1])>3) or ((List[i]-List[i+1])<1):
                return False
            else:
                ret = True
        elif List[i] < List[i + 1]:
            if ((List[i + 1] - List[i]) > 3) or ((List[i + 1] - List[i]) < 1):
                return False
            else:
                ret = True
        else:
            return False
    return ret

print(CheckArray(array))
