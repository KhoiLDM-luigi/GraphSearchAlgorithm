import numpy as np
import math
import queue
from heapdict import heapdict

def heuristic(pos, end):
    if end not in pos:
        return 
    end_x, end_y = pos[end]
    h = {}
    for item in pos:
        cur_x, cur_y = pos[item]
        h[item] = math.sqrt(math.pow(cur_x - end_x, 2) + math.pow(cur_y - end_y, 2))
    
    return h

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
    path =[]
    visited = {}
    parent = {}
    
    frontier = []
    parent[start] = start
    frontier.append(start)
    while frontier:
        cur_node = frontier.pop()
        visited[cur_node] = parent[cur_node]
        if cur_node == end: 
            break
        for i in range(len(matrix[cur_node])):
            if matrix[cur_node, i] != 0 and i not in visited:
                parent[i] = cur_node
                frontier.append(i)
            
    if end in visited:
        last_node = end
        while last_node != start:
            path.append(last_node)
            last_node = visited[last_node]
        path.append(start)
        path.reverse()    

    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    visited = {}
    path = []
    parent = {}
    
    frontier= queue.Queue()
    parent[start] = start
    frontier.put(start)
    while not frontier.empty():
        cur_node = frontier.get()
        visited[cur_node] = parent[cur_node]
        for i in range(len(matrix[cur_node])):
            if matrix[cur_node, i] != 0 and i not in visited:
                parent[i] = cur_node
                if i == end:
                    visited[i] = cur_node
                    break
                frontier.put(i)
        else:
            continue
        break
    
    if end in visited:
        last_node = end
        while last_node != start:
            path.append(last_node)
            last_node = visited[last_node]
        path.append(start)
        path.reverse()
    
    return visited, path



def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    visit = {}
    path = []
    parent = {}

    frontier= heapdict()
    parent[start] = start
    frontier[str(start)] = 0
    while frontier:
        str_cur_node, cur_weight = frontier.popitem() 
        cur_node = int(str_cur_node)
        visit[cur_node] = parent[cur_node]
        if cur_node == end:
            break
        for i in range(len(matrix[cur_node])):
            node = matrix[cur_node, i]
            weight = matrix[cur_node, i] + cur_weight
            if node != 0:
                if (i in visit or i in frontier):
                    if i in frontier and frontier[i] > weight:
                        parent[i] = cur_node
                        if (i in visit):
                            visit[i] = cur_node
                        frontier[str(i)] =  weight
                else:
                    parent[i] = cur_node
                    frontier[str(i)] = weight
    if end in visit:
        last_node = end
        while last_node != start:
            path.append(last_node)
            last_node = visit[last_node]
        
        path.append(start)
        path.reverse()
    
    return visit, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """ 
    # TODO: 
    visited = {}
    path = []
    parent = {}

    frontier= heapdict()
    parent[start] = start
    frontier[str(start)] = 0
    while frontier:
        str_cur_node, cur_f = frontier.popitem() 
        cur_node = int(str_cur_node)
        visited[cur_node] = parent[cur_node]
        if cur_node == end:
            break
        for i in range(len(matrix[cur_node])):
            node = matrix[cur_node, i]
            f = matrix[cur_node, i]
            if node != 0:
                if (i in visited or i in frontier):
                    if i in frontier and frontier[i] > f:
                        parent[i] = cur_node
                        if (i in visited):
                            visited[i] = cur_node
                        frontier[str(i)] =  f
                else:
                    parent[i] = cur_node
                    frontier[str(i)] = f
    if end in visited:
        last_node = end
        while last_node != start:
            path.append(last_node)
            last_node = visited[last_node]
        
        path.append(start)
        path.reverse()
    
    return visited, path
def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    visited = {}
    path = []
    parent = {}
    #heuristic list
    h = heuristic(pos, end)

    frontier= heapdict()
    parent[start] = start
    frontier[str(start)] = 0
    while frontier:
        str_cur_node, cur_f = frontier.popitem() 
        cur_node = int(str_cur_node)
        visited[cur_node] = parent[cur_node]
        if cur_node == end:
            break
        for i in range(len(matrix[cur_node])):
            node = matrix[cur_node, i]
            f = matrix[cur_node, i] + cur_f + h[i]
            if node != 0:
                if (i in visited or i in frontier):
                    if i in frontier and frontier[i] > f:
                        parent[i] = cur_node
                        if (i in visited):
                            visited[i] = cur_node
                        frontier[str(i)] =  f
                else:
                    parent[i] = cur_node
                    frontier[str(i)] = f
    if end in visited:
        last_node = end
        while last_node != start:
            path.append(last_node)
            last_node = visited[last_node]
        
        path.append(start)
        path.reverse()
    
    return visited, path