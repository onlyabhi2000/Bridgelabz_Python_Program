# Example dictionary
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sort by keys
sorted_dict = dict(sorted(my_dict.items() ,key=lambda x: x[1] ))

print(sorted_dict)
