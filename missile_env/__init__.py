from gym.envs.registration import register


register(
    id='missile-env-v0',
    entry_point='missile_env.envs:MissileEnv_0'
)

