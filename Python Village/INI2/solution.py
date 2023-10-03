import sys

sys.stdin = open("rosalind_ini2.txt", "r")
sys.stdout = open("output.txt", "w")

a, b = map(int, input().split())
print(a * a + b * b)
