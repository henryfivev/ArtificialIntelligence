
import numpy as np
import pandas as pd


class QLearning:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # a list
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy

        ''' build q table'''
        ############################

        # YOUR IMPLEMENTATION HERE #
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        ############################

    def choose_action(self, observation):
        ''' choose action from q table '''
        ############################

        # YOUR IMPLEMENTATION HERE #
        # 判断当前state是否在已知的状态中
        self.check_state_exist(observation)
        """
        使用epsilon-greedy策略选择动作:
        epsilon的概率选择最优动作
        1-epsilon的概率随机选择动作
        """
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.loc[observation, :]
            """
            可能存在多个动作相同Q值
            则从这些动作中随机选择一个即可
            """
            action = np.random.choice(
                state_action[state_action == np.max(state_action)].index)
        else:
            action = np.random.choice(self.actions)
        return action

        ############################

    def learn(self, s, a, r, s_):
        ''' update q table '''
        ############################

        # YOUR IMPLEMENTATION HERE #
        """
        使用greedy策略
        off-policy, 从表的最大值中选
        """
        # 判断当前state是否在已知的状态中
        self.check_state_exist(s_)
        if s_ != 'terminal':
            # 未达到最终状态
            # qtarget = R + g*max(Q(S', a))
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            # 达到最终状态
            q_target = r
        # 使用贝尔曼方程更新
        self.q_table.loc[s, a] = self.q_table.loc[s, a] + \
            self.lr * (q_target - self.q_table.loc[s, a])

        ############################

    def check_state_exist(self, state):
        ''' check state '''
        ############################

        # YOUR IMPLEMENTATION HERE #
        if state not in self.q_table.index:
            """
            判断当前state是否在已知的状态中
            若不在则以该state为name生成一个ndarray数组
            插入q_table中
            """
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

        ############################
