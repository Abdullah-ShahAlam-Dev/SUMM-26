def agent(data):
    if data:
        return "Light on"
    else:
        return "light off"

inputs = [True, False,False, True]
for inp in inputs:
    res = agent(inp)
    print(res)