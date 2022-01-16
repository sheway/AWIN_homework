# K-近鄰演算法(K-nearest neighbors, KNN)

## 訓練模型
藉由訓練集資料取出 80% 當作訓練資料，從 neighbors 為 3~6 ，parameter 為 2~4，準確率如下：
- KNN neighbors 為 3，parameter 為 2，Accuracy 為 0.905。
- KNN neighbors 為 3，parameter 為 3，Accuracy 為 0.9025。
- KNN neighbors 為 3，parameter 為 4，Accuracy 為 0.9025。
- KNN neighbors 為 4，parameter 為 2，Accuracy 為 0.9125。
- KNN neighbors 為 4，parameter 為 3，Accuracy 為 0.91。
- KNN neighbors 為 4，parameter 為 4，Accuracy 為 0.91。
- KNN neighbors 為 5，parameter 為 2，Accuracy 為 0.91。
- KNN neighbors 為 5，parameter 為 3，Accuracy 為 0.9175。
- KNN neighbors 為 5，parameter 為 4，Accuracy 為 0.92。
- KNN neighbors 為 5，parameter 為 5，Accuracy 為 0.9225。
- KNN neighbors 為 5，parameter 為 6，Accuracy 為 0.915。
- KNN neighbors 為 6，parameter 為 2，Accuracy 為 0.92。
- KNN neighbors 為 6，parameter 為 3，Accuracy 為 0.92。
- KNN neighbors 為 6，parameter 為 4，Accuracy 為 0.9175。
- KNN neighbors 為 7，parameter 為 2，Accuracy 為 0.9175。
- KNN neighbors 為 7，parameter 為 3，Accuracy 為 0.9225。
- KNN neighbors 為 7，parameter 為 4，Accuracy 為 0.9225。
- KNN neighbors 為 7，parameter 為 5，Accuracy 為 0.92。

| parameter\neighbors | 3      | 4      | 5      | 6      | 7      |
| -------------------:| ------ | ------ | ------ | ------ | ------ |
|               **2** | 0.905  | 0.9125 | 0.91   | 0.92   | 0.9175 |
|               **3** | 0.9025 | 0.91   | 0.9175 | 0.92   | **0.9225** |
|               **4** | 0.9025 | -      | 0.92   | 0.9175 | **0.9225** |
|               **5** | -      | -      | **0.9225** | -      | 0.92   |
|               **6** | -      | -      | 0.915  | -      | -      |


觀察不同變數的CNN指標，在(neighbors, neighbors) 為 (5, 5)、(7, 3)、(7, 4) 時有最高的準確率，但再比較其他指數後，(5, 5) 在其他指數得分較高。

### KNN neighbors 為 3，parameter 為 2，Accuracy 為 0.905。
![](https://i.imgur.com/yG62Mhn.png)
![](https://i.imgur.com/wyXCFXo.png)

### KNN neighbors 為 3，parameter 為 3，Accuracy 為 0.9025。
![](https://i.imgur.com/raUgZ0s.png)
![](https://i.imgur.com/oWYr8G2.png)

### KNN neighbors 為 3，parameter 為 4，Accuracy 為 0.9025。
![](https://i.imgur.com/ZE9sMH3.png)
![](https://i.imgur.com/nEZVoHR.png)

### KNN neighbors 為 4，parameter 為 2，Accuracy 為 0.9125。
![](https://i.imgur.com/SM4v7DG.png)
![](https://i.imgur.com/ErAiZ68.png)

### KNN neighbors 為 4，parameter 為 3，Accuracy 為 0.91。
![](https://i.imgur.com/DbVh7wu.png)
![](https://i.imgur.com/x2H9Spg.png)

### KNN neighbors 為 4，parameter 為 4，Accuracy 為 0.91。
![](https://i.imgur.com/KY6NXTw.png)
![](https://i.imgur.com/nTZ9iMy.png)

### KNN neighbors 為 5，parameter 為 2，Accuracy 為 0.915。
![](https://i.imgur.com/fntqeZD.png)
![](https://i.imgur.com/QULvqsX.png)

### KNN neighbors 為 5，parameter 為 3，Accuracy 為 0.9175。
![](https://i.imgur.com/JXPQnWR.png)
![](https://i.imgur.com/IzeNzDL.png)

### KNN neighbors 為 5，parameter 為 4，Accuracy 為 0.92。
![](https://i.imgur.com/KxkpYgi.png)
![](https://i.imgur.com/gx6ThnI.png)

### KNN neighbors 為 5，parameter 為 5，Accuracy 為 0.9225。
![](https://i.imgur.com/MX9LM3h.png)
![](https://i.imgur.com/JFj3RBr.png)

### KNN neighbors 為 5，parameter 為 6，Accuracy 為 0.915。
![](https://i.imgur.com/X7y20l0.png)
![](https://i.imgur.com/3ZLpWEb.png)

### KNN neighbors 為 6，parameter 為 2，Accuracy 為 0.92。
![](https://i.imgur.com/hGUGTco.png)
![](https://i.imgur.com/7SJQKAn.png)

### KNN neighbors 為 6，parameter 為 3，Accuracy 為 0.92。
![](https://i.imgur.com/6Ihy5RW.png)
![](https://i.imgur.com/4EQ8ihw.png)

### KNN neighbors 為 6，parameter 為 4，Accuracy 為 0.9175。
![](https://i.imgur.com/38RYeWG.png)
![](https://i.imgur.com/bQnbCrT.png)

### KNN neighbors 為 7，parameter 為 2，Accuracy 為 0.9175。
![](https://i.imgur.com/HvMnubz.png)
![](https://i.imgur.com/6JvNRX9.png)

### KNN neighbors 為 7，parameter 為 3，Accuracy 為 0.9225。
![](https://i.imgur.com/JSw8xv3.png)
![](https://i.imgur.com/kdSJnw5.png)

### KNN neighbors 為 7，parameter 為 4，Accuracy 為 0.9225。
![](https://i.imgur.com/FarmTP7.png)
![](https://i.imgur.com/nEitEuM.png)

### KNN neighbors 為 7，parameter 為 5，Accuracy 為 0.92。
![](https://i.imgur.com/zehPvVV.png)
![](https://i.imgur.com/CFjmwkR.png)
