# 8-Puzzle Problem Solver: BFS vs A* Search 🧩

This repository contains two different approaches to solving the classic 8-Puzzle Problem for the Artificial Intelligence Lab. 

It demonstrates the difference between an **Uninformed Search (BFS)** and an **Informed Search (A*)**.

---

## 📘 Assignment 1: Breadth-First Search (BFS)
**Approach:** Uninformed / Blind Search

BFS algorithm bina kisi extra knowledge ke graph ko level-by-level explore karta hai. Yeh har possible rasta check karta hai jab tak goal na mil jaye.

### Key Concepts & Implementation:
*   **Data Structure:** `Queue` (FIFO - First In First Out) use hoti hai frontier ko track karne ke liye.
*   **State Representation:** Puzzle ko as a **String** represent kiya gaya hai (e.g., `"123456780"`).
*   **Starting State:** `random.seed(roll_number)` use kar ke random puzzle generate ki gayi hai.
*   **Cost Calculation:** BFS koi math ya cost calculate nahi karta, bas blindly check karta hai.

### 💡 Study Note: The "Inversions" Concept & Unsolvable States
Is assignment se ek bara mathematical concept prove hota hai:
8-Puzzle board ko agar randomly mix kiya jaye, toh total 362,880 combinations bante hain. In mein se **exactly 50% states mathematically unsolvable hoti hain**. 
Agar starting state unsolvable ho, toh BFS poori 181,440 possible valid states ko check kar ke end mein `"No solution found"` print karta hai. Yeh code ka error nahi, balke algorithm ka correct logical behavior hai.

---

## 📙 Assignment 2: A* Search (Manhattan Distance)
**Approach:** Informed / Smart Search

A* Search ek smart algorithm hai. Yeh blind search karne ke bajaye "Heuristics" (smart guesses) use karta hai taake sab se chota aur fast rasta dhoond sake.

### Key Concepts & Implementation:
*   **Data Structure:** `Priority Queue` (Python ka `heapq` module) use hoti hai taake hamesha lowest cost wali state pehle pop ho.
*   **State Representation:** Puzzle ko as a **List/Tuple of 9 elements** represent kiya gaya hai (e.g., `[1, 2, 3, 4, 5, 6, 7, 8, 0]`).
*   **Starting State:** Ek fixed predefined list di gayi hai: `[1, 2, 3, 4, 0, 6, 7, 5, 8]`.
*   **Cost Formula:** A* algorithm is formula par kaam karta hai: 
    $$f(n) = g(n) + h(n)$$
    *   $g(n)$ **(Actual Cost):** Start node se current node tak aane mein kitne moves lag chuke hain.
    *   $h(n)$ **(Heuristic):** "Manhattan Distance" use hota hai. Yeh har tile ka absolute distance calculate karta hai ke wo apni goal position se kitna door hai.
    *   **Formula:** `|current_row - goal_row| + |current_col - goal_col|`

---

## 📊 Quick Comparison Table

| Feature | Assignment 1 (BFS) | Assignment 2 (A* Search) |
| :--- | :--- | :--- |
| **Search Type** | Uninformed / Blind | Informed / Smart |
| **Logic** | Checks every path step-by-step. | Uses heuristics to find the optimal path. |
| **Data Structure** | Simple Queue (FIFO) | Priority Queue (`heapq`) |
| **Data Format** | String (`"123456780"`) | List/Tuple (`[1, 2, 3, 4, 5, 6, 7, 8, 0]`) |
| **Cost Formula** | None | $f(n) = g(n) + h(n)$ |
| **Heuristic Used**| None | Manhattan Distance |
| **Efficiency** | Slower, uses high memory for large states. | Much faster, optimized pathfinding. |