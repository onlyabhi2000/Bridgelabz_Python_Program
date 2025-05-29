def two_sum(nums , target):
    seen= set()
    for num in nums:
        complement = target - num
        print("--" , complement)
        if complement in seen :
            return [complement , num]
        seen.add(num)

nums = [2, 7, 9, 5]
target = 9
print(two_sum(nums , target))


# 🕵️‍♂️ Dry Run:
# Input: [2, 7, 11, 15], target = 9

# seen = {}

# Check 2 → 9-2=7 → not in seen → add 2 → seen = {2}

# Check 7 → 9-7=2 → found in seen → return [2, 7]

