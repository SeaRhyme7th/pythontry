import torch
from torch.autograd import Variable
# x = torch.rand(5,3)
# y = torch.ones(5,3)

# z = x + y
# q = x.mm(y.transpose(0,1))

# import numpy as np
# a = np.ones([5,3])
# b = torch.from_numpy(a)
# c = torch.FloatTensor(a)
# b.numpy()


# x = Variable(torch.ones(2,2), requires_grad=True)
# 读取下对应的数据集文件
dataFile = open("./1A0001.txt")
orix = []
for line in dataFile.readlines():
    line = line.strip("\n")
    orix.append(line)
dataFile.close()
print(range(len(orix)))
count = 1
x = []
y = []
z = []
reay = []
for i in range(len(orix)):
    if count > 5 :
        total = float(orix[i-4]) + float(orix[i-3]) + float(orix[i-2]) + float(orix[i-1]) + float(orix[i])
        middle =  total / 5
        # print(total)
        z.append(middle)
        if ((i+1) < len(orix)) :
            res = 1 if  float(orix[i+1]) > middle else 0
            y.append(res)
            reay.append(float(orix[i+1]))
            x.append(middle)
    count = count + 1
# print(x）
# print(len(x))
# print(len(y))
# print(len(reay))

# t = Variable(torch.linspace(0, 100).type(torch.FloatTensor))## 生成等差的数据，范围为0到100
tx = torch.tensor(x)
reaty = torch.tensor(reay)
ty = torch.tensor(y)

# print(tx)
# print(ty)
# rand = Variable(torch.randn(100)) * 10#生成一百个数据，均值为0，方差为1，正态分布，将数据乘以10
# y = x + rand

import matplotlib.pyplot as plt
# plt.figure(figsize=(10, 8))
# plt.plot(tx.data.numpy(), reaty.data.numpy(), 'o')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

a = Variable(torch.rand(1), requires_grad = True)
b = Variable(torch.rand(1), requires_grad = True)
print('Initial parameters:', [a,b])

learning_rate = 0.0001 # learning rate

for i in range(1000) :
    if (a.grad is not None) and (b.grad is not None):
        a.grad.data.zero_()
        b.grad.data.zero_()
    predictions = a.expand_as(tx) * tx + b.expand_as(tx) # expand_as 表示把 a 填充成  跟x 一样大小的矩阵
    loss = torch.mean((predictions - reaty) ** 2)
    print('loss:', loss)

    loss.backward() #求导，根据learning rate 和 梯度下降的算法得到下一个值

    a.data.add_(- learning_rate * a.grad.data)# 根据上面的求导得到a的新的值
    b.data.add_(- learning_rate * b.grad.data)# 根据上面的值得到新的b的值

x_data = tx.data.numpy()
plt.figure(figsize = (10, 7))
xplot ,= plt.plot(x_data, reaty.data.numpy(), 'o')
yplot ,= plt.plot(x_data, a.data.numpy() * x_data + b.data.numpy())
plt.xlabel('X') 
plt.ylabel('Y')
str1 = str(a.data.numpy()[0]) + 'x +' + str(b.data.numpy()[0])
plt.legend([xplot, yplot], ['Data', str1])
plt.show()
