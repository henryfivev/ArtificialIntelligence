import os
import random
import copy
import numpy as np
import torch
from pathlib import Path
from tensorboardX import SummaryWriter
from torch import nn, optim
from torch.autograd import Variable
from agent_dir.agent import Agent
from collections import namedtuple


import gym
import matplotlib
import matplotlib.pyplot as plt
import time
from collections import deque
import platform


BATCH_SIZE = 64  
LEARNING_RATE = 0.001


use_cuda = torch.cuda.is_available()
FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
device = torch.device("cuda" if use_cuda else "cpu")
Transition = namedtuple('Transition', ('state', 'action', 'reward', 'next_state', 'done'))


class QNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(QNetwork, self).__init__()
        self.layer1 = torch.nn.Sequential(
            torch.nn.Linear(input_size, hidden_size),
            # torch.nn.BatchNorm1d(hidden_size),
            torch.nn.PReLU()
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.PReLU()
        )

        self.layer3 = torch.nn.Sequential(
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.PReLU()
        )

        self.final = torch.nn.Linear(hidden_size, output_size)
  

    def forward(self, x):
        ##################
        # YOUR CODE HERE #
        ##################
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.final(x)
        return x


class ReplayBuffer:
    def __init__(self, buffer_size):
        ##################
        # YOUR CODE HERE #
        ##################
        self.buffer_size = buffer_size
        self.memory = []
        self.position = 0 

    def __len__(self):
        ##################
        # YOUR CODE HERE #
        ##################
        return len(self.memory)

    def push(self, *transition):
        ##################
        # YOUR CODE HERE #
        ##################
        # 把经验数据存储起来
        self.memory.append(*transition)
        # 如果存储数据超过了容量，删除以前经验数据
        if len(self.memory) > self.buffer_size:
            del self.memory[0]   

    def sample(self, batch_size):
        ##################
        # YOUR CODE HERE #
        ##################
        # 对历史数据随机采样
        return random.sample(self.memory, batch_size)

    def clean(self):
        ##################
        # YOUR CODE HERE #
        ##################
        pass


class AgentDQN(Agent):
    def __init__(self, env, args):
        """
        Initialize every things you need here.
        For example: building your model
        """
        super(AgentDQN, self).__init__(env)
        self.q_local = QNetwork(args.n_states, args.n_actions, hidden_dim=16).to(device)
        self.q_target = QNetwork(args.n_states, args.n_actions, hidden_dim=16).to(device)
        self.mse_loss = torch.nn.MSELoss()
        self.optim = optim.Adam(self.q_local.parameters(), lr=LEARNING_RATE)
        self.n_states = args.n_states
        self.n_actions = args.n_actions
        # 定义经验存储容量
        self.replay_memory = ReplayBuffer(10000)
    
    def init_game_setting(self):
        """

        Testing function will call this function at the begining of new game
        Put anything you want to initialize if necessary

        """
        ##################
        # YOUR CODE HERE #
        ##################
        pass

    def train(self):
        """
        Implement your training algorithm here
        """
        ##################
        # YOUR CODE HERE #
        ##################
        if len(self.replay_memory.memory) < BATCH_SIZE:
            return
        transitions = self.replay_memory.sample(BATCH_SIZE)#随机取batch_size个历史数据
        batch = Transition(*zip(*transitions))#把数据转成设置格式，方便索索引
                        
        states = torch.cat(batch.state)
        actions = torch.cat(batch.action)
        rewards = torch.cat(batch.reward)
        next_states = torch.cat(batch.next_state)
        dones = torch.cat(batch.done)
        
        # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
        # columns of actions taken. These are the actions which would've been taken
        # for each batch state according to newtork q_local (current estimate)

        Q_expected = self.q_local(states).gather(1, actions)     
        Q_targets_next = self.q_target(next_states).detach().max(1)[0] #下一步的期望
        Q_targets = rewards + (self.gamma * Q_targets_next * (1-dones))#相当于真值
        
        #self.q_local.train(mode=True)        
        self.optim.zero_grad()
        loss = self.mse_loss(Q_expected, Q_targets.unsqueeze(1))
        loss.backward()
        self.optim.step()
        pass

    def make_action(self, state, eps, test=True):
        """
        Return predicted action of your agent
        Input:observation
        Return:action
        """
        ##################
        # YOUR CODE HERE #
        ##################
        global steps_done
        sample = random.random()#产生随机数，用于和eps对比

        if test==False or sample > eps:#如果随机数大于eps，就选择使用DQN网络输出的action，否则随机选择一个动作（探索）
           with torch.no_grad():
               # t.max(1) will return largest column value of each row.
               # second column on max result is index of where max element was
               # found, so we pick action with the larger expected reward.
               return self.q_local(Variable(state).type(FloatTensor)).data.max(1)[1].view(1, 1)#选择输出结果中最大值对应的动作
        else:
           ## return LongTensor([[random.randrange(2)]])
           return torch.tensor([[random.randrange(self.n_actions)]], device=device)
          #返回动作动作区间里面的随机的一个动作
        pass

    def run(self):
        """
        Implement the interaction between agent and environment here
        """
        pass