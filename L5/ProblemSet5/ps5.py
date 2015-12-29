# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    with open(mapFilename, 'r') as f:
        mapdata = []
        for line in f:
            d = [int(x) for x in line.strip().split(' ')]
            mapdata.append(d) #list(line.strip().split(' ')))
    print mapdata
    g = WeightedDigraph()
    for data in mapdata:
        n1 = Node(data[0])
        try:
            g.addNode(n1)        
        except ValueError as e:
            print e
        n2 = Node(data[1])
        try:
            g.addNode(n2)
        except ValueError as e:
            print e
        print data
        print g.nodes
        edge = WeightedEdge(n1, n2, data[2], data[3])
        print edge
        g.addEdge(edge)
    
    return g
        
        
mitMap = load_map('mit_map.txt')
mitMap = load_map('t_map.txt')
#print isinstance(mitMap, Digraph)
#print isinstance(mitMap, WeightedDigraph)
#print mitMap.nodes
print mitMap.edges


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


def DFS(graph, start, end, maxDistOutdoors, path = [], path_list = [], totalDistOutdoors = 0):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    nstart = Node(start)
    nend = Node(end)
    path = path + [nstart]
    print 'Current dfs path:', printPath(path)
    if nstart == nend:
        if path not in path_list:
            path_list.append(path)
        return path
        #path_list.append(path)
    print 'nstart: ', nstart
    print graph.childrenOf(nstart)
    for node in graph.childrenOf(nstart):
        if node not in path: #avoid cycles
            print 'node: ', node
            edges = graph.edges[nstart]
            print 'Edges: ', edges
            print type(edges[0][1])
            #break
            #outdoors = [x[1][1] for x in edges if str(x[0]) == node.getName()] 
            for edge in edges:
                if edge[0] == node:
                    outdoors = edge[1][1]
            print 'outdoors: ', outdoors
            distance = float(outdoors)
            #totalDistOutdoors += float(outdoors[0])
            #if len(outdoors) > 1:
            #    raise ValueError
            #print 'Total Outdoors: ', totalDistOutdoors
            if totalDistOutdoors + distance <= maxDistOutdoors:
                totalDistOutdoors += distance
                print 'Total Outdoors: ', totalDistOutdoors
                newPath = DFS(graph, node, end, maxDistOutdoors, path, path_list, totalDistOutdoors)
            else:
                continue
                #if newPath != None:
                    #return newPath
                    #print 'newPath: ', len(newPath)
                    #path_list.append(newPath)
    return path_list

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    #totalOutdoors = 0
    shortestDistance = (0, [])
    #print '*'*20
    path = []
    path_list = []
    totalDistOutdoors = 0
    path_list = DFS(digraph, start, end, maxDistOutdoors, path, path_list, totalDistOutdoors)
    print path_list
    if not path_list:
        raise ValueError
    for path in path_list:
        totalDistance = 0
        for i in range(len(path) - 1):
            #print 'path: ', path
            edges = digraph.edges[path[i]]
            #print edges
            for edge in edges:
                #print edge[0], path[i + 1]
                if edge[0].getName() == path[i + 1].getName():
                    #print edge[1][0]
                    totalDistance += int(edge[1][0])
                    #print totalDistance
        if totalDistance <= maxTotalDist and (shortestDistance[0] == 0 or totalDistance < shortestDistance[0]):
            shortestDistance = (totalDistance, path)
    print shortestDistance
    if shortestDistance[0] > 0:
        return [x.getName() for x in shortestDistance[1]]
    else:
        raise ValueError                
            
            
            

    #print digraph.edges[nstart]
    #for edges in digraph.edges[nstart]:
    #    
    #    print edges
    #for node in digraph.childrenOf(nstart):
    #    print node
    #    print digraph.edges[node]

#bruteForceSearch(mitMap, '4', '5', 21, 1)    


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    shortestDistance = (0, [])
    #print '*'*20
    path = []
    path_list = []
    totalDistOutdoors = 0
    path_list = DFS(digraph, start, end, maxDistOutdoors, path, path_list, totalDistOutdoors)
    print path_list
    if not path_list:
        raise ValueError
    for path in path_list:
        totalDistance = 0
        for i in range(len(path) - 1):
            #print 'path: ', path
            edges = digraph.edges[path[i]]
            #print edges
            for edge in edges:
                #print edge[0], path[i + 1]
                if edge[0].getName() == path[i + 1].getName():
                    #print edge[1][0]
                    totalDistance += int(edge[1][0])
                    #print totalDistance
        if totalDistance <= maxTotalDist and (shortestDistance[0] == 0 or totalDistance < shortestDistance[0]):
            shortestDistance = (totalDistance, path)
    print shortestDistance
    if shortestDistance[0] > 0:
        return [x.getName() for x in shortestDistance[1]]
    else:
        raise ValueError   

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#    Test cases
    mitMap = load_map("mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

#    Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#    Test case 2
#    print "---------------"
#    print "Test case 2:"
#    print "Find the shortest-path from Building 32 to 56 without going outdoors"
#    expectedPath2 = ['32', '36', '26', '16', '56']
#    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#    print "Expected: ", expectedPath2
#    print "Brute-force: ", brutePath2
#    print "DFS: ", dfsPath2
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)
#
##    Test case 3
#    print "---------------"
#    print "Test case 3:"
#    print "Find the shortest-path from Building 2 to 9"
#    expectedPath3 = ['2', '3', '7', '9']
#    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath3
#    print "Brute-force: ", brutePath3
#    print "DFS: ", dfsPath3
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
#
##    Test case 4
#    print "---------------"
#    print "Test case 4:"
#    print "Find the shortest-path from Building 2 to 9 without going outdoors"
#    expectedPath4 = ['2', '4', '10', '13', '9']
#    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#    print "Expected: ", expectedPath4
#    print "Brute-force: ", brutePath4
#    print "DFS: ", dfsPath4
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
#
##    Test case 5
#    print "---------------"
#    print "Test case 5:"
#    print "Find the shortest-path from Building 1 to 32"
#    expectedPath5 = ['1', '4', '12', '32']
#    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#    print "Expected: ", expectedPath5
#    print "Brute-force: ", brutePath5
#    print "DFS: ", dfsPath5
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
#
##    Test case 6
#    print "---------------"
#    print "Test case 6:"
#    print "Find the shortest-path from Building 1 to 32 without going outdoors"
#    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#    print "Expected: ", expectedPath6
#    print "Brute-force: ", brutePath6
#    print "DFS: ", dfsPath6
#    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
#
##    Test case 7
#    print "---------------"
#    print "Test case 7:"
#    print "Find the shortest-path from Building 8 to 50 without going outdoors"
#    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#    try:
#        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#    except ValueError:
#        bruteRaisedErr = 'Yes'
#    
#    try:
#        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
#    
#    print "Expected: No such path! Should throw a value error."
#    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
#
#    Test case 8
#    print "---------------"
#    print "Test case 8:"
#    print "Find the shortest-path from Building 10 to 32 without walking"
#    print "more than 100 meters in total"
#    bruteRaisedErr = 'No'
#    dfsRaisedErr = 'No'
#    try:
#        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#    except ValueError:
#        bruteRaisedErr = 'Yes'
#    
#    try:
#        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#    except ValueError:
#        dfsRaisedErr = 'Yes'
#    
#    print "Expected: No such path! Should throw a value error."
#    print "Did brute force search raise an error?", bruteRaisedErr
#    print "Did DFS search raise an error?", dfsRaisedErr
