import time

#this function converts the listNumbers-n files to python lists
def files_to_lists(n): #n being the size of lists
    try:
        nsolfp = f"CollectionNumbers//listNumbers-{n}-nsol.txt"
        listnumsfp = f"CollectionNumbers//listNumbers-{n}.txt"

        with open(nsolfp, 'r') as file:
            notsolvedlist = [int(line.strip()) for line in file]

        with open(listnumsfp, 'r') as file:
            textlist = [int(line.strip()) for line in file]

        return notsolvedlist,textlist

    except:
        print("No such file exists!")

#this function runs the binary search/brute force algos 10 times according to the listNumbers-nsol files, then returns the average time
def run_tests(n,method=0):
    timetotal = 0
    # method 0 is brute force, method 1 is binary search'
    notsolvedlist,textlist = files_to_lists(n)
    for sumthing in notsolvedlist:
        start = time.time()
        if method == 0: print(brute_force(sumthing,textlist))
        if method == 1: print(binary_search(sumthing,textlist))
        end = time.time()
        timetotal += end - start
            
    average_time = timetotal/len(notsolvedlist)

    if method == 0: print(f"Method: brute force \nNumber of Runs: {n} \nAverage time per run: {average_time} seconds")
    if method == 1: print(f"Method: binary search \nNumber of Runs: {n} \nAverage time per run: {average_time} seconds")

#brute force algo to find if a list contain two integers, x and y, such that x + y = sum
def brute_force(sum,dalist):
    for i in dalist:
        if sum / 2 == i:
            return f"{i} plus itself equals {sum}!"

        for j in dalist:
            if i + j == sum:
                return f"{i} plus {j} equals {sum}!"
    return f"{sum} has no twosum!"

#binary search algo to find if a list contain two integers, x and y, such that x + y = sum
def binary_search(sum,dalist):
    dalist = list(dalist)
    dalist.sort()

    for i in dalist:
        if sum / 2 == i:
            return f"{i} plus itself equals {sum}!"
        y = sum - i
        if bs_sublist(dalist,0,len(dalist),y) != -1:
            return f"{i} plus {y} equals {sum}!"
    return f"{sum} has no twosum!"

#this binary search algorithm is the one I wrote in CSE2500
def bs_sublist(L,  left, right, item=0):
    """searches for item using `left` and `right` indices instead of slicing"""
    #print(L[left:right])
    
    # base case - item not in list
    if right == left and item < L[left]: return -1 
    if right - left <= 1 and L[left] != item and item != L[left]: return -1

    if right == left and item > L[right]: return -1
    if right - left <= 1 and L[left] != item and item != L[right]: return -1

    median = ((right - left) // 2) + left
    #print(left,median,right)
    # base case: found item
    if item == L[median]: return L[median]
        
    # item is in smaller half
    elif item < L[median]: return bs_sublist(L,left, median,item)

    # item is in bigger half
    else: return bs_sublist(L,median,right,item)

#run_tests(1000000,1)

