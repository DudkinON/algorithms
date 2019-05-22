def three_sum(nums):

    n, cache, visited, output, zeros = len(nums), {}, {}, [], 0

    if n < 3:
        return []

    for i in range(n):
        if nums[i] == 0:
            zeros += 1
        visited[nums[i]] = i

    if zeros == len(nums):
        return [[0, 0, 0]]

    for i in range(n):
        for j in range(i + 1, n):
            x = -(nums[i] + nums[j])
            k = visited.get(x)
            if k is not None and k != i and k != j:
                lst = sorted([nums[k], nums[i], nums[j]])
                _id = "{}{}{}".format(lst[0], lst[1], lst[2])
                if cache.get(_id) is None:
                    cache[_id] = True
                    output.append(lst)
    return output
