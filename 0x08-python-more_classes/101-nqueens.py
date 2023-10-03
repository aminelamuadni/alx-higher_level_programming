#!/usr/bin/python3
"""A solution for the N queens problem using backtracking."""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The board represented as a 2D list.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the board (N x N).

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """
    Utilizes backtracking to solve N Queens.

    Args:
        board (list): The board represented as a 2D list.
        col (int): The current column.
        N (int): The size of the board (N x N).
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N)
            board[i][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)
