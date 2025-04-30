# N-queen problem
def solve_n_queens(n):
    board = []
    
    def is_safe(row, col):
        for r, c in board:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                board.append((row, col))
                if solve(row + 1):
                    return True
                board.pop()
        return False

    solve(0)
    return board

solution = solve_n_queens(4)
print("Queen positions (row, col):", solution)

