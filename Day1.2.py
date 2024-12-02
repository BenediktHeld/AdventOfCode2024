def AnzahlRightListNumber(List,value):
    anzahl = 0
    for i in range(len(List)):
        if List[i] == value:
            anzahl = anzahl + 1
    return anzahl

def ValueForOneIndex(List1,List2,i):
    value = List1[i]
    anzahlRight = AnzahlRightListNumber(List2, value)
    score = value * anzahlRight
    return score

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

GesamtScore = 0

for i in range(len(List1)):
    GesamtScore = GesamtScore + ValueForOneIndex(List1,List2,i)

print(GesamtScore)