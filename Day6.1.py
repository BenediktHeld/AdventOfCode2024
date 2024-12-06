def simulate_guard_path(maze):
    # Finde die Startposition des Wächters und seine Richtung
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    direction_order = ['^', '>', 'v', '<']  # Reihenfolge der Richtungen für Drehungen
    visited_positions = set()  # Set für besuchte Positionen
    guard_position = None
    guard_direction = None

    # Maze durchlaufen, um die Startposition des Wächters zu finden
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] in directions:
                guard_position = (x, y)
                guard_direction = maze[y][x]
                visited_positions.add(guard_position)  # Startposition hinzufügen
                break
        if guard_position:
            break

    # Simuliere die Bewegung des Wächters
    while True:
        x, y = guard_position
        dx, dy = directions[guard_direction]

        # Überprüfen, ob der Wächter vor einem Hindernis steht
        if (0 <= y + dy < len(maze)) and (0 <= x + dx < len(maze[y])):  # Überprüfe die Grenzen
            if maze[y + dy][x + dx] == '#':
                # Drehe nach rechts
                current_index = direction_order.index(guard_direction)
                guard_direction = direction_order[(current_index + 1) % 4]
            else:
                # Gehe einen Schritt vorwärts
                x += dx
                y += dy
                guard_position = (x, y)
                visited_positions.add(guard_position)

                # Überprüfen, ob der Wächter den Bereich verlässt
                if y < 0 or y >= len(maze) or x < 0 or x >= len(maze[y]):
                    break
        else:
            # Wenn der Wächter die Grenzen erreicht, beende die Simulation
            break

    return len(visited_positions)

# Maze aus der Datei 'Day6.txt' einlesen
dateiname = 'Day6.txt'
with open(dateiname, 'r') as f:
    maze = f.readlines()  # Liest alle Zeilen in eine Liste

# Entferne das Zeilenende von jeder Zeile
maze = [line.rstrip('\n') for line in maze]

# Aufruf der Funktion
distinct_positions = simulate_guard_path(maze)
print(f"Der Wächter besucht {distinct_positions} verschiedene Positionen.")
