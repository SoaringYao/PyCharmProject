from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torchvision import datasets, transforms

from model import *

writer = SummaryWriter('../logs')

train_data = datasets.CIFAR10('../data', train=True, transform=transforms.ToTensor(), download=True)
test_data = datasets.CIFAR10('../data', train=False, transform=transforms.ToTensor(), download=True)

train_data_size = len(train_data)
test_data_size = len(test_data)

train_data_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_data_loader = DataLoader(test_data, batch_size=64, shuffle=True)

net = Net()

if torch.cuda.is_available():
    net = net.cuda()

loss_fn = nn.CrossEntropyLoss()
if torch.cuda.is_available():
    loss_fn = loss_fn.cuda()

learning_rate = 1e-3
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

train_step = 0
test_step = 0
epoch = 100

for i in range(epoch):
    print('Epoch {}/{}'.format(i, epoch))

    for data in train_data_loader:
        imgs, labels = data

        if torch.cuda.is_available():
            imgs = imgs.cuda()
            labels = labels.cuda()

        Outputs = net(imgs)
        loss = loss_fn(Outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_step += 1

        if train_step % 100 == 0:
            print('Loss: {}'.format(loss.item()))
            writer.add_scalar('Loss/train', loss.item(), train_step)

    test_loss = 0
    with torch.no_grad():
        for data in test_data_loader:
            imgs, labels = data

            if torch.cuda.is_available():
                imgs = imgs.cuda()
                labels = labels.cuda()

            Outputs = net(imgs)
            loss = loss_fn(Outputs, labels)
            test_loss += loss.item()
            print('Loss: {}'.format(loss.item()))
    print('Test Loss: {}'.format(test_loss))
    writer.add_scalar('Test Loss', test_loss, test_step)
    test_step += 1

writer.close()
