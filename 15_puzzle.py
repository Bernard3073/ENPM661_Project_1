import numpy as np
import copy

# Test Case 1: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]

# Test Case 2: [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]

# Test Case 3: [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]

# Test Case 4: [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]

# Test Case 5: [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
test_case_1 = np.array([[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]])
test_case_2 = np.array([[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]])
test_case_3 = np.array([[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]])
test_case_4 = np.array([[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]])
test_case_5 = np.array([[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]])

class Node:

    def __init__(self, status, parent):
        self.status = status
        self.parent = parent


def swap(ls, p1, p2):
    ls[p1], ls[p2] = ls[p2], ls[p1]


def right(p, x):
    swap(p, x, x + 4)
    return p


def left(p, x):
    swap(p, x, x - 4)
    return p


def up(p, x):
    swap(p, x, x - 1)
    return p


def down(p, x):
    swap(p, x, x + 1)
    return p

def next_state(p_now):
    # Find the Blank Tile (Search for '0')
    i = p_now.status.index(0)
    
    row = int(i/4)
    col = i % 4
    p_next = []
    if col != 0:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(up(origin, i), p_now))
    if row != 3:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(right(origin, i), p_now))
    if col != 3:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(down(origin, i), p_now))
    if row != 0:
        origin = copy.deepcopy(p_now.status)
        p_next.append(Node(left(origin, i), p_now))
    return p_next

def Path_Trace(now):
    path = []
    while now.parent is not None:
        path.append(now)
        now = now.parent
    path.reverse()
    return path

def main():
    test_case = test_case_5  
    goal = [1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,0]
    # Turn the array from 2d to 1d 
    test_case = test_case.flatten()
    test_case = test_case.tolist()
    puzzle = []
    for i in range(int(len(test_case)/4)):
        for j in range(i,len(test_case),4):
            puzzle.append(test_case[j])
    # Apply BFS algorithm
    start = Node(puzzle, None)
    visited = [start]
    queue = [start]
    while queue:
        now = queue.pop(0)
        if(now.status == goal):
            path = Path_Trace(now)
            break
        next_Path = next_state(now)
        for neighbor in next_Path:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    

    path.insert(0, start)
    
    f = open("nodePath.txt", "w+")
    for i in range(len(path)):
        f.write("Step %d.: " %(i+1))
        for j in path[i].status:
            f.write('%d ' %j)
        f.write('\n')
    f.close()
    



if __name__ == '__main__':
    main()
