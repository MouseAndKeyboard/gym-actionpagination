# gym-actionpagination
Investigating whether representing actions in the environment using a pagination setup actually can work.

# How it works

1. Normal 10-armed bandit 
2. "observation space" is now a list of 5 of the arm pulls
3. "action space" is now the 5 available options plus the option to go to the next page of actions.
4. Using the "next page" action should not actually pull an arm, just update the observation space so that it exposes the other 5 arms.
5. Pulling an actual arm will return reward.
6. Paging **should** have no impact on training/reward, but idk if this will work in the real world because an agent may learn that the 0 reward from not pulling and paging is worse than just pulling. *actually on second thought this is kind of like a bandit problem within the bandit problem*