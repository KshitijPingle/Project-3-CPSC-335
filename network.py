# Design an algo to return the minimum time it takes for all the n nodes to recieve this signal, if cannot be recieved, return -1
# We can use the 'heapq' library to solve our priority queue in Dijkstra's algorithm to retrieve smallest distance node.
import heapq

# time is considered a list, the numbers of travel times as directed edges times[i] = [u (source), v (target), w (time)]
# n = how many nodes there are in the graph
# k = the starting node from where the signal first starts.
def network(times, n, k):
    
    # First create the sketch of the graph (adjacency list).
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
        
    # Initialize list for analyzing the shortest distance to each node.
    dist = {i: float('inf') for i in range(1, n + 1)} # this is just presetting a value of infinite to all nodes.
    dist[k] = 0 # Starting point for the signal.
    min_heap = [(0, k)] # (time, node); just saying that the distance from k -> k is 0.
    
    # Loop through each node possible while prio queue is not empty.
    while min_heap:
        # pop the smallest distance node from the priority queue.
        time, node = heapq.heappop(min_heap)
        
        # skips the current node path if it takes longer than the 'known' shortest distance.
        if time > dist[node]:
            continue
        
        # Iterate through other potential nodes aka 'neighbor' nodes.
        # Grabs the 'node' and 'delay' time to travel from current node to neighbor node.
        # Calculates time to reach neighbor and uploads the 'best' shortest time.
        for neighbor, delay in graph[node]:
            shortest_time = time + delay
            
            # If a even shorter time is found, update 'shortest_time' value with the new calculated value.
            # Updates dist[neightbor], then push back to min_heap to explore their neighbors.
            if shortest_time < dist[neighbor]:
                dist[neighbor] = shortest_time
                heapq.heappush(min_heap, (shortest_time, neighbor))
                
    # Returns back to the current 'dist' dictonary to check the value of the 'slowest' delay time of dist[node]
    max_time = max(dist.values())
    
    # Return "null" value or in this case '-1' if any dist[node] value is still infinite after sorting through.
    if max_time == float('inf'):
        return -1
    
    # Returns the delay time it takes to reach all nodes.
    return max_time
    
if (__name__ == "__main__"):
    
    # Sample 1
    times1 = [[2,1,1], [2,3,1], [3,4,1]]
    n1 = 4
    k1 = 2
    
    # Sample 2
    times2 = [[1,2,1]]
    n2 = 2
    k2 = 1
    
    # Sample 3
    times3 = [[1,2,1]]
    n3 = 2
    k3 = 2
    
    # Print the outputs and catagorize/label each outputs.
    print("Sample_1 Output: " + str(network(times=times1, n=n1, k=k1)))
    print("Sample_2 Output: " + str(network(times=times2, n=n2, k=k2)))
    print("Sample_3 Output: " + str(network(times=times3, n=n3, k=k3)))
    
    