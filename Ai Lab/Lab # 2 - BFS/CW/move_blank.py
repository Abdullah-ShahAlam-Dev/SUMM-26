def move_blank(puzzle):
    # Puzzle positions:
    # [0] [1] [2]
    # [3] [4] [5]
    # [6] [7] [8]
    blank_pos = puzzle.find("0") # Find where the blank space is
    print("Blank space is at position", blank_pos)

    # Check if we can move right (not in rightmost column)
    rightmost_positions = [2, 5, 8] # These are the far-right spots
    if blank_pos not in rightmost_positions:
        print("We can move right!")

        # Convert string to list to make changes
        puzzle_list = list(puzzle)

        # Swap blank with tile to its right
        puzzle_list[blank_pos], puzzle_list[blank_pos + 1] = puzzle_list[blank_pos + 1], puzzle_list[blank_pos]
        
        # Print the new puzzle
        print("New puzzle:")
        print(puzzle_list[:3])  # First row
        print(puzzle_list[3:6]) # Second row
        print(puzzle_list[6:])  # Third row
    else:
        print("Can't move right - we're at the edge!")

# Try it with this puzzle
puzzle = "123045786" # 0 is in the middle of first row
move_blank(puzzle)