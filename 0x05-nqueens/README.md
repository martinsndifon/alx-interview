The N-Queens problem is a classical combinatorial problem where the goal is to place N queens on an N×N chessboard in such a way that no two queens attack each other. In chess, a queen can move horizontally, vertically, or diagonally across the board. The problem requires finding all possible configurations of placing the queens on the board without any queen attacking another.

Question:
Write a program that solves the N queens problem.

Usage: nqueens N
- If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
Where N must be an integer greater or equal to 4
- If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
- If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
- One solution per line
- Format: see example
- You don’t have to print the solutions in a specific order
You are only allowed to import the sys module

Example
```bash
martins@ubuntu:~/0x05-nqueens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
martins@ubuntu:~/0x05-nqueens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
martins@ubuntu:~/0x05-nqueens$ 
```
