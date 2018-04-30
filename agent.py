import numpy as np
import random
#what if it goes bad?
class Agent:
    def __init__(self, state):
        self.previous_state=state
        self.action=-1
        self.learning_rate=0.8
        self.epsilon = 0.9  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.95
        self.state=state
        self.Q=np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
    def thinking(self,reward,legal):
        #checkout what was previous state
        if not legal:
            self.Q[self.previous_state,self.action] = reward
            return

        self.Q[self.previous_state,self.action] = reward + self.learning_rate * max(self.Q[self.state])
        self.state=self.action
        #print('wyliczone',self.Q[state,action])
    def act(self,state):
        if np.random.rand() <= self.epsilon:
            action=random.randrange(self.Q.size/6)
            #print('random ',action)
            self.previous_state=state
            self.action=action
            return action
        action = np.argmax(self.Q[state])
        self.previous_state=state
        #print('wymyslone action ', action, 'Qrow for our state', self.Q[state])
        self.action=action
        return action
    def new_episode(self, where):
        self.state = where
        self.previous_state=where
        self.action=where

        if self.epsilon>self.epsilon_min:
            self.epsilon*=self.epsilon_decay
