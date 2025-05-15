list = [1, 2, 3, 4,5]

k= 2
print(list[:-k])
shifted_array = list[-k:] +list[:-k]
print(shifted_array)