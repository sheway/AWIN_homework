import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob as gb

from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns
from sklearn.metrics import confusion_matrix
from tensorflow.keras.utils import to_categorical

#讀照片
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
train_data_path = 'D:/YZU/碩班/codes/Deep Learning/flowers'
image_class = {'daisy': 0, 'dandelion': 1, 'rose': 2, 'sunflower': 3, 'tulip': 4}
new_size = 224
X_train = []
y_train = []
print('---------------------------匯入照片---------------------------')
for folder in os.listdir(train_data_path):
    in_folder_path = train_data_path + '/' + folder + '/*.jpg'
    files = gb.glob(pathname=str(in_folder_path))
    print('在', folder, '中有', len(files), '張照片')  #抓取該資料夾中所有照片
    for file in files:
        orignal_image = cv2.imread(file)
        orignal_image = preprocess_input(orignal_image)
        image = cv2.cvtColor(orignal_image, cv2.COLOR_BGR2RGB)  #將圖片轉成bitmap
        resized_image = cv2.resize(image, (new_size, new_size))
        X_train.append(resized_image)  #bitmap型態的圖片append到list
        y_train.append(image_class[folder])  #利用image_class(dictionary)來將圖片種類(花的類別)轉成數字型態
print('------------------------共', len(X_train), '張照片------------------------')

y_train = to_categorical(y_train, 5)

#將所有照片轉成 array 型態
X_train = np.array(X_train)
y_train = np.array(y_train)

#隨機選取 10 張照片
X_train, y_train = shuffle(X_train, y_train)
X_train, data, y_train, datalabel= train_test_split(X_train, y_train, test_size=0.00231642, random_state=1)
#最後輸出圖表時，若有一個 label 的照片沒被選到會 error

print("X_train shape after shuffle:", X_train.shape)
print("data shape after shuffle:", data.shape)
print("y_train shape after shuffle:", y_train.shape)
print("datalabel shape after shuffle:", datalabel.shape)

Mobilenet = MobileNetV2(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.99)
EarlyStop = EarlyStopping(patience=10, restore_best_weights=True)
Reduce_LR = ReduceLROnPlateau(monitor='accuracy', verbose=2, factor=0.5, min_lr=0.00001)
callback = [EarlyStop, Reduce_LR]
Mobilenet.trainable = False

model = Sequential([
    Mobilenet,
    MaxPooling2D(3, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(512, activation='relu'),
    Dense(512, activation='relu'),
    Dense(5, activation='softmax', kernel_initializer='glorot_normal')
])

model.summary()

model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=["accuracy"])
history = model.fit(X_train, y_train, validation_data=(data, datalabel), epochs=100, batch_size=8,
                  callbacks=callback, verbose=1)

#以下為輸出結果
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'b', label='Training Loss')
plt.plot(epochs, val_loss, 'r', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()
plt.figure()

predictions = model.predict(data)
np.argmax(datalabel, axis=-1)
print(classification_report(datalabel, to_categorical(predictions.argmax(axis=1))))

cm = confusion_matrix(np.argmax(datalabel, axis=-1), predictions.argmax(axis=1))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu")
plt.xlabel("predicted value")
plt.ylabel("true value")
plt.show()
