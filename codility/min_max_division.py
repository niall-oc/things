# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/

def is_valid_minimal_limit(A, num_blocks, sum_slice_limit):
    """
    Scans Array A summing values until minimal_limit is reached.  Array A cannot
    be divided into more than num_blocks.  If the parameters given cannot succeed
    then a False is returned.
    """
    block_count = 0
    block_sum = 0

    for number in A:
        new = block_sum + number
        if new <= sum_slice_limit: # We have not breached the block sum limit
            block_sum = new
        else:                      # We have breached the block sum limit
            block_count += 1
            block_sum = number
        if block_count >= num_blocks:
            return False
    return True

def binary_search(A, num_blocks):
    """
    When array is divided into num_blocks the sum of each block searched to find
    the minimal highest block value.
    """
    sum_slice_min = max(A)
    sum_slice_max = sum(A)

    while sum_slice_min <= sum_slice_max:
        sum_slice_mid = (sum_slice_min + sum_slice_max) // 2
        #print(sum_slice_mid)
        if is_valid_minimal_limit(A, num_blocks, sum_slice_mid):
            sum_slice_max = sum_slice_mid - 1 # Search the lower half of the space
        else:
            sum_slice_min = sum_slice_mid + 1 # Search the upper half of the space
    
    return sum_slice_min

def solution(K, M, A):
    # Using M as the assumed max value of array A doesn't work!!!
    return binary_search(A, K)

if __name__ == '__main__':
    tests = (
        (6, ([2, 1, 5, 1, 2, 2, 2], 3, 5)),
    )
    for expected, args in tests:
        res = solution(*args)
        try:
            assert(expected == res)
        except AssertionError as e:
            print(expected, args, res)