# Design an algo to return the minimum time it takes for all the n nodes to recieve this signal, if cannot be recieved, return -1
import heapq

# time is considered a list, the numbers of travel times as directed edges times[i] = [u (source), v (target), w (time)]
# n = how many nodes there are in the graph
# k = the starting node from where the signal first starts.
def network(times, n, k):
    
    # First create the sketch of the graph (adjacency list).
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append(v, w)
        
if (__name__ == "__main__"):
    None