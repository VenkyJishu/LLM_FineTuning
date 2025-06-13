import random

# Initialize learning
actions = ['sit', 'bark']
rewards = {'sit': 1, 'bark': -1}  # sit is good, bark is bad
dog_memory = {'sit': 0, 'bark': 0}

# Training loop
for i in range(4):
    # Dog randomly tries an action
    action = random.choice(actions)
    
    # Get reward
    reward = rewards[action]
    
    # Learn: update memory
    dog_memory[action] += reward
    
    print(f"Round {i+1}: Dog did '{action}', got reward {reward}.")
    print("Memory now:", dog_memory)
