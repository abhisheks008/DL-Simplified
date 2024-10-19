## Drone-Navigation-using-Reinforcement-Learning-

# Drone Navigator

## Project Description
Drone Navigator is an advanced software solution designed to empower autonomous drones with the capability to navigate complex environments efficiently and safely using Reinforcement Learning (RL) techniques.

## Key Features
- Adaptive Navigation
- Obstacle Detection and Avoidance
- Efficient Pathfinding
- User-Friendly Interface
- Real-World Applications

## Technical Features
- Programming Language: Python
- Dependency Management: requirements.txt
- Modular Design
- Learning Mechanism

## Technologies Used

- **Python**: The primary programming language for implementing the RL algorithms.
- **TensorFlow/PyTorch**: For building and training neural networks.
- **OpenAI Gym**: For simulating the drone's environment.
- **NumPy**: For numerical operations.
- **Matplotlib**: For visualizing results and training progress.
- **ROS (Robot Operating System)** (optional): For real-world application and control.

## Installation:

1) Create a virtual python environment
python -m venv env

2) Activate the virtual environment:
.\env\Scripts\activate

3) Clone the repository:
git clone https://github.com/Panchadip-128/Drone-Navigation-using-Reinforcement-Learning-

4) Navigate to the project directory:
cd drone-navigator

5) Install the required packages:
pip install -r requirements.txt

Once you have the requirements and dependencies installed, you can train your PPO model on the DroneEnv. Here's a full example, including resetting and training the model:


import gym
import numpy as np
from stable_baselines3 import PPO

    class DroneEnv(gym.Env):
    def __init__(self):
        super(DroneEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(4)  # 0: Up, 1: Down, 2: Left, 3: Right
        self.observation_space = gym.spaces.Box(low=0, high=10, shape=(2,), dtype=np.float32)
        self.state = np.array([5, 5])  # Starting position of the drone
        self.target = np.array([8, 8])  # Target position
        self.obstacles = [np.array([6, 6]), np.array([7, 7])]  # Sample obstacles

    def reset(self):
        self.state = np.array([5, 5])
        return self.state

    def step(self, action):
        if action == 0:  # Up
            self.state[1] += 1
        elif action == 1:  # Down
            self.state[1] -= 1
        elif action == 2:  # Left
            self.state[0] -= 1
        elif action == 3:  # Right
            self.state[0] += 1

        # Check for collisions
        reward = -1
        done = False
        if any(np.array_equal(self.state, obs) for obs in self.obstacles):
            reward = -10  # Penalty for hitting an obstacle
            done = True
        elif np.array_equal(self.state, self.target):
            reward = 10  # Reward for reaching the target
            done = True

        return self.state, reward, done, {}

    def render(self):
        print(f"Drone Position: {self.state}, Target: {self.target}, Obstacles: {self.obstacles}")

Create the environment
env = DroneEnv()

Create the model
model = PPO("MlpPolicy", env, verbose=1)

Train the model for a number of timesteps
model.learn(total_timesteps=10000)

Test the trained model
obs = env.reset()
for _ in range(100):
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
        
## Explanation of Code
- Environment Class: This class creates a drone environment with actions to move in four directions, collision detection, and target reaching.

- Training: The PPO model is created with the MLP policy and trained for 10,000 timesteps.

- Testing the Model: After training, the model is tested in a loop where it predicts actions based on the current state, steps through the environment, and renders the state.

## Future Scopes:

- Parameter Tuning: Experiment with different hyperparameters for the PPO model to improve performance.
- Enhanced Environment: Add more obstacles, or features, or increase the complexity of the environment.
- Logging: Implement logging of rewards and actions to analyze the agent's performance.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
