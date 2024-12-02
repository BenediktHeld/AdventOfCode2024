import sys

def FindLowestValue(List):
    indexLowest = sys.maxsize
    lowest = sys.maxsize
    for i in range(len(List)):
        if lowest > List[i]:
            lowest = List[i]
            indexLowest = i
    return indexLowest

# Dateiname
dateiname = 'Day1File.txt'

List1 = []
List2 = []

# Datei einlesen
with open(dateiname, 'r', encoding='utf-8') as datei:
    for zeile in datei:
        # Zeile in zwei Zahlen aufteilen
        zahl1, zahl2 = map(int, zeile.split())
        # Zahlen zu den Listen hinzufügen
        List1.append(zahl1)
        List2.append(zahl2)

TotalDistance = 0
for i in range(len(List1)):
    min1 = List1[FindLowestValue(List1)]
    List1.pop(FindLowestValue(List1))
    min2 = List2[FindLowestValue(List2)]
    List2.pop(FindLowestValue(List2))

    if min1 > min2:
        TotalDistance = TotalDistance + (min1-min2)
    elif min1 < min2:
        TotalDistance = TotalDistance + (min2-min1)
    elif min1 == min2:
        TotalDistance = TotalDistance
    else:
        print("Error")

print(f"Total Distance: {TotalDistance}")