from gym.envs.registration import register

register(
    id='pagination-v0',
    entry_point='gym_pagination.envs:PaginationEnv',
)
