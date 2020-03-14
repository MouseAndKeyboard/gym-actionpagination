from gym.envs.registration import register

register(
    id='actionpagination-v0',
    entry_point='gym_actionpagination.envs:PagedBanditEnv'
)