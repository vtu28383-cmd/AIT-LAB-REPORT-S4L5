def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solution = ["".join("Q" if col else "." for col in r) for r in board]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    print("🤖 Hello! I’m your N-Queens Chatbot.")
    n = int(input("Enter the number of queens (N): "))
    print(f"\nSolving {n}-Queens problem...\n")
    solutions = n_queens(n)
    print(f"Total solutions found: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()
