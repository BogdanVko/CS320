import sys

# global variable, keeping track in dfs whether a cycle was found
cyclic = False


# Don't change helper functions
#   read, dump, white, dfsInit

def read(fnm):
    """
    read file fnm containing a graph into a dictionary and return the dictionary
    each line has a nodeName followed by its adjacent nodeNames
    """
    f = open(fnm)
    gr = {}  # graph represented by dictionary
    for line in f:
        l = line.strip().split(" ")
        # ignore empty lines
        if l == ['']: continue
        # dictionary: key: nodeName  value: (color, adjacency List of names)
        gr[l[0]] = ('white', l[1:])
    return gr


def dump(gr):
    print("Input graph: nodeName (color, [adj list]) dictionary ")
    for e in gr:
        print(e, gr[e])


def white(gr):
    """
     paint all gr nodes white
    """
    for e in gr:
        gr[e] = ('white', gr[e][1])


def dfsInit(gr, root):
    """
   dfs keeps track of cycles in global cyclic
   call dfs with appropriate initial parameters
   """
    global cyclic
    cyclic = False
    visited = dfs(gr, root, [])
    return (visited, cyclic)


# Work on bfs, dfs

def bfs(gr, q):
    arr_v = [q[0][0]]
    for el in q:
        path = el[1] + 1

        for el in gr[el[0]][1]:
            if el in arr_v:

                continue
            else:
                q.append((el, path))
            arr_v.append(el)

    return q


def dfs(gr, r, visited):

    global cyclic

    if r not in visited:
        visited.append(r)
    else:
        cyclic = True
        return

    for el in gr[r][1]:
        dfs(gr, el, visited)

    return visited


def DFS(self, v):
    # Mark all the vertices as not visited
    visited = [False] * (max(self.graph) + 1)

    # Call the recursive helper function
    # to print DFS traversal
    self.DFSUtil(v, visited)


if __name__ == "__main__":
    print(sys.argv[0])  # program name
    gr = read(sys.argv[1])  # graph file name
    root = sys.argv[2]  # root node
    print("BFS")
    dump(gr)
    print("Root node:", root)
    # don't need grey for bfs
    gr[root] = ('black', gr[root][1])
    q = bfs(gr, [(root, 0)])
    print("BFS queue: (node name, distance) pairs")
    print(q)
    print("END BFS")
    print()
    white(gr)
    print("DFS")
    dump(gr)
    print("Root node", root)
    vis, cyc = dfsInit(gr, root)
    print("DFS from root visited:")
    print(vis)
    if cyc:
        print("graph with root", root, "is cyclic")
    else:
        print("graph with root", root, "is not cyclic")
    print("END DFS")
