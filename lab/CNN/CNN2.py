import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable
from torch.optim import Adam
from torchvision.datasets import ImageFolder


transformations = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

batch_size = 128
number_of_labels = 5

train_set = ImageFolder('./train', transform=transformations)
train_loader = DataLoader(train_set, batch_size=batch_size,
                          shuffle=True, num_workers=0)
test_set = ImageFolder('./test', transform=transformations)
test_loader = DataLoader(test_set, batch_size=batch_size,
                         shuffle=False, num_workers=0)
classes = ('baihe', 'dangshen', 'gouqi', 'huaihua', 'jinyinhua')
print("Train images : 902")
print("Test images  : 10")
print("Batch size   :", batch_size)


class Network(nn.Module):
    def __init__(self):
        """
        Conv -> BatchNorm -> ReLU -> 
        Conv -> BatchNorm -> ReLU -> 
        MaxPool -> 
        Conv -> BatchNorm -> ReLU -> 
        Conv -> BatchNorm -> ReLU -> 
        Linear
        """
        super(Network, self).__init__()
        self.conv1 = nn.Conv2d(
            in_channels=3, out_channels=12, kernel_size=5, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(12)
        self.conv2 = nn.Conv2d(
            in_channels=12, out_channels=12, kernel_size=5, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(12)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv4 = nn.Conv2d(
            in_channels=12, out_channels=24, kernel_size=5, stride=1, padding=1)
        self.bn4 = nn.BatchNorm2d(24)
        self.conv5 = nn.Conv2d(
            in_channels=24, out_channels=24, kernel_size=5, stride=1, padding=1)
        self.bn5 = nn.BatchNorm2d(24)
        self.fc1 = nn.Linear(24*10*10, 10)

    def forward(self, input):
        output = F.relu(self.bn1(self.conv1(input)))
        output = F.relu(self.bn2(self.conv2(output)))
        output = self.pool(output)
        output = F.relu(self.bn4(self.conv4(output)))
        output = F.relu(self.bn5(self.conv5(output)))
        output = output.view(-1, 24*10*10)
        output = self.fc1(output)

        return output


model = Network()
loss_fn = nn.CrossEntropyLoss()
loss_history = []
accuracy_history = []
optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)


def testAccuracy():
    model.eval()
    accuracy = 0.0
    total = 0.0
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            accuracy += (predicted == labels).sum().item()
    accuracy = (100 * accuracy / total)
    return(accuracy)


def train_test(num_epochs):
    # train part
    best_accuracy = 0.0
    device = torch.device("cpu")
    print("run on", device)
    model.to(device)

    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader, 0):
            images = Variable(images.to(device))
            labels = Variable(labels.to(device))
            optimizer.zero_grad()# 清理上一步的梯度
            outputs = model(images)# 输入神经网络并得到输出
            loss = loss_fn(outputs, labels)# 计算loss
            loss.backward() # loss反向传播
            optimizer.step()# 更新优化器
            loss_history.append(loss.item())# 记录loss值
        accuracy = testAccuracy()
        accuracy_history.append(accuracy)
        print('epoch', epoch+1, ': accuracy is', accuracy)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
    print("Best accuracy is", best_accuracy)
    print("\n---Train finished---\n")
    # test part
    images, labels = next(iter(test_loader))
    outputs = model(images)
    _, predicted = torch.max(outputs, 1)
    print('Reallabel: ', ' '.join('%5s' % classes[labels[j]]
                            for j in range(10)))
    print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                                    for j in range(10)))


if __name__ == "__main__":
    train_test(10)
    # print(loss_history)
    # print loss and accuracy
    fig1, ax = plt.subplots(figsize=(8,4))
    ax.plot(np.arange(len(loss_history)), loss_history)
    plt.show()

    fig1, ax = plt.subplots(figsize=(8,4))
    ax.plot(np.arange(len(accuracy_history)), accuracy_history)
    plt.show()