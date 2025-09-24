def activitySelection(start, finish):
    arr = list(zip(start, finish))
    # Sort activities by finish time
    arr.sort(key=lambda x: x[1])
    # At least one activity can be performed
    count = 1
    
    # Index of last selected activity
    j = 0

    for i in range(1, len(arr)):
        
        # Check if current activity starts
        # after last selected activity finishes
        if arr[i][0] > arr[j][1]: #arr[1][0] > arr[0][1]
            count += 1
            
            # Update last selected activity
            j = i

    return count

#time complexity: O(nlogn)
if __name__ == '__main__':
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print(activitySelection(start, finish))

    """
    1  2
    3  4
    0  6
    5  7
    8  9
    5  9
    """