def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def print_map(map_grid):
    for row in map_grid:
        print(''.join(row))


def move_guard(map_grid, start_pos):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    visited = set()
    x, y = start_pos
    current_direction = '^'

    while True:
        visited.add((x, y))
        dx, dy = directions[current_direction]
        next_x, next_y = x + dx, y + dy

        # Überprüfen, ob die nächste Position innerhalb der Grenzen liegt und kein Hindernis ist
        if 0 <= next_x < len(map_grid) and 0 <= next_y < len(map_grid[0]) and map_grid[next_x][next_y] != '#':
            x, y = next_x, next_y
        else:
            # Drehe nach rechts
            current_direction = turn_right[current_direction]
            dx, dy = directions[current_direction]
            next_x, next_y = x + dx, y + dy

            # Überprüfen, ob die neue Richtung gültig ist
            if 0 <= next_x < len(map_grid) and 0 <= next_y < len(map_grid[0]) and map_grid[next_x][next_y] != '#':
                x, y = next_x, next_y
            else:
                break  # Der Wächter kann nicht mehr weitergehen

    return visited


def main():
    map_grid = read_map('Day6.txt')
    start_pos = None

    # Finde die Startposition des Wächters
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break

    visited_positions = move_guard(map_grid, start_pos)

    # Markiere die besuchten Positionen auf der Karte
    for x, y in visited_positions:
        if map_grid[x][y] != '#':
            map_grid[x][y] = 'X'

    print_map(map_grid)
    print(f"Distinct positions visited: {len(visited_positions)}")


if __name__ == "__main__":
    main()
