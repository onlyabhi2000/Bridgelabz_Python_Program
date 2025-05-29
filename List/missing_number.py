list1 = [1,2,3,4,6,7,8,9]
n = len(list1)+1

expected_sum = n*(n+1)//2

print("expected_sum-->",expected_sum)
actual_sum = sum(list1)
print("actula sum" , actual_sum)
#formula to get the missing number
result = expected_sum - actual_sum

print(result)


