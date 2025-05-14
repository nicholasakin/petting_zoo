from pettingzoo.test import api_test, parallel_api_test
from pettingzoo.butterfly import pistonball_v6
from pettingzoo.butterfly import cooperative_pong_v5

env = cooperative_pong_v5.env(render_mode="human")

#test to see if valid api
api_test(env, num_cycles=10, verbose_progress=True)



env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample()

    env.step(action)
env.close()


