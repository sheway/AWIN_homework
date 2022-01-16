# 決策樹(Decision Tree, DT)

## 訓練模型
藉由訓練集資料取出 80% 當作訓練資料，從 4 層訓練到 10 層，準確率如下：
- 決策樹深度為 4 層，Accuracy 為 0.815。
- 決策樹深度為 5 層，Accuracy 為 0.83。
- 決策樹深度為 6 層，Accuracy 為 0.8325。
- 決策樹深度為 7 層，Accuracy 為 0.8425。
- 決策樹深度為 8 層，Accuracy 為 0.8475。
- 決策樹深度為 9 層，Accuracy 為 0.8425。
- 決策樹深度為 10 層，Accuracy 為 0.845。

由 8 層增加到 9 層時準確率已經有下降的趨勢，雖然第 10 層仍有增加，但增加不多，由此可知已經呈現 over fitting 的情況。

觀察不同深度的決策樹的指標，在深度為 8 層的各指數平均皆為最高，可推斷由決策樹訓練該測資最高準確率為 84.75% 

### 決策樹深度為 4 層，Accuracy 為 0.815。
![](https://i.imgur.com/LnnDWmM.png)
![](https://i.imgur.com/cgr5UML.png)

### 決策樹深度為 5 層，Accuracy 為 0.83。
![](https://i.imgur.com/ACGd9yX.png)
![](https://i.imgur.com/Adxz76P.png)

### 決策樹深度為 6 層，Accuracy 為 0.8325。
![](https://i.imgur.com/VaHCaiX.png)
![](https://i.imgur.com/sD8DfFa.png)

### 決策樹深度為 7 層，Accuracy 為 0.8425。
![](https://i.imgur.com/spdYySI.png)
![](https://i.imgur.com/Q0umQOU.png)

### 決策樹深度為 8 層，Accuracy 為 0.8475。
![](https://i.imgur.com/1dxJD2Q.png)
![](https://i.imgur.com/3ZNddbr.png)

### 決策樹深度為 9 層，Accuracy 為 0.8425。
![](https://i.imgur.com/P5YvM0W.png)
![](https://i.imgur.com/8HZb3N5.png)

### 決策樹深度為 10 層，Accuracy 為 0.845。
![](https://i.imgur.com/vxjAob8.png)
![](https://i.imgur.com/Z91LUil.png)

