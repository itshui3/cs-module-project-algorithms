'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    maximum = []
    max_tracker = [None, None]
    for i in range(len(arr) - k + 1):
        if max_tracker[0] is None:
            for l in range(i, i + k):
                if max_tracker[0] is None:
                    max_tracker[0], max_tracker[1] = arr[l], l
                elif arr[l] > max_tracker[0]:
                    max_tracker[0], max_tracker[1] = arr[l], l

        elif arr[i + (k-1)] > max_tracker[0]:
            max_tracker[0], max_tracker[1] = arr[i + (k-1)], i + (k-1)

        elif i > max_tracker[1]:
            max_tracker[0], max_tracker[1] = None, None
            for l in range(i, i + k):

                if max_tracker[0] is None:
                    max_tracker[0], max_tracker[1] = arr[l], l
                elif arr[l] > max_tracker[0]:
                    max_tracker[0], max_tracker[1] = arr[l], l
            
        maximum.append(max_tracker[0])

    return maximum

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
