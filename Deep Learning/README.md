# 深度學習（Deep Learning）

## 步驟
1. 將照片讀入後，轉換成 Array 型態
2. 將資料利用 train_test_split 來依照比例切割，0.00231642 為 10/4317
3. 開始建立線性堆疊模型
    - 本次共建立 10 層
    - 卷積層1
    - 池化層1
    - 卷積層2
    - 池化層2
    - Dropout層：減少過度擬合。每次訓練時要丟棄25%的神經元
    - 平坦層：將特徵值轉為一維資料以供後續的全連結層使用
    - 全連結層中的隱藏層1
    - 全連結層中的隱藏層2
    - 全連結層中的隱藏層3
    - 輸出層：有五種label：daisy, dandelion, rose, sunflower, tulip
4. 訓練模型
    - 損失函數使用交叉熵 (cross entropy)，梯度下降法使用 adam，模型的評估方式是以準確率 (accuracy) 為主
    - 擬合 model

## 預測結果
![](https://i.imgur.com/tpNXXgi.png)
![](https://i.imgur.com/LlVk1uO.png)
![](https://i.imgur.com/nRbs6G6.png)
![](https://i.imgur.com/siktt0u.png)

由於有時其中一個 label 的照片沒被選到會 error，所以嘗試將比例切割到 1000 張，發現準確率大概只有 6~7 成，所以去網路找到其他人使用 MobileNetV2 來訓練，準確率提高很多，但其中參數就沒有去了解太深。
