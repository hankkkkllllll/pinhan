# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:29:25 2023

@author: God
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 示例数据集：假设您有一个包含设备状态和历史故障记录的数据集
# 请替换下面的数据集示例为您的实际数据

# 创建示例数据集
data = {
    '设备温度': [60, 65, 70, 75, 80, 85, 90, 95],
    '设备湿度': [30, 35, 40, 45, 50, 55, 60, 65],
    '故障': ['正常', '正常', '正常', '正常', '故障', '故障', '故障', '故障']
}

df = pd.DataFrame(data)

# 将故障列转换为二进制标签，1表示故障，0表示正常
df['故障'] = df['故障'].apply(lambda x: 1 if x == '故障' else 0)

# 分割特征和标签
X = df[['设备温度', '设备湿度']]
y = df['故障']

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树分类器
clf = DecisionTreeClassifier()

# 训练模型
clf.fit(X_train, y_train)

# 进行预测
y_pred = clf.predict(X_test)

# 计算分类准确度
accuracy = accuracy_score(y_test, y_pred)
print("分类准确度：", accuracy)

# 假设您有新的设备温度和湿度数据，您可以使用模型来预测设备的故障状态
new_data = pd.DataFrame({'设备温度': [70, 85], '设备湿度': [45, 60]})
predictions = clf.predict(new_data)
print("新数据的故障预测：", predictions)