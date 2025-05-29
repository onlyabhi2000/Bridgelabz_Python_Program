#Find triplets that add up to a zero

def three_sum(nums , target):
    seen= set()
    for num in nums :
        complement = target -num
        if complement in seen:
            return [complement , num]
        else:
            seen.add(num)


nums = [2,5,7 ,8]
target = 9
print(three_sum(nums, target))

