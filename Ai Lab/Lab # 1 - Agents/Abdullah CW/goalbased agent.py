# SIR CODE
def agent(data, goal):
    if data in goal:
        return "goal achieved"
    else:
        return "Move toward goal"

# Inputs ki list aur Model (Memory)
maze = ["A", "B", "C"]
goal = ["B"]

# Loop ke zariye har input check karna
for inp in maze:
    res = agent(inp, goal)
    if res == "goal achieved":
        print(res) 
        break  # Yahan loop ruk jayega!
    print(res)



#     # GPT CODE
#     def agent(data, goal):
#     if data in goal:
#         return "goal achieved"
#     else:
#         return "Move toward goal"

# maze = ["A", "B", "C"]
# goal = ["B"]

# # Loop me goal milte hi break lagayein
# for inp in maze:
#     res = agent(inp, goal)
#     print(res)
    
#     if res == "goal achieved":
#         print("Stopping agent.")
#         break  # Yahan loop ruk jayega!