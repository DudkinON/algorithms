from typing import List


def max_sub_array_length(nums: List[int], k: int):

    _map = {0: -1}
    _sum = max_len = 0

    for i in range(len(nums)):
        _sum += nums[i]

        if _sum - k in _map:
            max_len = max(i - _map[_sum - k], max_len)

        if _sum not in _map:
            _map[_sum] = i

    return max_len
