import re

# Dateiname
dateiname = 'InputDay3.txt'

f = open(dateiname,"r")
text = f.read()

def extract_and_sum_mul_instructions(corrupted_memory):
    # Reguläre Ausdrücke für mul, do und don't
    mul_pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    # Initialisiere den Status
    mul_enabled = True
    total_sum = 0

    # Teile den Input in Tokens basierend auf den Mustern
    tokens = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', corrupted_memory)

    for token in tokens:
        if token is None or token.strip() == "":
            continue  # Überspringe leere oder None-Tokens

        token = token.strip()  # Entferne führende/nachfolgende Leerzeichen

        # Überprüfe auf do() Anweisung
        if re.match(do_pattern, token):
            mul_enabled = True  # Aktiviere mul Anweisungen

        # Überprüfe auf don't() Anweisung
        elif re.match(dont_pattern, token):
            mul_enabled = False  # Deaktiviere mul Anweisungen

        # Überprüfe auf mul Anweisungen
        match = re.match(mul_pattern, token)
        if match and mul_enabled:
            x, y = int(match.group(1)), int(match.group(2))
            total_sum += x * y  # Berechne das Produkt und addiere es zur Summe

    return total_sum

total_sum = extract_and_sum_mul_instructions(text)

print(total_sum)