def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def count_xmas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(1, rows - 1):  # Vermeiden Sie die Ränder
        for c in range(1, cols - 1):  # Vermeiden Sie die Ränder
            if grid[r][c] == 'A':
                # Überprüfen Sie das X-MAS-Muster
                if (grid[r - 1][c - 1] == 'M' and grid[r - 1][c + 1] == 'S' and
                        grid[r + 1][c - 1] == 'M' and grid[r + 1][c + 1] == 'S'):
                    count += 1
                # Überprüfen Sie das umgekehrte Muster
                if (grid[r - 1][c + 1] == 'M' and grid[r - 1][c - 1] == 'S' and
                        grid[r + 1][c + 1] == 'M' and grid[r + 1][c - 1] == 'S'):
                    count += 1

    return count


# Hauptausführung
filename = 'TextDay4.txt'  # Ersetzen Sie dies durch den Pfad zu Ihrer Datei
grid = read_file_to_grid(filename)
xmas_count = count_xmas(grid)
print(f"Die Anzahl der X-MAS-Vorkommen ist: {xmas_count}")



