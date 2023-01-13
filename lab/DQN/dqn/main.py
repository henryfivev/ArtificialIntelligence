import gym
import numpy as np
import torch
import time
import matplotlib.pyplot as plt
from collections import deque
from agent import Agent, FloatTensor
from replay_buffer import ReplayMemory, Transition
from torch.autograd import Variable


use_cuda = torch.cuda.is_available()
FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
device = torch.device("cuda" if use_cuda else "cpu")
BATCH_SIZE = 64
TAU = 0.005 # soft update of target parameters
gamma = 0.99
TARGET_UPDATE = 10
num_episodes = 800
print_every = 10
hidden_dim = 16
min_eps = 0.01
max_eps_episode = 50
RENDER_FLAG = True # 是否显示训练过程


env = gym.make('CartPole-v0')
space_dim = env.observation_space.shape[0]  # n_spaces观测空间
action_dim = env.action_space.n  # n_actions 动作空间
threshold = env.spec.reward_threshold
agent = Agent(space_dim, action_dim, hidden_dim)


def epsilon_annealing(i_epsiode, max_episode, min_eps: float):
    slope = (min_eps-1.0) / max_episode
    ret_eps = max(slope*i_epsiode + 1.0, min_eps)
    return ret_eps


def save(directory, filename):
    # 保存local和target模型，根据需要保存
    torch.save(agent.q_local.state_dict(), '%s/%s_local.pth' %
               (directory, filename))
    torch.save(agent.q_target.state_dict(), '%s/%s_target.pth' %
               (directory, filename))


def run_episode(env, agent, eps):
    # 环境初始化
    state = env.reset()
    # 初始化游戏结束标志位
    done = False
    total_reward = 0

    while not done:
        # 是否可视化
        if RENDER_FLAG:
            env.render()
        # 根据输入state输出action
        action = agent.get_action(FloatTensor(
            [state]), eps)
        # 根据action更新下一步状态和奖励
        next_state, reward, done, _ = env.step(
            action.item())
        total_reward += reward
        if done:
            reward = -1
        # 保存历史经验
        agent.replay_memory.push(
            (FloatTensor([state]),
             action,
             FloatTensor([reward]),
             FloatTensor([next_state]),
             FloatTensor([done]))
        )

        if len(agent.replay_memory) > BATCH_SIZE:
            # 更新local网络
            agent.learn(gamma)
        state = next_state
    return total_reward


def train():
    # 初始化
    scores_deque = deque(maxlen=100)
    scores_array = []
    avg_scores_array = []
    time_start = time.time()

    for i_episode in range(num_episodes):
        eps = epsilon_annealing(i_episode, max_eps_episode, min_eps)
        score = run_episode(env, agent, eps)
        # 保存score
        scores_deque.append(score)
        scores_array.append(score)
        avg_score = np.mean(scores_deque)
        avg_scores_array.append(avg_score)
        # 输出调试信息
        dt = (int)(time.time() - time_start)
        if i_episode % print_every == 0 and i_episode > 0:
            print('Episode: {:5} Score: {:5}  Avg.Score: {:.2f}, eps-greedy: {:5.2f} Time: {:02}:{:02}:{:02}'.
                  format(i_episode, score, avg_score, eps, dt // 3600, dt % 3600 // 60, dt % 60))
        # 是否解决问题
        if len(scores_deque) == scores_deque.maxlen:
            if np.mean(scores_deque) >= threshold:
                print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.
                      format(i_episode, np.mean(scores_deque)))
                break
        # 经过一定episode后使用local net更新target net网络参数
        if i_episode % TARGET_UPDATE == 0:  
            agent.q_target.load_state_dict(agent.q_local.state_dict())
    return scores_array, avg_scores_array


if __name__ == "__main__":
    scores, avg_scores = train()
    # 画历次score
    fig1, ax = plt.subplots(figsize=(8, 4))
    ax.plot(np.arange(len(scores)), scores)
    plt.show()
    # 画平均score
    fig1, ax = plt.subplots(figsize=(8, 4))
    ax.plot(np.arange(len(avg_scores)), avg_scores)
    plt.show()


"""
Episode:    10 Score:  15.0  Avg.Score: 19.64, eps-greedy:  0.80 Time: 00:00:04
Episode:    20 Score:  13.0  Avg.Score: 19.67, eps-greedy:  0.60 Time: 00:00:08
Episode:    30 Score:  14.0  Avg.Score: 18.77, eps-greedy:  0.41 Time: 00:00:12
Episode:    40 Score:  82.0  Avg.Score: 27.32, eps-greedy:  0.21 Time: 00:00:23
Episode:    50 Score: 132.0  Avg.Score: 46.10, eps-greedy:  0.01 Time: 00:00:48
Episode:    60 Score: 141.0  Avg.Score: 64.87, eps-greedy:  0.01 Time: 00:01:21
Episode:    70 Score: 162.0  Avg.Score: 76.44, eps-greedy:  0.01 Time: 00:01:51
Episode:    80 Score: 179.0  Avg.Score: 89.06, eps-greedy:  0.01 Time: 00:02:27
Episode:    90 Score: 172.0  Avg.Score: 98.86, eps-greedy:  0.01 Time: 00:03:03
Episode:   100 Score: 144.0  Avg.Score: 105.20, eps-greedy:  0.01 Time: 00:03:34
Episode:   110 Score: 143.0  Avg.Score: 117.90, eps-greedy:  0.01 Time: 00:04:04
Episode:   220 Score: 162.0  Avg.Score: 185.14, eps-greedy:  0.01 Time: 00:10:49
Episode:   230 Score: 200.0  Avg.Score: 191.43, eps-greedy:  0.01 Time: 00:11:27

Environment solved in 233 episodes!    Average Score: 195.05
"""
