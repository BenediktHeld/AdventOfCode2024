def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def part2(data):
    rows, cols = len(data), len(data[0])
    count = 0

    _set = {"M", "S"}

    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    count += 1

    return count

# Hauptausführung
filename = 'TextDay4.txt'  # Ersetzen Sie dies durch den Pfad zu Ihrer Datei
grid = read_file_to_grid(filename)
xmas_count = part2(grid)
print(f"Die Anzahl der X-MAS-Vorkommen ist: {xmas_count}")
