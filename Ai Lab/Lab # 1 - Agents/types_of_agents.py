# Types of Agents
# 1. Simple Reflex Agent
# 2. Model-Based Reflex Agent
# 3. Goal-Based Agent
# 4. Utility-Based Agent
# 5. Learning Agent


# Simple Reflex Agent
# Motion-Based Room light controller
print("\n\n--------------------------------")
print("Simple Reflex Agent: Motion-Based Room light controller")
print("--------------------------------")
def motion_based_room_light_agent(data):
    if data:
        return "Light On"
    else:
        return "Light Off"

motions = [True, False, True, False, True]
for motion in motions:
    result = motion_based_room_light_agent(motion)
    print(result)


# Model-Based Reflex Agent
# Obstacle Avoidance Robot
print("\n\n--------------------------------")
print("Model-Based Reflex Agent: Obstacle Avoidance Robot")
print("--------------------------------")
def obstacle_avoidance_robot_agent(data, model):
    if data in model:
        return "Avoid Obstacle"
    else:
        return "Move Forward"

obstacles = ["chair", "table", "wall", "door", "window"]
model = ["chair", "table", "wall"]
for obstacle in obstacles:
    result = obstacle_avoidance_robot_agent(obstacle, model)
    print(result)


# Goal-Based Agent
# Maze Solver Robot
print("\n\n--------------------------------")
print("Goal-Based Agent: Maze Solver Robot")
print("--------------------------------")
def maze_solver_robot_agent(data, goal):
    if data == goal:
        return "Reached Goal"
    else:
        return "Move Forward"
    
maze = ["A", "B", "C", "D", "E"]
goal = "E"
for maze in maze:
    result = maze_solver_robot_agent(maze, goal)
    print(result)


# Utility-Based Agent
# Car Safest and Fastest Route Finder
print("\n\n--------------------------------")
print("Utility-Based Agent: Car Safest and Fastest Route Finder")
print("--------------------------------")
def car_safest_and_fastest_route_finder_agent(paths):
    best_path = min(paths, key = paths.get)
    return best_path

paths = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}
result = car_safest_and_fastest_route_finder_agent(paths)
print(result)


# Learning Agent
# Rule-Based Chatbot
print("\n\n--------------------------------")
print("Learning Agent: Rule-Based Chatbot")
print("--------------------------------")
known_responses = {
    "Hello": "Hello, how can I help you?",
    "Goodbye": "Goodbye, have a great day!",
    "Thank you": "You're welcome!",
}
def rule_based_chatbot_agent(data):
    if data in known_responses:
        return known_responses[data]
    else:
        new_reply = input(f"I dont know the answer to '{data}'. Please teach me: ")
        known_responses[data] = new_reply
        return new_reply

data = [
    "Hello", 
    "What is the capital of Pakistan?", 
    "Thank you", 
    "What is the capital of Pakistan?", 
    "Goodbye", 
    "What is the capital of India?"
]
for data in data:
    result = rule_based_chatbot_agent(data)
    print(f"{data}: {result}")
