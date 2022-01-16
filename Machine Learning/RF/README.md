# 隨機森林(Random Forest, RF)

## 訓練模型
藉由訓練集資料取出 80% 當作訓練資料，RF 的 random_state 固定為 50，從 n_estimators=100 到 300，min_samples_leaf=10 到 30，準確率如下：

- RF 的 n_estimators=100，min_samples_leaf=10，Accuracy 為 0.84。
- RF 的 n_estimators=100，min_samples_leaf=15，Accuracy 為 0.845。
- RF 的 n_estimators=100，min_samples_leaf=20，Accuracy 為 0.8275。
- RF 的 n_estimators=150，min_samples_leaf=10，Accuracy 為 0.86。
- RF 的 n_estimators=150，min_samples_leaf=15，Accuracy 為 0.845。
- RF 的 n_estimators=200，min_samples_leaf=10，Accuracy 為 0.8525。
- RF 的 n_estimators=200，min_samples_leaf=15，Accuracy 為 0.845。

| min_samples_leaf \ n_estimators | 100    | 150    | 200    |
| -------------------------------:| ------ | ------ | ------ |
|                          **10** | 0.84   | 0.86   | 0.8525 |
|                          **15** | 0.845  | 0.845  | 0.845  |
|                          **20** | 0.8275 | -      | -      |

觀察不同變數的RF指標，在(min_samples_leaf, n_estimators) 為 (150, 15) 時有最高的準確率。


### RF 的 n_estimators=100，min_samples_leaf=10，Accuracy 為 0.84。
![](https://i.imgur.com/g9nXeIQ.png)
![](https://i.imgur.com/rbmHtJI.png)

### RF 的 n_estimators=100，min_samples_leaf=15，Accuracy 為 0.845。
![](https://i.imgur.com/fBu9L3w.png)
![](https://i.imgur.com/AdEVHpF.png)

### RF 的 n_estimators=100，min_samples_leaf=20，Accuracy 為 0.8275。
![](https://i.imgur.com/VOttpr5.png)
![](https://i.imgur.com/sqXqDTd.png)

### RF 的 n_estimators=150，min_samples_leaf=10，Accuracy 為 0.86。
![](https://i.imgur.com/r90ul31.png)
![](https://i.imgur.com/Okq2lM8.png)

### RF 的 n_estimators=150，min_samples_leaf=15，Accuracy 為 0.845。
![](https://i.imgur.com/ycB9cYa.png)
![](https://i.imgur.com/LqBAXIG.png)

### RF 的 n_estimators=200，min_samples_leaf=10，Accuracy 為 0.8525。
![](https://i.imgur.com/HhZFJqY.png)
![](https://i.imgur.com/mkmcu6T.png)

### RF 的 n_estimators=200，min_samples_leaf=15，Accuracy 為 0.845。
![](https://i.imgur.com/sa2BeYs.png)
![](https://i.imgur.com/u8nXvHX.png)



