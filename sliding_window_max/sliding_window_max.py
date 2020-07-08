'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_per_win = []
    for i in range(len(nums) - (k - 1)):
        max_win_num = nums[i]

        if k > 1: 
            for l in range(i + 1, i + k):
                if max_win_num < nums[l]:
                    max_win_num = nums[l]
        else:
            print('k not greater than 1')
            for l in range(i, i + k):
                if max_win_num < nums[l]:
                    max_win_num = nums[l]

        max_per_win.append(max_win_num)

    return max_per_win



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
