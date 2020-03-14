from gym.envs.registration import register

register(
    id=f'actionpagination-v0',
    entry_point=f'gym_actionpagination.envs:PagedBanditEnv'
)