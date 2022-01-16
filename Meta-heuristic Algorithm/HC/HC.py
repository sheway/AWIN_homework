# coding=UTF-8
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
    for i in range(len(weights)):  #隨機放01進去
            ans_list.append(random.randint(0, 1))
    while cal_weights(ans_list) > capacity:  #若大於weights則重新取
        ans_list = []
        for i in range(len(weights)):
            ans_list.append(random.randint(0, 1))

    print("初始值   ", ans_list, " ", cal_profit(ans_list))

    iteration_ans_list = []  #放每次疊代完的profit
    plot_list = []  #畫表用
    iteration_time = 500  #疊代次數

    for i in range(iteration_time+1):
        # print("第", i, "次疊代：")
        ran = random_pick(ans_list.copy())
        if cal_profit(ran) > cal_profit(ans_list) and cal_weights(ran) < capacity:  #如果profit增加且weights小於capacity就更新資料
            ans_list = ran

        iteration_ans_list.append(cal_profit(ans_list))
        plot_list.append(i)

    print("疊代500次", ans_list, " ", cal_profit(ans_list))
    print("最佳解   ", OSOF, " ", cal_profit(OSOF))

#以下為畫圖
    # plt.xticks([0, 100, 200, 300, 400, 500])
    # plt.yticks([1440.0, 1442.5, 1445.0, 1447.5, 1450.0, 1452.5, 1455.0, 1457.5])
    # plt.ylim([1440.0, 1460.0])
    # plt.xlim([0, 500])
    plt.plot(plot_list, iteration_ans_list)
    # plt.xlabel("疊代次數")
    # plt.ylabel("收斂值")
    # plt.title("模擬退火演算法")
    plt.show()


