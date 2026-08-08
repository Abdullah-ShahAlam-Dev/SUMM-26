# SIR CODE
def agent(paths):
    best=min(paths, key = paths.get)
    return best

# Simple path dictionary (Node: Cost)
paths = {
    "A": 5,
    "B": 3,
    "C": 8,
    "D": 2,
    "E": 0  # Goal node (cost 0)
}
res=agent(paths)
print ("Best paths:"+res)
