def agent(data, model):
    if data in model:
        return "avoid obstacles"
    else:
        return "Move forward"

# Inputs ki list aur Model (Memory)
inputs = ["chair", "table", "door"]
model = ["chair"]

# Loop ke zariye har input check karna
for inp in inputs:
    res = agent(inp, model)
    print(res)  # 'yes' ki jagah variable 'res' print hoga