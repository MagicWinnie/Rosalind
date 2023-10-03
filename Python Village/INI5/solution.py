import sys

sys.stdin = open("rosalind_ini5.txt", "r")
sys.stdout = open("output.txt", "w")

for i, line in enumerate(sys.stdin):
    if i % 2:  # starting from 1
        print(line, end="")
