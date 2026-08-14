import random
# --- 1. GENERATE STARTING Fixed STATE ---
number = "0462"  
random.seed(number)
digits = list("012345678") #for make list to make a shuffle of digits
random.shuffle(digits)
# To make A String from the list of digits from the list of digits
start_state = "".join(digits) #to make a string from the list of digits using join() method without spaces

# Some another string for testing rather than random seed
start_state = "123405786" #2 move away from goal, replace new string to test with different starting state
# start_state = "208534167" #19 Moves away from goal

print("Starting State Generated:", start_state)

# --- 2. MOVEMENT FUNCTIONS ---
# Ye functions khali jagah ('0') ko alag alag directions mein move karte hain

def move_up(puzzle):
    pos = puzzle.find("0")
    if pos not in [0, 1, 2]:  # Agar top row mein nahi hai toh up move karein
        p_list = list(puzzle)
        p_list[pos], p_list[pos - 3] = p_list[pos - 3], p_list[pos]
        return "".join(p_list)
    return None

def move_down(puzzle):
    pos = puzzle.find("0")
    if pos not in [6, 7, 8]:  # Agar bottom row mein nahi hai toh down move karein
        p_list = list(puzzle)
        p_list[pos], p_list[pos + 3] = p_list[pos + 3], p_list[pos]
        return "".join(p_list)
    return None

def move_left(puzzle):
    pos = puzzle.find("0")
    if pos not in [0, 3, 6]:  # Agar left most column mein nahi hai toh left move karein
        p_list = list(puzzle)
        p_list[pos], p_list[pos - 1] = p_list[pos - 1], p_list[pos]
        return "".join(p_list)
    return None

def move_right(puzzle):
    pos = puzzle.find("0")
    if pos not in [2, 5, 8]:  # Agar right most column mein nahi hai toh right move karein
        p_list = list(puzzle)
        p_list[pos], p_list[pos + 1] = p_list[pos + 1], p_list[pos]
        return "".join(p_list)
    return None


# --- 3. GET NEXT STATES ---
# Ye function saare valid next moves return karta hai
def get_next_states(puzzle):
    states = []
    # Saari directions check karein
    for move in [move_up(puzzle), move_down(puzzle), move_left(puzzle), move_right(puzzle)]:
        if move is not None:  # Agar move possible tha
            states.append(move)
    return states


# --- 4. BFS SOLVER ---
def bfs_8_puzzle(start):
    goal_state = "123456780"
    
    # Queue mein hum poora "path" (raasta) save karenge taake baad mein print kar sakein
    queue = [[start]]
    # Set speed ke liye use kiya hai taake code foran run ho jaye
    visited = set([start])  
    states_checked = 0
    
    while queue:
        # Queue se pehla path nikalte hain
        path = queue.pop(0)
        # Path ka aakhri state hamara current state hai
        current_state = path[-1]
        states_checked += 1
        
        # Agar goal mil gaya
        if current_state == goal_state:
            return path, states_checked
            
        # Naye states generate karein aur queue mein daalein
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                # Purane path mein naya state add kar ke queue mein daal dein
                queue.append(path + [next_state])
                
    return None, states_checked

# --- 5. RUN ALGORITHM & PRINT RESULTS ---
print("\nSolving puzzle with BFS, please wait...")
solution_path, total_checked = bfs_8_puzzle(start_state)

if solution_path:
    print("\n--- RESULTS ---")
    print("1. Sequence of states from start to goal:")
    for step_num, state in enumerate(solution_path):
        # print(f"Step {step_num}: {state[:3]} | {state[3:6]} | {state[6:]}")
        print(f"Step {step_num}:")
        print([" ".join(state[:3])])
        print([" ".join(state[3:6])])
        print([" ".join(state[6:])])
        print("-" * 10) 
  


    print(f"\n2. Total number of moves taken: {len(solution_path) -1}")

    # moves means state  ki betwween ka jump
    # len(solution_path) = 20 (Total states jo queue se nikli hain)
    # # Total Moves = 20 - 1 = 19
    print(f"3. Total number of states checked before reaching the goal: {total_checked}")
else:
    print("\nNo solution found for this puzzle state.")
    print(f"Total number of states checked: {total_checked}\n\n")