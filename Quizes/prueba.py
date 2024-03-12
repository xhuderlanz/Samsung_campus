def is_valid_sum_puzzle(grid, row, col, num, target_sum=12):
    row_sum = sum(x for x in grid[row] if x is not None)
    col_sum = sum(grid[i][col] for i in range(len(grid)) if grid[i][col] is not None)
    
    # Verificar la suma de la fila y la columna con el número añadido
    if (row_sum + num > target_sum) or (col_sum + num > target_sum):
        return False
    
    # Verificar si el número ya está en la fila o columna
    if num in grid[row] or num in [grid[i][col] for i in range(len(grid))]:
        return False
    
    return True

def solve_puzzle(grid, available_numbers, target_sum=12):
    if not available_numbers:  # Si no hay números disponibles, se ha resuelto el puzzle
        return True

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] is None:  # Espacio vacío
                for num in available_numbers.copy():  # Hacer una copia para iterar sobre ella
                    if is_valid_sum_puzzle(grid, row, col, num, target_sum):
                        grid[row][col] = num
                        new_available_numbers = available_numbers.copy()
                        new_available_numbers.remove(num)  # Retirar el número usado de la lista
                        if solve_puzzle(grid, new_available_numbers, target_sum):
                            return True
                        grid[row][col] = None  # Backtrack
                return False  # No se encontró un número válido, por lo tanto se hace backtrack
    return True  # Se llenó el tablero correctamente

# Asumiendo que el 0 ya está colocado y no debe ser usado de nuevo
available_numbers = [3, 0, 2, 4, 7]

# Iniciar el tablero con `None` en los espacios vacíos
grid = [
    [None, None, None],
    [None, None, 8],
    [5, 6, 1]
]

# Llamar a la función de resolución
if solve_puzzle(grid, available_numbers):
    for row in grid:
        print(row)
else:
    print("No solution found")
