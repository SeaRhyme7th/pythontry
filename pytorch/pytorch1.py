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

x = Variable(torch.linspace(0, 100).type(torch.FloatTensor))
rand = Variable(torch.randn(100)) * 10
y = x + rand

import matplotlib.pyplot as plt
# plt.figure(figsize=(10, 8))
# plt.plot(x.data.numpy(), y.data.numpy(), 'o')
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
    predictions = a.expand_as(x) * x + b.expand_as(x)
    loss = torch.mean((predictions - y) ** 2)
    print('loss:', loss)

    loss.backward()

    a.data.add_(- learning_rate * a.grad.data)
    b.data.add_(- learning_rate * a.grad.data)

x_data = x.data.numpy()
plt.figure(figsize = (10, 7))
xplot = plt.plot(x_data, y.data.numpy(), 'o')
yplot = plt.plot(x_data, a.data.numpy() * x_data + b.data.numpy())
plt.xlabel('X') 
plt.ylabel('Y')
str1 = str(a.data.numpy()[0]) + 'x +' + str(b.data.numpy()[0])
plt.legend([xplot, yplot], ['Data', str1])
plt.show()
