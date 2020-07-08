'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    indices = []
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
        else:
            indices.append(i)

    zero_shifted = []

    for i in indices:
        zero_shifted.append(arr[i])

    for i in range(count):
        zero_shifted.append(0)

    return zero_shifted

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")