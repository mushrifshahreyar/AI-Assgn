from Q1 import BFS
from Q2 import A_star
from Q1 import createInput
initialState = input("Enter the input for Puzzle Ex: Input (WWWBBB ):\t")
BFS(createInput(initialState))
A_star(createInput(initialState))