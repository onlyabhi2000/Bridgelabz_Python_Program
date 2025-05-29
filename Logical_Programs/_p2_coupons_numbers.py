# Coupon Numbers
# a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
# need to generate distinct coupon number? This program simulates this random
# process.
# b. I/P -> N Distinct Coupon Number
# c. Logic -> repeatedly choose a random number and check whether it's a new one.
# d. O/P -> total random number needed to have all distinct numbers.
# e. Functions => Write Class Static Functions to generate random number and to
# process distinct coupons
import random


def collect_coupons(n):
    collected_coupons = set()
    count = 0
    while len(collected_coupons) < n :
        number = random.randint(0 , n-1)
        count+=1
        collected_coupons.add(number)

    print("Total count required is: ",count)


n = int(input("Enter the number of distinct coupon number :"))

collect_coupons(n)