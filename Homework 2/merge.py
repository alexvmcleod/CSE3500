import heapq

#takes arguement of k_lists, which is a list which contains k amount of lists
def merge_k_lists(k_lists):
    minheap = []
    heapq.heapify(minheap)

    #runs in O(nlogk) time, where n is the total amount of elements
    for k in k_lists:
        #adds every item in each sublist to a heap
        for n in k:
            #runs in O(logk) time
            heapq.heappush(minheap,n)

    newlist = []

    #pops every item from the minheap: runs in O(n) time
    while minheap:
        newlist.append(heapq.heappop(minheap))

    return newlist
