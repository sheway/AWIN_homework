# AWIN_homework

## 聲明
此份作業是 AWINLAB 新生作業，由林璟翔完成。內容包含機器學習（Machine Learning）、深度學習（Deep Learning）、超啟發式演算法（Meta-heuristic Algorithm）三大題
## 機器學習（Machine Learning）
請至 [Kaggle](https://www.kaggle.com/iabhishekofficial/mobile-price-classification
) 下載Mobile Price 資料集，並用機器學習的方法進行「分類」。
1. 請使用python 的SciKit-Learn 套件來進行訓練。
2. 機器學習的模型請使用以下4 個：
    - 支援向量機(Support Vector Machine, SVM)
    - K-近鄰演算法(K-nearest neighbors, KNN)
    - 決策樹(Decision Tree, DT)
    - 隨機森林(Random Forest, RF)
3. 請使用混淆矩陣(Confusion matrix)分析上面這些模型在解決這個分類問題上的優劣，並說明你的看法。說明須包含以下性能指標(Performance metrics)：
    - 準確率(Accuracy)
    - 精準度(Precision)
    - 召回率(Recall)
    - F1 分數(F1-score)
    - 支持度(Support)
4. 模型訓練僅能使用訓練集(Training set)，但最後模型訓練的結果必須要針對訓練集(Training set)和測試集(Testing set)都輸出。


## 深度學習（Deep Learning）
請至 [Kaggle](https://www.kaggle.com/alxmamaev/flowers-recognition) 下載flowers 資料集，並用深度學習的方法進行「分類」。
1. 請使用Keras 的方法建立模型，各30 分。
2. 深度學習的模型請使用深度神經網路(Deep Neural Network, DNN)或者卷積神經網路(Convolutional Neural Network, CNN)，擇一即可。
3. 訓練集(Training Set)訓練完後，請針對測試集(Testing set)透過一些性能指標衡量模型的好壞，並印出測試集隨機十筆預測後的結果和正解進行比較。

## 超啟發式演算法（Meta-heuristic Algorithm）
請至該 [連結](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
) 下載P07 的測試資料，並使用以下的方法來解決0/1 背包問題(0/1 Knapsack problem)。

1. 動態規劃(Dynamic programming)。
2. 爬山演算法(Hill climbing, HC)。
3. 模擬退火演算法(Simulated annealing, SA)。

爬山與模擬退火的部份，初始解請自己隨機取，並做500 次迭代，畫出收斂圖。

![](https://i.imgur.com/T2xMM5i.png)
