# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:03:37 2023

@author: God
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# 創建數據集
data_updated = {
    'Modulation Technique': [0, 1, 0, 1, 0, 1],
    'Frequency Range': [1000, 100000, 600, 95000, 1500, 105000],
    'Resistance to Interference': [0, 1, 0, 1, 0, 1],
    'Transmission Range': [1, 0, 1, 0, 1, 0],
    'Audio Quality': [0, 1, 0, 1, 0, 1],
    'Bandwidth': [30, 80, 30, 80, 30, 80],
    'Label': [0, 1, 0, 1, 0, 1]
}

df_updated = pd.DataFrame(data_updated)

# 分離特徵和標籤
X = df_updated.drop('Label', axis=1)
y = df_updated['Label']

# 重新分割數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 重新建立決策樹模型並訓練
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

# 使用測試集進行預測
y_pred = clf.predict(X_test)

# 計算準確率
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 計算混淆矩陣
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion)

# 計算精確度
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# 計算召回率
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

# 計算F1分數
f1 = f1_score(y_test, y_pred)
print("F1 Score:", f1)

# 創建一個新的數據點



new_data_point1 = {
    'Modulation Technique': [0],
    'Frequency Range': [8000],
    'Resistance to Interference': [1],
    'Transmission Range': [1],
    'Audio Quality': [1],
    'Bandwidth': [60]
}

new_data_point2 = {
    'Modulation Technique': [1],  # 修改 Modulation Technique 為 1
    'Frequency Range': [8000],  # 修改 Frequency Range 為 80000
    'Resistance to Interference': [1],  # 修改 Resistance to Interference 為 0
    'Transmission Range': [1],  # 修改 Transmission Range 為 0
    'Audio Quality': [1],  # 修改 Audio Quality 為 0
    'Bandwidth': [60]  # 修改 Bandwidth 為 600
}

# 將兩個新數據轉換為DataFrame
new_df1 = pd.DataFrame(new_data_point1)
new_df2 = pd.DataFrame(new_data_point2)

# 使用創建的決策樹模型進行預測
prediction1 = clf.predict(new_df1)
prediction2 = clf.predict(new_df2)

if prediction1[0] == 0:
    print("第一個預測結果是 AM")
else:
    print("第一個預測結果是 FM")

if prediction2[0] == 0:
    print("第二個預測結果是 AM")
else:
    print("第二個預測結果是 FM")