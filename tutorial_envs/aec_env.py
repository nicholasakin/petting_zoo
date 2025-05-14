"""
AEC Agent Environment Cycle
Gym-like API for MARL.

IN AEC Environments, agents act sequentially, receiving updated observations
and rewards before taking an action. Sequential games (such as chess).



"""



from pettingzoo.classic import rps_v2

env = rps_v2.env(render_mode="human")
env.reset(seed=42)

for agent in env.agent_iter():
    obs, rew, ter, tru, inf = env.last()

    if ter or tru:
        action = None
    else:
        action=env.action_space(agent).sample()

    env.step(action)
env.close()