# 导入所需库
import numpy as np                                             # 用于处理数组和矩阵，科学计算的核心库
import pandas as pd                                            # 用于读取和处理像 CSV 这样的表格数据
import matplotlib.pyplot as plt                                # 用于绘图，实现数据的可视化
from sklearn.linear_model import LinearRegression              # 导入sklearn中封装好的线性回归模型
from sklearn.metrics import mean_squared_error, r2_score       # 导入评估工具，用于计算模型的性能

# 加载、准备数据
df = pd.read_csv('temperature.CSV', names=['Day', 'Temp'])     # 读入数据
X = df[['Day']].values                                         # scikit-learn 期望 X 是一个二维数组（或DataFrame），因为它假设可能有很多个特征。即使我们现在只有一个特征'Day'，也需要将它转换成二维结构。
y = df['Temp'].values

# 数据样本可视化
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.6, label='Temperature') 
plt.title('202505ChangchunDailyHighTemperature', fontsize=15)
plt.xlabel('date(5.x)', fontsize=12) 
plt.ylabel('temperature(°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5) 
plt.legend() 
plt.savefig('temperature_scatterplot.png') 

# 创建并训练模型
model_sklearn = LinearRegression()            # 创建模型
model_sklearn.fit(X, y)                       # 训练模型

# 查看模型参数
w_sklearn = model_sklearn.coef_[0]            # 系数
b_sklearn = model_sklearn.intercept_          # 截距
print(f"Scikit-learn 找到的模型参数:")
print(f"  - 斜率 (w): {w_sklearn:.4f}")
print(f"  - 截距 (b): {b_sklearn:.4f}")

# 使用 Scikit-learn 模型进行预测
# 记住，模型的 .predict() 方法也需要一个二维数组作为输入。
day_to_predict = 31
input_day = np.array([[day_to_predict]]) 
predicted_temp_sklearn = model_sklearn.predict(input_day)
print(f"\n使用 Scikit-learn 模型预测:")
print(f"  - 5月 {day_to_predict}日的最高气温大约为: {predicted_temp_sklearn[0]:.2f} °C")

# 我们将使用梯度下降法，一步步地找到最佳的 w 和 b。
# 初始化参数和超参数
w_manual = 0.0
b_manual = 0.0
learning_rate = 0.001      # 学习率：控制每一步“下山”的步子大小。步子不能太大也不能太小。
epochs = 50000             # 迭代次数：总共“下山”多少步。  
losses = []
n_samples = len(y)  
for i in range(epochs):
    y_pred = w_manual * X.flatten() + b_manual
    # 计算损失 (均方误差 MSE)，这不是必须的，但可以帮我们监控学习过程
    loss = np.mean((y - y_pred)**2)
    losses.append(loss)
    # 计算损失函数对 w 和 b 的梯度（偏导数）
    # 这是梯度下降中最关键的数学部分，它指明了参数应该向哪个方向更新。
    dw = (-2 / n_samples) * np.sum(X.flatten() * (y - y_pred))
    db = (-2 / n_samples) * np.sum(y - y_pred)
    # 根据梯度和学习率，更新参数 w 和 b
    # 我们朝着梯度的反方向移动一小步，从而让损失变小。
    w_manual = w_manual - learning_rate * dw
    b_manual = b_manual - learning_rate * db
    if (i + 1) % 10000 == 0:
        print(f"迭代 {i+1}/{epochs}, 当前损失 (MSE): {loss:.4f}")

print("\n手动梯度下降完成！找到的模型参数:")
print(f"  - 斜率 (w): {w_manual:.4f}")
print(f"  - 截距 (b): {b_manual:.4f}")

# 使用我们手动训练的模型进行预测
predicted_temp_manual = w_manual * day_to_predict + b_manual
print(f"\n使用手动实现模型预测:")
print(f"  - 5月 {day_to_predict}日的最高气温大约为: {predicted_temp_manual:.2f} °C")

# 可视化回归线
plt.figure(figsize=(12, 7))
plt.scatter(X, y, color='blue', alpha=0.6, label='truly temperature')
plt.plot(X, model_sklearn.predict(X), color='red', linewidth=3, label='Scikit-learn')
plt.plot(X, w_manual * X + b_manual, color='green', linewidth=2, linestyle='--', label='Handmade')

# 绘制预测点
plt.scatter(day_to_predict, predicted_temp_sklearn, color='magenta', marker='*', s=200, zorder=5, label=f'predict{day_to_predict}temperature')

plt.title('compare', fontsize=15)
plt.xlabel('date(5.x)', fontsize=12)
plt.ylabel('temperature(°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend() 
plt.savefig('comparison_fit_with_prediction.png')    # 保存图片

# 可视化损失函数下降过程
plt.figure(figsize=(10, 6))                          # 调整图片大小
plt.plot(range(epochs), losses, color='purple')      # 设置颜色
plt.title('loss', fontsize=15)                       # 题目
plt.xlabel('Epochs', fontsize=12)                    # 横坐标
plt.ylabel('MSE Loss', fontsize=12)                  # 纵坐标
plt.grid(True, linestyle='--', alpha=0.5)            # 设置
plt.savefig('loss_curve.png')                        # 图片保存