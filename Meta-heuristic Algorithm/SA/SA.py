# coding=UTF-8
import math
import random
import matplotlib.pyplot as plt

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

# 以上在讀檔

    def random_pick(cur_ans_list):  #隨機取一個位置01互換
        i = random.randint(0, len(cur_ans_list) - 1)
        if cur_ans_list[i] == 0:  #如果不在背包內，就放入
            cur_ans_list[i] = 1
        else:  #如果在背包內，隨機挑一個不再背包內的東西與之互換
            while True:  
                j = random.randint(0, len(cur_ans_list) - 1)
                if cur_ans_list[j] == 0:
                    cur_ans_list[i] = 0
                    cur_ans_list[j] = 1
                    break
        return cur_ans_list

    def cal_profit(temp_list):  #計算profit
        num = 0
        for i in range(0, len(temp_list)):
            num += profits[i] * temp_list[i]
        return num

    def cal_weights(temp_list):  #計算weights
        num = 0
        for i in range(0, len(temp_list)):
            num += weights[i] * temp_list[i]
        return num

    ans_list = []  #解答list
    while True:
        ans_list = []
        for i in range(len(weights)):  #隨機放01進去
            if random.random() < 0.5:
                ans_list.append(1)
            else:
                ans_list.append(0)
        if cal_weights(ans_list) < capacity:  #若大於weights則重新取
            break

    print("初始值   ", ans_list, " ", cal_profit(ans_list))

    iteration_ans_list = []  #放每次疊代完的profit
    plot_list = []  #畫表用
    iteration_time = 500  #疊代次數
    temperature = 1.0  #初始溫度
    R_t = 0.95  #退火率

    for i in range(iteration_time):
        ran = random_pick(ans_list.copy())  #隨機挑選合法答案
        if cal_weights(ran) > capacity:  #如果weights>capacity則忽略本次解答
            continue
        elif cal_profit(ran) > cal_profit(ans_list):  #如果答案更佳，則更新
            ans_list = ran
        elif cal_profit(ran) <= cal_profit(ans_list):  #如果答案沒有更佳，則計算退火
            delta_f = cal_profit(ran) - cal_profit(ans_list)
            r = random.random()
            if r <= math.exp(delta_f / temperature) and temperature >= 0:
                ans_list = ran
                temperature = temperature * R_t

        iteration_ans_list.append(cal_profit(ans_list))
        plot_list.append(i)

    # print("疊代500次：", iteration_ans_list)
    print("ans_list ", ans_list, " ", cal_profit(ans_list))
    print("最佳解   ", OSOF, " ", cal_profit(OSOF))

    # plt.xticks([0, 100, 200, 300, 400, 500])
    # plt.yticks([1440.0, 1442.5, 1445.0, 1447.5, 1450.0, 1452.5, 1455.0, 1457.5])
    # plt.ylim([1440.0, 1460.0])
    plt.xlim([0, iteration_time])
    plt.plot(plot_list, iteration_ans_list)
    # plt.xlabel("疊代次數")
    # plt.ylabel("收斂值")
    # plt.title("模擬退火演算法")
    plt.show()



