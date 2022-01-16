# coding=UTF-8
import numpy as np

if __name__ == "__main__":

    f = open('./capacity.txt', 'r')
    for line in f.readlines():
        capacity = int(line)
    print("capacity ", capacity)

    weights = []
    f = open('./weights.txt', 'r')
    for line in f.readlines():
        line = line.split('\n')[0]
        weights.append(int(line))
    print("weights  ", weights)

    profits = []
    f = open('./profits.txt', 'r')
    for line in f.readlines():
        line = line.split('\n')[0]
        profits.append(int(line))
    print("profits  ", profits)

    OSOF = []
    f = open('./optimal_selection_of_weights.txt', 'r')
    for line in f.readlines():
        line = line.split('\n')[0]
        OSOF.append(int(line))
    print("OSOF     ", OSOF)

    table = [[0 for x in range(0, capacity + 1)] for x in range(0, len(weights) + 1)]  #建立表格
    for i in range(len(weights) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i - 1] <= j:
                table[i][j] = max(profits[i-1] + table[i-1][j - weights[i-1]], table[i-1][j])  #更新表格，取更換物品與原本的最大值
            else:
                table[i][j] = table[i-1][j]  #原本的最大值
        # print(table)

    ans = 0
    for i in range(0, len(weights)):
        ans = ans + profits[i] * OSOF[i]

    print("My ans:", table[len(weights)][capacity], ", 最佳解:", ans)
