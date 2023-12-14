def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same row
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check if there is a queen in the upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check if there is a queen in the lower diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col):
        if col == n:
            # Found a solution, add it to the result
            solutions.append([''.join(row) for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve(board, col + 1)
                board[i][col] = '.'

    solutions = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    solve(empty_board, 0)

    return solutions

# Example usage:
solutions = solve_n_queens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print("\n" + "------------------"  + "\n")
