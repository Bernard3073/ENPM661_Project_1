import numpy as np
import copy

# Test Case 1: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]

# Test Case 2: [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]

# Test Case 3: [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]

# Test Case 4: [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]

# Test Case 5: [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]



class Node:

    def __init__(self, status, parent):
        self.status = status
        self.parent = parent


def swap(ls, p1, p2):
    ls[p1], ls[p2] = ls[p2], ls[p1]


def right(p, x):
    swap(p, x, x + 1)
    return p


def left(p, x):
    swap(p, x, x - 1)
    return p


def up(p, x):
    swap(p, x, x - 4)
    return p


def down(p, x):
    swap(p, x, x + 4)
    return p

def next_state(p_now):
    # Find the Blank Tile (Search for '0')
    i = p_now.status.index(0)
    row = int(i/4)
    col = i % 4
    p_next = []
    if row != 0:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(up(origin, i), p_now))
    if col != 3:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(right(origin, i), p_now))
    if row != 3:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(down(origin, i), p_now))
    if col != 0:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(left(origin, i), p_now))
    return p_next

def check_goal(p):
    # make sure the puzzle is copy correctly
    ls = copy.deepcopy(p)
    ls.remove(0)
    flag = False
    for i in range(len(ls)-1):
        if ls[i] == i+1:
            flag = True
        else:
            flag = False
            return flag
    return flag

def main():
    puzzle = np.array([[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]])
    # Turn the array from 2d to 1d 
    puzzle = puzzle.flatten()
    puzzle = puzzle.tolist()
    # Apply BFS algorithm
    start = Node(puzzle, None)
    visited = [start]
    queue = [start]
    step = 0
    while queue:
        now = queue.pop(0)
        step += 1
        if(check_goal(now.status)):
            print("Goal!!!")
            print("# of steps: ", step)
            break
        next_Path = next_state(now)
        for neighbor in next_Path:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    
    



if __name__ == '__main__':
    main()
