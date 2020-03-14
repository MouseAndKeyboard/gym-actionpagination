from gym.envs.registration import register

from .bandit import PagedBanditEnv

environments = [
    ['ActionPaginationBandit', 'v0']
]

for environment in environments:
    register(
        id=f'{environment[0]}-{environment[1]}',
        entry_point=f'gym_actionpagination:{environment[0]}'
    )