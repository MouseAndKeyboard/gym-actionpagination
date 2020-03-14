from gym.envs.registration import register

register(
    id='pager-v0',
    entry_point='gym_pager.envs:pagerenv'
)