import numpy as np
import matplotlib.pyplot as plt

n = 0
lr = 0.10
#1.输入数据集与其对应标签
#5组输入数据
X = np.array ([[1,1,2,3],
               [1,1,4,7],
               [1,1,1,3],
               [1,1,5,3],
               [1,1,0,1]])
#标签
Y = np.array([1,1,-1,1,-1])

#2.权重的初始化
#随机生成范围在(-1,1)的权重，权重的个数与输入向量维度相同
W = (np.random.random(X.shape[1])-0.5)*2
def get_show():
    all_x = X[:, 2]
    all_y = X[:, 3]

    all_negative_x = [1,0]
    all_negative_y = [1,1]

    k = - W[2] / W[3]
    b = -(W[0] + W[1]) / W[3]

    xdata = np.linspace(0, 5)
    plt.figure()
    plt.plot(xdata,xdata*k+b,'r')
    plt.plot(all_x,all_y,'bo')
    plt.plot(all_negative_x,all_negative_y,'yo')
    plt.show()


#3.更新权重函数
def get_update():
    global X,Y,W,lr,n
    n += 1
    #输出：X与W的转置相乘，得到的结果再由阶跃函数处理
    new_output = np.sign(np.dot(X,W.T))
    #调整权重：新权重 = 旧权重 + 改变权重
    new_W = W + lr*((Y-new_output.T).dot(X))/int(X.shape[0])
    W = new_W

def main():
    for _ in range(100):
        get_update()
        new_output = np.sign(np.dot(X,W.T))
        if (new_output == Y.T).all():
            print("迭代次数：",n)
            break
    get_show()
if __name__ == "__main__":
    main()


