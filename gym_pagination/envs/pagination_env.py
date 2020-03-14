import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

class PaginationEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, p_dist, r_dist):
    if len(p_dist) != len(r_dist):
        raise ValueError("Probability and Reward distribution must be the same length")

    if min(p_dist) < 0 or max(p_dist) > 1:
        raise ValueError("All probabilities must be between 0 and 1")

    for reward in r_dist:
        if isinstance(reward, list) and reward[1] <= 0:
            raise ValueError("Standard deviation in rewards must all be greater than 0")

    self.page_no = 0
    self.pages = [[0, 1, 2, 3 , 4], [5, 6, 7, 8, 9]]
    self.pagesize = 5
    self.current_page = self.pages[self.page_no]

    self.p_dist = p_dist
    self.r_dist = r_dist

    self.n_bandits = len(p_dist)
    self.action_space = spaces.Discrete(self.pagesize + 1)
    self.observation_space = spaces.MultiDiscrete(self.pagesize)

    self._seed()

  def _seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]

  def step(self, action):
    assert self.action_space.contains(action)
    
    if action == self.pagesize:
        self.page_no = (self.page_no + 1) % len(self.pages)
        self.current_page = self.pages[self.page_no]

        reward = 0
        return self.current_page, reward, False, {'page_no': self.page_no}
    else:
        reward = 0
        done = True

        arm_to_pull = self.current_page[action]

        if np.random.uniform() < self.p_dist[arm_to_pull]:
            if not isinstance(self.r_dist[arm_to_pull], list):
                reward = self.r_dist[arm_to_pull]
            else:
                reward = np.random.normal(self.r_dist[arm_to_pull][0], self.r_dist[arm_to_pull][1])

        return self.current_page, reward, done, {'page_no': self.page_no}

  def reset(self):
    self.page_no = 0
    self.current_page = self.pages[self.page_no]
    return self.current_page
    
  def render(self, mode='human'):
    pass

  def close(self):
    pass