#Find all pairs in a list that sum up to a specific target.


def pair_sum(nums, target):
    seen = set()
    pairs = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            # Add sorted tuple to avoid duplicates like (2,7) and (7,2)
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return list(pairs)

nums = [2, 7, 9, 5, 4, 3, 6]
target = 9

result = pair_sum(nums, target)
print(result)

