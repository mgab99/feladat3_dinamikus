#3. feladat: dinamikus programozás
#https://cses.fi/problemset/task/1745
#-1-gyel térek vissza ha nem felel meg az input

import sys

input_data = sys.stdin.read().splitlines()
rows = int(input_data[0])
inputs = list(map(int, input_data[1].split()))

def all_sum(n, inputs):
    if n < 1 or n > 100:
        return -1

    for i in inputs:
        if i < 1 or i > 1000:
            return -1

    all_sums = [0] * (sum(inputs) + 1)
    all_sums[0] = 1

    for i in inputs:
        for j in range(sum(inputs), i-1, -1):
            all_sums[j] += all_sums[j-i]

    sums = [i for i in range(sum(inputs)+1) if all_sums[i] and i != 0]
    return f'{len(sums)}\n{" ".join(map(str, sums))}'

print(all_sum(rows, inputs))
