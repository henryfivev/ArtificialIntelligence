import random
from collections import namedtuple
Transition = namedtuple(
    'Transition', ('state', 'action', 'reward', 'next_state', 'done'))


class ReplayMemory(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, batch):
        # 把经验数据存储起来
        self.memory.append(batch)
        # 如果存储数据超过了容量，删除以前经验数据
        if len(self.memory) > self.capacity:
            del self.memory[0]

    def sample(self, batch_size):
        # 对历史数据随机采样
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
