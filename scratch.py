import numpy as np
import random
from agent  import Agent
number_of_episodes=1000
goal_state=5
class Env:
    def __init__(self,where=0):
        self.where_I_am=where
        self.agencik = Agent(where)
        self.R=np.array([[-1,-1,-1,-1,0,-1],[-1,-1,-1,0,-1,100],[-1,-1,-1,0,-1,-1],[-1,0,0,-1,0,-1],[0,-1,-1,0,-1,100],[-1,0,-1,-1,0,100]])
    def move(self,To):
        if(self.R[self.where_I_am,To]!=-1 ):
            self.where_I_am=To
         #   self.agencik.state=To #bad place
            return True
        return False
    def refresh_surrounding(self):
        r=random.randrange(0,5)
        self.where_I_am=r
        self.agencik.new_episode(r)



#jest w miejscu nie na zewnatrz
env=Env(1)

for i in range(0,number_of_episodes):
    print('------------- episode ',i+1,' -------------------')
    print('zaczynam jestem w ',env.where_I_am)
    while env.where_I_am!=goal_state:
        #print(env.agencik.Q)
        action=env.agencik.act(env.where_I_am)
        while not env.move(action):
            env.agencik.thinking(env.R[env.where_I_am,action],False)
            #print(env.agencik.Q)
            print('stoje akcja ',action)
            action=env.agencik.act(env.where_I_am)
            #print(env.agencik.Q)
        env.agencik.thinking(env.R[env.agencik.previous_state,action],True)
        #print(env.agencik.Q)
        print('akcja ',action)
        print('jestem w ',env.where_I_am)
    env.refresh_surrounding()

print(env.agencik.Q)
print(env.R)


