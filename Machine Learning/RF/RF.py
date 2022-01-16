import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns


if __name__ == '__main__':
    train_data = pd.read_csv('train.csv')  #匯入訓練資料集
    test_data = pd.read_csv('test.csv')  #匯入測試資料集
    X = train_data[train_data.columns[0:-1]]  #將資料切割成無target
    Y = train_data.price_range  #target資料

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)  #將資料切割成0.8訓練，0.2測試

    rfc = RandomForestClassifier(n_estimators=150,n_jobs=-1,random_state=50, min_samples_leaf=10)  #建立模型
    rfc.fit(x_train, y_train)  #訓練模型
    y_predict = rfc.predict(x_test)  #預測x_test的資料

    print("accuracy score:", accuracy_score(y_test, y_predict))  #輸出準確率
    # print("target_names:", list(set(train_data.price_range)))
    results = list(map(str, list(set(train_data.price_range))))  #將預測型別轉成無重複
    print("report:\n", classification_report(y_test, y_predict, target_names=results))  #輸出性能指標

    #顯示Confusion matrix
    mat = confusion_matrix(y_test, y_predict)
    sns.heatmap(mat, square=True, annot=True, cbar=False)
    plt.xlabel("predicted value")
    plt.ylabel("true value")
    plt.show()
