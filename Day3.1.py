import re

# Dateiname
dateiname = 'InputDay3.txt'

f = open(dateiname,"r")
text = f.read()

def extract_and_sum_mul_instructions(corrupted_memory):
    # Regular expression to match valid mul instructions
    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'

    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of the results
    total_sum = sum(int(x) * int(y) for x, y in matches)

    return total_sum

total_sum = extract_and_sum_mul_instructions(text)

print(total_sum)