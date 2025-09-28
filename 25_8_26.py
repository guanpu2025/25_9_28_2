

'''import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

temperature_data = pd.read_csv("C:\\Users\\Guanp\\Desktop\\temperature.CSV", names = ['Days', 'temps'])

x = temperature_data[['Days']]
y = temperature_data['temps']

line = LinearRegression()
line.fit(x, y)
w_sklearn = line.coef_[0]
b_sklearn = line.intercept_
print(f"斜率为(w):{w_sklearn:.2f}")
print(f"截距为(b):{b_sklearn:.2f}")

predict_day = 31
input_day = np.array([[predict_day]])
input_day = pd.DataFrame([[predict_day]], columns=['Days'])
predict_day_temp = line.predict(input_day)
print(f"5月31日的预测气温为{predict_day_temp[0]:.2f}")

plt.figure(figsize=(10, 6))
plt.xlabel('Day(5.x)', fontsize=12)
plt.ylabel('Temperature(℃)', fontsize=12)
plt.scatter(x, y, label='True_Temperature')
plt.scatter([predict_day], [predict_day_temp], color = 'Red',marker='*', label='Predict_Temperature')
plt.title('changchun_Temperature')
y_pre = line.predict(x)
plt.plot(x, y_pre, color = 'Green', linewidth = 3, label = 'sklrean-line')
plt.legend()
plt.show() '''

'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("C:\\Users\\Guanp\\Desktop\\temperature.CSV", names = ['Day', 'Temp'])
X = df[['Day']].values
y = df['Temp'].values

plt.figure(figsize = (10, 6))
plt.scatter(X, y, color = 'blue', alpha=0.6, label = 'Temperature')
plt.xlabel('Data(5.x)', fontsize = 12)
plt.ylabel('temperature(℃)', fontsize = 12)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.legend()
plt.show()

model_sklearn = LinearRegression()
model_sklearn.fit(X, y)

w_sklearn = model_sklearn.coef_[0]
b_sklearn = model_sklearn.intercept_
print(f" - 斜率(w):{w_sklearn:.4f}")
print(f" - 截距(w):{b_sklearn:.4f}")

day_to_predict = 31
input_day = np.arry([[day_to_predict]])
predicted_temp_sklearn = model_sklearn.predict(input_day)
print(f"\n使用 Scikit-learn 模型预测：")
print(f"  - 5月{day_to_predict}日的最高气温大约为：{predicted_temp_sklearn[0]:.2f}℃")

plt.figure(figsize=(12, 7))
plt.scatter(X, y, color = 'blue', alpha=0.6, lable = 'truly tempearture')
plt.polt(X, model_sklearn.predict(X), color = 'red', linewidth = 3, label = 'Scikit-learn')

plt.scatter(day_to_predict, predicted_temp_sklearn, color='magenta', marker='*', s = 200, zorder=5, label = f'predict{day_to_predict}temperature')

plt.title('compare', fontsize=15)
plt.xlabel('data(5.x)', fontsize=12)
plt.ylable('Temperature(℃)', fontsize=12)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.legend()
plt.show()
'''
'''import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import math

plt.rcParams["font.family"] = ["SimHei"]
data = pd.read_csv("C:\\Users\\Guanp\\Desktop\\distanceMatrix.txt", header = None, sep='\t')

plt.figure(figsize=(10, 8))
plt.scatter(x = data[1], y = data[2], c = 'red')

for i in range (len(data)):
    plt.annotate(text = data[0][i], xy = (data[1][i], data[2][i]))

plt.title = ('城市经纬度')
plt.xlabel = ('经度')
plt.ylabel = ('纬度')
plt.grid(True, linestyle = '--', alpha = 0.4)

plt.show()

way = []
for i in range (len(data)):
    way_new = []
    for j in range (len(data)):
        if(i == j):
            way_ij = 0
        else:
            way_ij = math.sqrt(pow((float(data[1][i]) - float(data[1][j])), 2) + pow((float(data[2][i]) - float(data[2][j])), 2))
        way_new.append(way_ij)
    way.append(way_new)

names = []

for i in range(len(data)):
    names.append(data[0][i])

form = pd.DataFrame(way, index=names, columns=names)

pd.set_option('display.max_rows', None)     # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列

form = form.map(lambda x:f"{x:.2f}")
print(form)'''
        


'''import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math


rcParams['font.family'] = 'Arial Unicode Ms'#设置字体

guassian_date =np.random.randn(10000)       #随机生成10000个符合正态分布的数，默认均值为0，标准差为1

Mean = guassian_date.mean()                 #获取平均值
Var = math.sqrt(guassian_date.var())        #计算标准差

plt.hist(guassian_date              #绘制直方图
         , bins=60                  #分为60个区间
         , density = True           #频率密度
         , color = 'b'              #颜色为蓝色
         , label='Histogram')       #标签

x = np.linspace((Mean - 3 * Var), (Mean + 3 * Var), 1000) #x轴的范围，均值±三个标准差
pdf = (1 / (Var * np.sqrt(2 * np.pi))) * np.exp(-(x - Mean)**2 / (2 * Var ** 2))#概率密度函数
plt.plot(x, pdf, color = 'r', label = 'Guassian PDF')     #绘制概率密度函数，颜色为红色，标签为Guassian PDF

plt.title('Guassian')               #标题
plt.xlabel('x')                     #x轴标签

plt.legend()                        #图例
plt.show()                          #显示这个图'''

'''import random
times = 100000                        #实验次数
result1 = {"True" : 0, "False" : 0}   #字典，用于保存没改答案的正确与错误次数
result2 = {"True" : 0, "False" : 0}   #字典，用于保存改了答案的正确与错误次数

for i in range(times):                  
    right = random.choice([1, 2, 3, 4])   #正确答案  
    answer = random.choice([1, 2, 3, 4])  #一开始选的答案  
    if(right == answer):                  #记录没改答案的正确与错误次数
        result1["True"] += 1
    else:
        result1["False"] += 1

    paichu = [1, 2, 3, 4]              #一个列表，用来记录哪个选项可以排除
    paichu.remove(right)               #去掉正确答案
    if(right != answer):
        paichu.remove(answer)          #如果一开始选的是错的，那么去掉一开始选的答案
    #或者这么写也行paichu = [x for x in [1, 2, 3, 4] if x != answer and x != right]
    paichu_choice = random.choice(paichu)   #现在列表paichu就是可以排除的选项了，随机选一个

    an = [x for x in [1, 2, 3, 4] if x != answer and x != paichu_choice] #可以换的选项
    new_answer = random.choice(an)       #在可以换的里面随机换一个
    if(new_answer == right):             #记录改了答案的正确与错误次数
        result2["True"] += 1
    else:
        result2["False"] += 1

#打印结果
print("如果不修改答案，正确次数为%d，正确概率为%.4f" % (result1["True"], result1["True"] / times))
print("如果修改答案，正确次数为%d，正确概率为%.4f" % (result2["True"], result2["True"] / times))'''




'''import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.stats import shapiro

def generate_data(n_samples):
    X = np.random.normal(0, 1, (n_samples, 1))
    Y = 3 * X * X + np.random.normal(0, 1, (n_samples, 1))
    return X, Y 

def generate_data_test(n_samples):
    X = np.random.normal(0, 1, (n_samples, 1))
    Y = 3 * X * X
    return X, Y

def caculate_error(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_train_p = model.predict(X_train)
    y_test_p = model.predict(X_test)

    t_error = mean_squared_error(y_train,y_train_p)
    g_error = mean_squared_error(y_test, y_test_p)
    return t_error, g_error

n_samples = 10000
n_exp = 10000
g_errors = []

for _ in tqdm(range(n_exp), desc = "Running"):
    X, y = generate_data(n_samples)
    X_test, y_test = generate_data_test(n_samples)

    t_error,g_error = caculate_error(X, X_test, y, y_test)
    g_errors.append(g_error)

plt.hist(g_errors, bins = 30, density = True, alpha = 0.6)
plt.show()

stat, p = shapiro(g_errors)
print(stat, p)'''



























