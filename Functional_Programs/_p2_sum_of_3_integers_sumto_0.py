# 2. Sum of three Integer adds to ZERO
# a. Desc -> A program with cubic running time. Read in N integers and counts the
# number of triples that sum to exactly 0.
# b. I/P -> N number of integer, and N integer input array
# c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P -> One Output is number of distinct triplets as well as the second output is to
# print the distinct triplets.

def find_zero_sum_triplets(arr):
    n = len(arr)
    triplets = set()

    for i in range(n):
        for j in range(i+1 ,n):
            for k in range(j+1 , n):
                if arr[i] + arr[j] + arr[k] == 0:

                    triplet = tuple(sorted((arr[i], arr[j] ,arr[k])))
                    triplets.add(triplet)


    return triplets


n = int(input("Neter the number of numbers"))

numbers = []

for i in range(n):
    num = int(input(f"Enter numbers #{i+1} :  "))
    numbers.append(num)

print("the final numbers is ", numbers)


print(find_zero_sum_triplets(numbers))



