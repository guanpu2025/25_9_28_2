'''请调用sklearn中的乳腺癌数据集(breast_cancer)进行实验并撰写实验报告，要求如下：

在终端输出数据集的基本信息，并将数据集划分为训练集与测试集（建议测试集占比30%左右）；
调用sklearn中的SVC，比较采用不同的核函数的SVM（如线性核、多项式核、RBF核等）在测试集上的分类效果，
在终端输出采用不同的核函数的SVM在测试集上的准确率、分类报告，并输出混淆矩阵图像，选出效果最好的核函数；

使用2选择出来的效果最好的核函数，对以下三个数据进行预测，
在终端输出预测结果、每个类别的预测概率：
 new_samples = np.array([        
 # 样本1：类似恶性特征        
 # [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,        
 # 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,         
 # 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189],             
 #  # 样本2：类似良性特征          
 # [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766,         
 # 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023,        
 # 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259],               
 # # 样本3：边界案例        
 # [14.42, 19.77, 94.48, 642.5, 0.09752, 0.1141, 0.09388, 0.05839, 0.1879, 0.0639,        
 # 0.2895, 1.851, 2.376, 26.85, 0.008005, 0.02895, 0.03321, 0.01424, 0.01462, 0.004452,        
 # 16.33, 30.86, 109.5, 826.4, 0.1431, 0.3026, 0.3194, 0.1565, 0.2078, 0.09209]])
更改超参数C、核函数有关的超参数，观察在测试集上分类准确率，分析其对分类效果、泛化能力的影响'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

plt.rcParams["font.family"] = ["Microsoft YaHei"]

cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

print('数据集的基本信息：')
print(f'共有{X.shape[0]}个数据，其中恶性共有{np.sum(y == 0)}, 良性共有{np.sum(y == 1)}')
print(f'每个数据共有{X.shape[1]}个特征')
print('\n')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=36, stratify=y)

scaler = StandardScaler()                       #创建一个用于标准化的工具
X_train_scale = scaler.fit_transform(X_train)
#fit把训练集的各项数据的均值和标准差记录下来，transform用记下来的信息标准化训练集
X_test_scale = scaler.transform(X_test)
#这里不用fit，因为测试集的标准化参数需要与训练集一致，直接拿训练集的数据来

he = ['linear', 'poly', 'rbf']
best_he = None
best_accuracy = 0
models = {}

for he_han_shu in he:
    model = SVC(kernel=he_han_shu, probability=True, random_state=36)
    model.fit(X_train_scale, y_train)
    models[he_han_shu] = model
    y_pred = model.predict(X_test_scale)
    accuracy = accuracy_score(y_test, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_he = he_han_shu
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='d',xticklabels=cancer.target_names, yticklabels=cancer.target_names)
    plt.xlabel('预测类别')
    plt.ylabel('真实类别')
    plt.title(f'SVC{he_han_shu}核混淆矩阵的热力图')
    plt.tight_layout()
    plt.show()

print(f'最优核函数是{best_he}, 准确率为{best_accuracy:.4f}')

new_samples = np.array([
    [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
     1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
     25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189],
    [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766,
     0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023,
     15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259],
    [14.42, 19.77, 94.48, 642.5, 0.09752, 0.1141, 0.09388, 0.05839, 0.1879, 0.0639,
     0.2895, 1.851, 2.376, 26.85, 0.008005, 0.02895, 0.03321, 0.01424, 0.01462, 0.004452,
     16.33, 30.86, 109.5, 826.4, 0.1431, 0.3026, 0.3194, 0.1565, 0.2078, 0.09209]
])
news = scaler.transform(new_samples)
best_model = models[best_he]
new_samples_pred = best_model.predict(news)
probility = best_model.predict_proba(news)

print('\n新样本预测结果')
for i in range(len(new_samples)):
    print(f'样本{i}的预测结果为{cancer.target_names[new_samples_pred[i]]}')
    print(f'概率结果为：恶性{probility[i][0]:.4f}, 良性{probility[i][1]:.4f}\n')

Cs = [0.01, 0.1, 1, 10, 100]
accuracies = []

for c in Cs:
    new_model = SVC(kernel=best_he, C = c, probability=True, random_state=36)
    new_model.fit(X_train_scale, y_train)
    pred = new_model.predict(X_test_scale)
    acc = accuracy_score(y_test, pred)
    accuracies.append(acc)
    print(f'超参数C为{c}时，准确率为{acc:.4f}')

plt.figure(figsize=(8, 4))
plt.plot(Cs, accuracies, 'o-', color='blue')
plt.xscale('log')
plt.xlabel('超参数 C')
plt.ylabel('测试集准确率')
plt.title('不同C值对线性核SVM性能的影响')
plt.grid(alpha=0.3)
plt.show()
