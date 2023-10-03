import sys

sys.stdin = open("rosalind_ini3.txt", "r")
sys.stdout = open("output.txt", "w")

s = input()
a, b, c, d = map(int, input().split())
print(s[a : b + 1], s[c : d + 1])
