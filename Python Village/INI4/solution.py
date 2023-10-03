import sys

sys.stdin = open("rosalind_ini4.txt", "r")
sys.stdout = open("output.txt", "w")

a, b = map(int, input().split())
s = sum(i for i in range(a if a % 2 else a + 1, b + 1, 2))
print(s)
