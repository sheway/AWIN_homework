# 機械學習
注：各模型使用 train_test_split 來分割資料時所使用的 random_state 皆為 1。
## 名詞解釋
- Accuracy(準確率)：預測正確的sample占所有sample的比例，表示了一個分類器的區分能力。
- precision(精確率)：預測值為True情況下真實值仍為True所佔的比例。
- Recall(召回率)：真實值為True的情況下預測值仍為True所佔的比例。
- F1-score(F1 分數)：為精確值和召回率的調和均值，是一種用來評估模型穩健程度的標準，其反應的是再提高召回率的同時是不是有維持一定的準確率，數值越大越好。
- Support(支持度)：訓練資料有多少可以使用
 
## 各模型比較
- 最佳準確率
    - SVM：0.9725
    - ![](https://i.imgur.com/E8n5UTr.png)
    - KNN：0.9225
    - ![](https://i.imgur.com/MX9LM3h.png)
    - DT：0.8475
    - ![](https://i.imgur.com/1dxJD2Q.png)
    - RF：0.86
    - ![](https://i.imgur.com/r90ul31.png)
