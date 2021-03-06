import copy
import collections


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
    # Search for the row and column where the blank tile locate
    row = int(i/4)
    col = i % 4
    p_next = []
    # Provide restrictions to the moving direction of the blank tile
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
    # Trace the path
    path = []
    while now.parent is not None:
        path.append(now)
        now = now.parent
    path.reverse()
    return path

def main():
    # Read test_case from test_case.txt
    with open('test_case.txt') as f:
        lines = f.readline()
        lines.replace("[", "").replace("]", "").replace(","," ")
    test_case = []
    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            if lines[i+1].isdigit():
                test_case.append(int(lines[i]+lines[i+1]))
                i = i+2
                continue
            test_case.append(int(lines[i]))
        i = i+1

    goal = [1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,0]

    # Store the test_case in column-wise order
    puzzle = []
    for i in range(int(len(test_case)/4)):
        for j in range(i,len(test_case),4):
            puzzle.append(test_case[j])
            
    # Apply BFS algorithm
    start = Node(puzzle, None)  
    # Use Set data structure and collections.deque to improve time complexity 
    visited, queue = set([start]), collections.deque([start])
    
    while queue:
        # popleft() is more efficient than pop(0)
        now = queue.popleft()
        # When the goal is reached, break the loop
        if(now.status == goal):
            path = Path_Trace(now)
            break
        next_Path = next_state(now)
        for neighbor in next_Path:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    path.insert(0, start)
    
    # Generate nodePath.txt 
    f = open("nodePath.txt", "w+")
    for i in range(len(path)):
        for j in path[i].status:
            f.write('%d ' %j)
        f.write('\n')
    f.close()
    


if __name__ == '__main__':
    main()
