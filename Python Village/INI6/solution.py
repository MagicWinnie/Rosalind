import sys

sys.stdin = open("rosalind_ini6.txt", "r")
sys.stdout = open("output.txt", "w")

from collections import Counter

s = input()
counter = Counter(s.split())
for k, v in counter.items():
    print(k, v)
